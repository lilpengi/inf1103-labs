#Handling valid input
def get_valid_input():
    delivery = input("Enter delivery amount (or type 'quit' to finish): ")

    if delivery.lower() == "quit":
        return "quit"

    if not delivery.isdigit():
        print("Error: Invalid input. Please enter a whole number.")
        return None

    quantity = int(delivery)

    if quantity < 0:
        print("Error: Negative numbers are not allowed.")
        return None

    return quantity

# this is to calculate the new total amt everytime the user inputs a new number
def process_delivery(current_total, new_value):
    return current_total + new_value

#calculates tax
def calculate_tax(amount):
    return amount * 0.1

#generating final report to be printed for user
def generate_report(total_units, failed_attempts):
    print("\n--- Final Report ---")
    print(f"Total Deliveries Processed: {total_units}")
    print(f"Number of Failed/Rejected Entries: {failed_attempts}")


def main():
    # Initialize inventory and counters to zero at the start
    total_inventory = 0
    failed_entries = 0

    # run in a continuous loop until the user types 'quit'
    while True:
        result = get_valid_input()

        if result == "quit":
            break

        if result is None:
            # Invalid entry (non-numeric or negative) — count it and retry
            failed_entries += 1
            continue

        #result is a valid integer at this point
        quantity = result

        #update running total
        total_inventory = process_delivery(total_inventory, quantity)

        #calculate tax for this delivery
        tax = calculate_tax(quantity)

    # 4. Reporting when user quits
    generate_report(total_inventory, failed_entries)


if __name__ == "__main__":
    main()