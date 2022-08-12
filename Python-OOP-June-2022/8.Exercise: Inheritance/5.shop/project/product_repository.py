from project.product import Product


class ProductRepository(Product):
    def __init__(self):
        self.products = []

    def add(self, product: Product):
        self.products.append(product)
        self.to_use = product

    def find(self, product_name: str):
        for product in self.products:
            if product.name == product_name:
                return product

    def remove(self, product_name):
        for product in self.products:
            if product_name in self.products:
                self.product.remove(product)

    def __repr__(self):
        list_all_items = ''
        for el in self.products:
            list_all_items += f"{el}: {self.to_use.quantity}\n"

        return list_all_items.strip()
