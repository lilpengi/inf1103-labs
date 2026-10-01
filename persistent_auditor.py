ORDERS_FILE = "inventory.txt"   # change this one line if your TA says orders.txt


def load_inventory():
    """Read the file and return a list of order dictionaries."""
    orders = []
    try:
        with open(ORDERS_FILE, "r") as f:
            for line in f:
                line = line.strip()
                if line == "":          # skip blank lines
                    continue
                parts = line.split(",")
                if len(parts) != 3:     # skip badly formatted lines
                    continue
                orders.append({
                    "id": int(parts[0]),
                    "product": parts[1].strip(),
                    "quantity": int(parts[2]),
                })
    except FileNotFoundError:
        pass                            # no file yet: start with an empty list
    return orders


def print_current_orders(orders):
    print("Current Orders:")
    for order in orders:
        print(f"{order['id']}, {order['product']}, {order['quantity']}")


def get_product_name():
    while True:
        product = input("Enter Product Name: ").strip()
        if product.lower() == "quit":
            return "quit"
        if product == "":
            print("Invalid input. Please enter a valid product name.")
            continue
        return product


def get_quantity():
    while True:
        quantity_str = input("Enter Quantity: ").strip()
        if quantity_str.lower() == "quit":
            return "quit"
        try:
            quantity = int(quantity_str)
        except ValueError:
            print("Invalid input. Please enter a whole number.")
            continue
        if quantity <= 0:
            print("Invalid input. Quantity must be a positive whole number.")
            continue
        return quantity


def get_next_id(orders):
    if orders:
        return orders[-1]["id"] + 1     # last order's id + 1
    return 1001                         # first ever order


def main():
    orders = load_inventory()
    print_current_orders(orders)

    while True:
        product = get_product_name()
        if product == "quit":
            break

        quantity = get_quantity()
        if quantity == "quit":
            break

        new_id = get_next_id(orders)
        orders.append({"id": new_id, "product": product, "quantity": quantity})

        print("\nNew Order Added:")
        print(f"{new_id},{product},{quantity}\n")


if __name__ == "__main__":
    main()