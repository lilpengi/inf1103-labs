class Product:
    def __init__(self, product_id, name, price, stock):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock

    def get_product_id(self):
        return self.__product_id

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_stock(self):
        return self.__stock

    def update_stock(self, quantity):
        self.__stock = quantity

    def display_information(self):
        print(
            f"ID: {self.__product_id} | "
            f"Name: {self.__name} | "
            f"Price: ${self.__price:.2f} | "
            f"Stock: {self.__stock}"
        )

class PhysicalProduct(Product):
    def __init__(self, product_id, name, price, stock, weight):
        super().__init__(product_id, name, price, stock) #key line being used
        self.__weight = weight

    def get_weight(self):
        return self.__weight

    def display_information(self):
        print(
            f"ID: {self.get_product_id()} | "
            f"Name: {self.get_name()} | "
            f"Price: ${self.get_price():.2f} | "
            f"Stock: {self.get_stock()} | "
            f"Weight: {self.__weight} kg"
        )

class DigitalProduct(Product):
    def __init__(self, product_id, name, price, stock, download_size):
        super().__init__(product_id, name, price, stock)
        self.__download_size = download_size

    def get_download_size(self):
        return self.__download_size

    def display_information(self):
        print(
            f"ID: {self.get_product_id()} | "
            f"Name: {self.get_name()} | "
            f"Price: ${self.get_price():.2f} | "
            f"Stock: {self.get_stock()} | "
            f"Download Size: {self.__download_size} MB"
        )