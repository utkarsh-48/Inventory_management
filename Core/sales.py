import json
import os
from datetime import datetime

class Sales:
    def __init__(self):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.sales_file = os.path.join(base_dir, "data", "sales.json")
        self.stock_file = os.path.join(base_dir, "data", "stock.json")

        self.sales = self.load_sales()
        self.stock = self.load_stock()

    def load_sales(self):
        try:
            with open(self.sales_file, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_sales(self):
        with open(self.sales_file, "w") as f:
            json.dump(self.sales, f, indent=2)

    def load_stock(self):
        try:
            with open(self.stock_file, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    def save_stock(self):
        with open(self.stock_file, "w") as f:
            json.dump(self.stock, f, indent=2)

    def record_sale(self, shop, products, user):
        print("\n=== Record Sale ===")

        # Show products:
        print(f"{'ID':<5} {'Name':<30}")
        for p in products:
            print(f"{p['id']:<5} {p['name']:<30}")

        product_id = input("Enter Product ID sold: ").strip()
        try:
            qty = int(input("Enter quantity sold: "))
        except ValueError:
            print("Invalid quantity. Please enter a number.")
            return

        # Find product
        product = next((p for p in products if str(p['id']) == product_id), None)
        if not product:
            print("Invalid product ID.")
            return

        # Check stock
        if shop not in self.stock:
            self.stock[shop] = {}
        current_qty = self.stock[shop].get(product_id, 0)
        if qty > current_qty:
            print(f"Not enough stock. Available: {current_qty}")
            return

        # Reduce stock
        self.stock[shop][product_id] = current_qty - qty
        self.save_stock()

        # Create sale entry
        total_amount = qty * product['price']
        sale_entry = {
            "sale_id": len(self.sales) + 1,
            "shop": shop,
            "product_id": product_id,
            "product_name": product['name'],
            "quantity": qty,
            "total_amount": total_amount,
            "sold_by": user['username'],
            "date": datetime.now().strftime("%Y-%m-%d")
        }

        self.sales.append(sale_entry)
        self.save_sales()

        print(f"Sale recorded. Total amount: {total_amount}")
