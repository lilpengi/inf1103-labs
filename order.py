
from product import Product
from order_line import OrderLine


class Order:
    def __init__(self, order_id: str):
        self.order_id: str = order_id
        self.order_lines: list[OrderLine] = []

    def add_order_line(self, product: Product, quantity: int) -> None:
        order_line = OrderLine(product, quantity)
        self.order_lines.append(order_line)

    def remove_order_line(self, product_id: str) -> None:
        for line in self.order_lines:
            if line.product.get_product_id() == product_id:
                self.order_lines.remove(line)
                return

    def calculate_total(self) -> float:
        total = 0.0

        for line in self.order_lines:
            total += line.calculate_subtotal()

        return total
