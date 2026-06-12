"""
Name: Derek R. Neilson
Description: Fountain View Hall's event attendance & revenue tracker.
"""


def main():
    total_events = 0
    total_guests = 0
    total_projected_revenue = 0
    average_revenue = 0

    LARGE_GUEST_AMOUNT = 60
    LARGE_GUEST_DISCOUNT_PERCENT = 0.80  # 20 percent discount

    while True:
        guest_count = -1
        projected_revenue = -1

        event_name = input(
            "What is the name of your event?\nenter a name or done to quit: "
        )

        if event_name.lower().strip() == "done":
            break

        while guest_count < 0:
            try:
                guest_count = int(
                    input(
                        "\nHow many guests are attending the event?\nEnter a integer eg.(53) or zero to quit: "
                    )
                )
                total_guests += guest_count
                if guest_count >= LARGE_GUEST_AMOUNT:
                    percent_off = (1 - LARGE_GUEST_DISCOUNT_PERCENT) * 100
                    print(
                        f"Receives a {percent_off:n} discount because of how much guests are present"
                    )
                if guest_count == 0:
                    break
            except ValueError as e:
                print(e)
        if guest_count == 0:
            break
        while projected_revenue < 0:
            try:
                projected_revenue = float(
                    input(
                        "\nHow mach revenue do you estimate\nEnter a number eg.(53.50) or zero to quit:  "
                    )
                )
                total_projected_revenue += projected_revenue
                if projected_revenue == 0:
                    break
            except ValueError as e:
                print(e)
        if projected_revenue == 0:
            break

        total_events += 1

    try:
        average_revenue = total_projected_revenue / total_events
    except ZeroDivisionError:
        print("\nDefaulting to zero as there where no events or revenue")

    print(f"""
Event Revenue Summary
{"-" * 65}
Total events: {total_events}
Total guest count: {total_guests}
Total projected revenue: {total_projected_revenue:,.2f}
Average revenue: {average_revenue}
{"-" * 65}
""")


if __name__ == "__main__":
    main()
