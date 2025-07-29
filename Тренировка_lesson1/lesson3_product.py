class Product:

    def __init__(self, name, price):
        self.product_name = name
        self.product_price = price

    def get_name(self):
        return self.product_name

    def get_price(self):
        return self.product_price

    def get_product_info(self):
        return f"Product: {self.product_name}, Price: {self.product_price}"
