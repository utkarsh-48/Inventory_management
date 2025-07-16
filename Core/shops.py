import json
import os

class ShopManager:
    def __init__(self):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.shops_file = os.path.join(base_dir, "data", "shops.json")
        self.shops = self.load_shops()

    def load_shops(self):
        try:
            with open(self.shops_file, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

    def view_shops(self):
        print("\n=== Shops ===")
        for shop_id, shop_name in self.shops.items():
            print(f"{shop_id}. {shop_name}")

    def get_shop_name(self, shop_id):
        return self.shops.get(shop_id, "Unknown Shop")
