"""
Name: Derek R. Neilson
Description: Fountain View Hall's event attendance & revenue tracker.
"""


def main():
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
                guest_count = int(input("How many guests are attending the event: "))
            except ValueError as e:
                print(e)

        while projected_revenue < 0:
            try:
                projected_revenue = int(input("How mach revenue do you estimate "))
            except ValueError as e:
                print(e)


if __name__ == "__main__":
    main()
