import json
import os

from product import Product, PhysicalProduct, DigitalProduct
from inventory import Inventory

INVENTORY_FILE = "inventory.json"


def load_inventory():
    inventory = Inventory()

    if os.path.exists(INVENTORY_FILE):
        print("inventory.json found.")

        try:
            with open(INVENTORY_FILE, "r") as f:
                data = json.load(f)

            for item in data:
                product = Product(
                    item["id"],
                    item["name"],
                    item["price"],
                    item["stock"]
                )

                inventory.add_product(product)

            print("Inventory loaded successfully.")

        except (json.JSONDecodeError, OSError):
            print(
                "Could not read inventory.json. "
                "Starting with an empty inventory."
            )

    else:
        print(
            "inventory.json not found. "
            "Starting with an empty inventory."
        )

    return inventory


def add_product(inventory):
    print("\nAdd New Product")
    print("1. Physical Product")
    print("2. Digital Product")

    product_type = input("Select product type: ").strip()

    if product_type not in ("1", "2"):
        print("Invalid product type.")
        return

    product_id = input("Product ID: ").strip()

    if inventory.search_product(product_id):
        print("A product with that ID already exists.")
        return

    name = input("Product Name: ").strip()

    try:
        price = float(input("Price: "))
        stock = int(input("Stock Quantity: "))
    except ValueError:
        print("Invalid price or stock. Product not added.")
        return

    if product_type == "1":
        try:
            weight = float(input("Weight (kg): "))
        except ValueError:
            print("Invalid weight. Product not added.")
            return

        product = PhysicalProduct(
            product_id,
            name,
            price,
            stock,
            weight
        )

    else:
        try:
            download_size = float(input("Download Size (MB): "))
        except ValueError:
            print("Invalid download size. Product not added.")
            return

        product = DigitalProduct(
            product_id,
            name,
            price,
            stock,
            download_size
        )

    inventory.add_product(product)
    print("Product added successfully!")

def update_stock(inventory):
    print("\nUpdate Stock")

    product_id = input("Enter Product ID: ").strip()
    product = inventory.search_product(product_id)

    if product is None:
        print("Product not found.")
        return

    print("Product Found:")
    print(f"Name: {product.get_name()}")
    print(f"Current Stock: {product.get_stock()}")

    try:
        new_stock = int(input("New Stock Quantity: "))
    except ValueError:
        print("Invalid quantity. Stock not updated.")
        return

    product.update_stock(new_stock)

    print("Stock updated successfully!")


def search_product(inventory):
    print("\nSearch Product")

    product_id = input("Enter Product ID: ").strip()
    product = inventory.search_product(product_id)

    if product is None:
        print("Product not found.")
        return

    print("Product Found")
    print("-" * 48)
    product.display_information()
    print("-" * 48)


def save_inventory(inventory):
    print("Saving inventory...")

    data = []

    for product in inventory.get_products():
        product_data = {
            "id": product.get_product_id(),
            "name": product.get_name(),
            "price": product.get_price(),
            "stock": product.get_stock()
        }

        data.append(product_data)

    try:
        with open(INVENTORY_FILE, "w") as f:
            json.dump(data, f, indent=4)

        print(
            f"Inventory saved successfully to "
            f"{INVENTORY_FILE}."
        )

    except OSError as e:
        print(f"Error saving inventory: {e}")


def print_menu():
    print("\n----------- MENU -----------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("----------------------------")


def main():
    print("=" * 40)
    print("INVENTORY MANAGEMENT SYSTEM")
    print("=" * 40)

    inventory = load_inventory()

    while True:
        print_menu()
        choice = input("Enter option: ").strip()

        if choice == "1":
            inventory.display_all()

        elif choice == "2":
            add_product(inventory)

        elif choice == "3":
            update_stock(inventory)

        elif choice == "4":
            search_product(inventory)

        elif choice == "5":
            save_inventory(inventory)

        elif choice == "6":
            print("Saving inventory before exit...")
            save_inventory(inventory)
            print(
                "Thank you for using "
                "Inventory Management System."
            )
            print("Program terminated.")
            break

        else:
            print(
                "Invalid option. "
                "Please enter a number from 1 to 6."
            )


if __name__ == "__main__":
    main()