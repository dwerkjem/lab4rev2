#!/usr/bin/env bash

set -euo pipefail

mkdir -p completions

# set env variables
_FVH_MANAGER_COMPLETE=source_bash uv run fvh-manager > completions/fvh-manager.bash
_FVH_MANAGER_COMPLETE=source_zsh uv run fvh-manager > completions/_fvh-manager
_FVH_MANAGER_COMPLETE=source_fish uv run fvh-manager > completions/fvh-manager.fish
_FVH_MANAGER_COMPLETE=source_powershell uv run fvh-manager > completions/fvh-manager.ps1

git add \
  completions/fvh-manager.bash \
  completions/_fvh-manager \
  completions/fvh-manager.fish \
  completions/fvh-manager.ps1