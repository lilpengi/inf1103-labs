ORDERS_FILE = "inventory.txt"   # change this one line if your TA says orders.txt


def load_orders(): #to read the orders from the file and return them as a list of dictionaries
    orders = [] #initialize an empty list to hold the orders
    try:
        with open(ORDERS_FILE, "r") as f: #open the file for reading
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


def main():
    orders = load_orders()
    print_current_orders(orders)

if __name__ == "__main__":
    main()