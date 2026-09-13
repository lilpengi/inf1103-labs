# 1. Initialize your inventory to zero in the start
total_inventory = 0
failed_entries = 0

# 2. Run in a continuous loop asking user to enter a stock quantity, until the user types quit.
while True:
    user_input = input("Enter stock quantity (or type 'quit' to finish): ")

    #when user types quit, the loop should break.
    if user_input.lower() == "quit":
        break

    # 4. Handling invalid input
    if not user_input.isdigit():
        print("Error: Invalid input. Please enter a whole number.")
        failed_entries += 1
        continue

    # 3. Accept stock values as integers
    quantity = int(user_input)

    # 5.: Enforce business rules - reject negative numbers
    if quantity < 0:
        print("Error: Negative numbers are not allowed.")
        failed_entries += 1
        continue

    # 6. Manage state: Keep a running total of the inventory
    total_inventory += quantity

    # 7. Trigger Overstock Alert
    if total_inventory > 500:
        print(f"ALERT: Overstock detected! Total inventory is {total_inventory}, which exceeds 500 units.")
        break
    elif total_inventory == 500:
        print("Inventory has reached exactly 500 units.")
    else:
        print(f"Accepted. Current total inventory: {total_inventory}")

# 8. Reporting
print("\n--- Final Report ---")
print(f"Total Units Processed: {total_inventory}")
print(f"Number of Failed/Rejected Entries: {failed_entries}")