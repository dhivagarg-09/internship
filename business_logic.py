# business_logic.py

def process_orders(products, orders):
    for order in orders:
        product = products[order['product_id']]
        if product['stock'] >= order['quantity']:
            product['stock'] -= order['quantity']
            print(f"{product['name']} order processed. Remaining stock: {product['stock']}")
        else:
            print(f"Insufficient stock for {product['name']}")

        # Trigger alert if stock is below threshold (10 units)
        if product['stock'] < 10:
            print(f"Alert: {product['name']} needs restocking!")

def restock_items(products, restock_list):
    for restock in restock_list:
        product = products[restock['product_id']]
        product['stock'] += restock['quantity']
        print(f"{product['name']} restocked. New stock: {product['stock']}")


# Example data for testing
if __name__ == "__main__":
    products = {
        1: {'name': 'Product 1', 'stock': 15},
        2: {'name': 'Product 2', 'stock': 8}
    }

    orders = [
        {'product_id': 1, 'quantity': 6},
        {'product_id': 2, 'quantity': 3}
    ]

    restock_list = [
        {'product_id': 2, 'quantity': 10}
    ]

    process_orders(products, orders)
    restock_items(products, restock_list)
