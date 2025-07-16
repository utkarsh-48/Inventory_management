import json
import os
from datetime import datetime

class Reports:
    def __init__(self):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.sales_file = os.path.join(base_dir, "data", "sales.json")
        self.stock_file = os.path.join(base_dir, "data", "stock.json")
        self.products_file = os.path.join(base_dir, "data", "products.json")

        self.sales = self.load_file(self.sales_file)
        self.stock = self.load_file(self.stock_file)
        self.products = self.load_file(self.products_file)

    def load_file(self, file_path):
        try:
            with open(file_path, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return [] if "sales" in file_path else {}

    def sales_by_shop(self, shop):
        print(f"\n=== Sales Report for {shop} ===")
        total = 0
        for sale in self.sales:
            if sale['shop'] == shop:
                print(f"ID: {sale['sale_id']} | Product: {sale['product_name']} | Qty: {sale['quantity']} | Total: {sale['total_amount']} | Date: {sale['date']}")
                total += sale['total_amount']
        print(f"Total Sales for {shop}: {total}")

    def sales_by_user(self, username):
        print(f"\n=== Sales Report for User: {username} ===")
        total = 0
        for sale in self.sales:
            if sale['sold_by'] == username:
                print(f"Shop: {sale['shop']} | Product: {sale['product_name']} | Qty: {sale['quantity']} | Total: {sale['total_amount']} | Date: {sale['date']}")
                total += sale['total_amount']
        print(f"Total Sales by {username}: {total}")

    def sales_by_date_range(self, start_date, end_date):
        print(f"\n=== Sales Report from {start_date} to {end_date} ===")
        total = 0
        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")

        for sale in self.sales:
            sale_date = datetime.strptime(sale['date'], "%Y-%m-%d")
            if start <= sale_date <= end:
                print(f"Shop: {sale['shop']} | Product: {sale['product_name']} | Qty: {sale['quantity']} | Total: {sale['total_amount']} | Date: {sale['date']}")
                total += sale['total_amount']
        print(f"Total Sales in range: {total}")

    def global_sales_comparison(self):
        print("\n=== Global Sales Comparison ===")
        shop_totals = {}

        for sale in self.sales:
            shop = sale['shop']
            shop_totals[shop] = shop_totals.get(shop, 0) + sale['total_amount']

        for shop, total in shop_totals.items():
            print(f"{shop}: {total}")

    def stock_report(self, shop):
        print(f"\n=== Stock Report for {shop} ===")
        print(f"{'ID':<5} {'Name':<30} {'Qty':<10} {'Reorder Level':<15}")

        for product in self.products:
            pid = str(product['id'])
            qty = self.stock.get(shop, {}).get(pid, 0)
            reorder_level = product.get('reorder_level', 0)
            alert = "LOW" if qty <= reorder_level else ""
            print(f"{pid:<5} {product['name']:<30} {qty:<10} {reorder_level:<15} {alert}")
