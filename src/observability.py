"""
Sets up logging and metrics for the application.

:author: Derek R. Neilson
:var logger: Application logger configured for OpenTelemetry.
:var meter: OpenTelemetry meter used to create counters and histograms.

This module configures OpenTelemetry logging and metrics, then exposes
the ``track_command`` decorator for tracking CLI command execution.
"""

import logging
import time
from collections.abc import Callable
from functools import wraps
from typing import Any, TypeVar, cast
import requests
from opentelemetry.metrics import Meter
from opentelemetry import _logs, metrics
from opentelemetry.exporter.otlp.proto.http._log_exporter import OTLPLogExporter
from opentelemetry.exporter.otlp.proto.http.metric_exporter import OTLPMetricExporter
from opentelemetry.sdk._logs import LoggerProvider, LoggingHandler
from opentelemetry.sdk._logs.export import BatchLogRecordProcessor
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader
from opentelemetry.sdk.resources import Resource

from src import __version__

APP_VERSION = __version__
SERVICE_NAME = "fountain-view-hall"
OTLP_URL = "http://localhost:4318"

try:
    response = requests.post(
        f"{OTLP_URL}/v1/logs",
        data=b"",  # send empty string as bytes
        headers={"Content-Type": "application/x-protobuf"},
    )
    otlp_is_available = response.status_code in {200, 400, 405, 415}
except requests.RequestException:
    otlp_is_available = False


resource = Resource.create(
    {
        "service.name": SERVICE_NAME,
        "service.version": APP_VERSION,
    }
)


def configure_logging() -> logging.Logger:
    """Configure and return the application logger."""
    logger = logging.getLogger(SERVICE_NAME)
    logger.setLevel(logging.INFO)

    if otlp_is_available:
        logger_provider = LoggerProvider(resource=resource)
        _logs.set_logger_provider(logger_provider)

        log_exporter = OTLPLogExporter(
            endpoint=OTLP_URL + "/v1/logs",
        )

        logger_provider.add_log_record_processor(BatchLogRecordProcessor(log_exporter))

        otel_handler = LoggingHandler(
            level=logging.INFO,
            logger_provider=logger_provider,
        )

        if not any(isinstance(handler, LoggingHandler) for handler in logger.handlers):
            logger.addHandler(otel_handler)

        logger.propagate = False
    else:
        logger.addHandler(logging.StreamHandler())

    return logger


def configure_metrics() -> Meter:
    """Configure and return the application metrics meter."""
    if otlp_is_available:
        metric_exporter = OTLPMetricExporter(
            endpoint=OTLP_URL + "/v1/metrics",
        )

        metric_reader = PeriodicExportingMetricReader(
            metric_exporter,
            export_interval_millis=5_000,
        )

        meter_provider = MeterProvider(
            resource=resource,
            metric_readers=[metric_reader],
        )

        metrics.set_meter_provider(meter_provider)

    return metrics.get_meter(SERVICE_NAME, APP_VERSION)


logger = configure_logging()
meter = configure_metrics()

errors_counter = meter.create_counter(
    name="lab4.errors",
    description="Number of errors.",
    unit="1",
)

command_runs_counter = meter.create_counter(
    name="lab4.cli.commands",
    description="Number of CLI commands executed.",
    unit="1",
)

command_duration_histogram = meter.create_histogram(
    name="lab4.cli.command.duration",
    description="CLI command execution duration.",
    unit="s",
)

db_query_duration_histogram = meter.create_histogram(
    name="lab4.db.query.duration",
    description="Database query duration.",
    unit="s",
)

active_operations_counter = meter.create_up_down_counter(
    name="lab4.active_operations",
    description="Number of currently active operations.",
    unit="1",
)


F = TypeVar("F", bound=Callable[..., Any])


def track_command(command_name: str) -> Callable[[F], F]:
    """
    Track command execution with logs and metrics.

    The wrapped function records the number of command runs, active operations,
    errors, and command duration.

    Args:
        command_name: Name of the command being tracked. Format not required but should be name-of-command

    Example:
        .. code-block:: python

            from src.observability import logger, track_command

            @track_command("some-command")
            def some_command():
                logger.info("Command executed")
    """

    def decorator(func: F) -> F:
        @wraps(func)
        def wrapper(
            *args: Any, **kwargs: Any
        ) -> Any:  # positional and keyword arguments are passed
            attributes = {"command": command_name}

            command_runs_counter.add(1, attributes)
            active_operations_counter.add(1, attributes)

            start = time.perf_counter()

            try:
                logger.info("command started", extra=attributes)
                result = func(*args, **kwargs)
                logger.info("command completed", extra=attributes)
                return result
            except Exception:
                errors_counter.add(1, attributes)
                logger.exception("command failed", extra=attributes)
                raise
            finally:
                duration = time.perf_counter() - start
                command_duration_histogram.record(duration, attributes)
                active_operations_counter.add(-1, attributes)

        return cast(F, wrapper)

    return decorator
