"""
Name: Derek R. Neilson
Description: Fountain View Hall's event attendance & revenue tracker.
"""

import pandas as pd


def main():
    total_events = 0
    total_guests = 0
    total_projected_revenue = 0.0
    total_discount_amount = 0.0
    largest_event = 0

    events = []

    LARGE_GUEST_AMOUNT = 60
    LARGE_GUEST_DISCOUNT_PERCENT = 0.80  # Customer pays 80%, meaning 20% off.

    while True:
        event_name = input(
            "What is the name of your event?\nEnter a name or done to quit: "
        ).strip()

        if event_name.lower() == "done":
            break

        guest_count = -1
        projected_revenue_before_discount = -1.0

        # Every booking must include a valid guest count.
        while guest_count <= 0:
            try:
                guest_count = int(
                    input(
                        "\nHow many guests are attending the event?\n"
                        "Enter a positive integer, eg. 53: "
                    )
                )

                if guest_count <= 0:
                    print("Guest count must be greater than zero.")

            except ValueError:
                print("Please enter a valid whole number for guest count.")

        # Assumption: the user enters the booking total before any discount is applied.
        while projected_revenue_before_discount < 0:
            try:
                projected_revenue_before_discount = float(
                    input(
                        "\nHow much revenue do you estimate before discounts?\n"
                        "Enter a number, eg. 53.50: "
                    )
                )

                if projected_revenue_before_discount < 0:
                    print("Projected revenue cannot be negative.")

            except ValueError:
                print("Please enter a valid number for projected revenue.")

        discount_amount = 0.0
        final_projected_revenue = projected_revenue_before_discount

        # Large events receive a 20% discount.
        if guest_count >= LARGE_GUEST_AMOUNT:
            discount_amount = projected_revenue_before_discount * (
                1 - LARGE_GUEST_DISCOUNT_PERCENT
            )
            final_projected_revenue = (
                projected_revenue_before_discount * LARGE_GUEST_DISCOUNT_PERCENT
            )

            print(
                f"{event_name} receives a {discount_amount:,.2f} discount "
                "because it is a large event."
            )

        total_events += 1
        total_guests += guest_count
        total_projected_revenue += final_projected_revenue
        total_discount_amount += discount_amount

        if guest_count > largest_event:
            largest_event = guest_count

        # Store each event so pandas can display the event data later.
        events.append(
            {
                "Event Name": event_name,
                "Guests": guest_count,
                "Revenue Before Discount": projected_revenue_before_discount,
                "Discount Amount": discount_amount,
                "Final Projected Revenue": final_projected_revenue,
            }
        )

    if total_events > 0:
        average_guests = total_guests / total_events
        average_revenue = total_projected_revenue / total_events
    else:
        average_guests = 0
        average_revenue = 0

    event_dataframe = pd.DataFrame(events)

    print("\nEvent Data")
    print("-" * 65)

    if event_dataframe.empty:
        print("No events were entered.")
    else:
        print(event_dataframe.to_string(index=False))

    print(f"""
Event Revenue Summary
{"-" * 65}
Events Processed: {total_events}
Total Guests: {total_guests:,}
Total Revenue: ${total_projected_revenue:,.2f}
Total Discounts Given: ${total_discount_amount:,.2f}
Average Guests Per Event: {average_guests:,.2f}
Average Revenue Per Event: ${average_revenue:,.2f}
Largest Event: {largest_event:,} Guests
{"-" * 65}
""")


if __name__ == "__main__":
    main()
