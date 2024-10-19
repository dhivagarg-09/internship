# system_design.py

class User:
    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.orders = []

    def create_order(self, order):
        self.orders.append(order)

    def view_orders(self):
        return self.orders

class Product:
    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock

class Order:
    def __init__(self, order_id, user_id):
        self.order_id = order_id
        self.user_id = user_id
        self.products = []
        self.status = "pending"

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)

    def view_products(self):
        return [product.name for product in self.products]

class Payment:
    def __init__(self, payment_id, order_id, amount):
        self.payment_id = payment_id
        self.order_id = order_id
        self.amount = amount
        self.status = "pending"

    def make_payment(self):
        self.status = "completed"
