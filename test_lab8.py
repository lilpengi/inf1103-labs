
from supplier import Supplier
from product import Product, PhysicalProduct, DigitalProduct
from inventory import Inventory


def show_product_details(product: Product) -> None:
    product.display_information()
    print(product.get_fulfilment_info())


def test_product_substitution() -> None:
    supplier = Supplier("S001", "Apple", "apple@example.com")

    iphone = PhysicalProduct(
        "P001", "iPhone", 1200.0, 10, 0.5, supplier
    )

    app = DigitalProduct(
        "P002", "Mobile App", 20.0, 50, 100.0, supplier
    )

    inventory = Inventory()
    inventory.add_product(iphone)
    inventory.add_product(app)

    assert len(inventory.get_products()) == 2

    for product in inventory.get_products():
        show_product_details(product)

        old_stock = product.get_stock()
        product.update_stock(old_stock + 5)

        assert product.get_stock() == old_stock + 5
        assert isinstance(product.get_fulfilment_info(), str)

    assert iphone.get_fulfilment_info() == (
        "This product requires physical shipping."
    )

    assert app.get_fulfilment_info() == (
        "This product is delivered digitally."
    )

    print("LSP and polymorphism tests passed!")


if __name__ == "__main__":
    test_product_substitution()
