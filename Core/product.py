import json
import os

class Product:
    def __init__(self):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.products_file = os.path.join(base_dir, "data", "products.json")
        self.products = self.load_products()

    def load_products(self):
        try:
            with open(self.products_file, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_products(self):
        with open(self.products_file, "w") as f:
            json.dump(self.products, f, indent=2)  

    def add_products(self):
        print("\n=== Add Product ===")
        name = input("Enter product name: ")
        price = float(input("Enter price: "))
        reorder_level = int(input("Enter reorder level: "))

    
        if self.products:
            new_id = max(p['id'] for p in self.products) + 1
        else:
            new_id = 1

        new_product = {
            "id": new_id,
            "name": name,
            "price": price,
            "reorder_level": reorder_level
        }

        self.products.append(new_product)
        self.save_products()
        print("Product added successfully.")

    def update_products(self):
        print("\n=== Update Product ===")
        self.view_products()

        pid = int(input("Enter product ID to update: "))
        product = next((p for p in self.products if p['id'] == pid), None)

        if not product:
            print("Product not found.")
            return

        name = input(f"Enter new name [{product['name']}]: ") or product['name']
        price = input(f"Enter new price [{product['price']}]: ") or product['price']
        reorder_level = input(f"Enter new reorder level [{product['reorder_level']}]: ") or product['reorder_level']

        product['name'] = name
        product['price'] = float(price)
        product['reorder_level'] = int(reorder_level)

        self.save_products()
        print("Product updated successfully.")

    def delete_products(self):
        print("\n=== Delete Product ===")
        self.view_products()

        pid = int(input("Enter product ID to delete: "))
        product = next((p for p in self.products if p['id'] == pid), None)

        if not product:
            print("Product not found.")
            return

        self.products.remove(product)
        self.save_products()
        print("Product deleted successfully.")

    def view_products(self):
        print("\n=== Product List ===")
        if not self.products:
            print("No products found.")
            return

        print(f"{'ID':<5} {'Name':<30} {'Price':<10} {'Reorder Level':<15}")
        for p in self.products:
            print(f"{p['id']:<5} {p['name']:<30} {p['price']:<10} {p['reorder_level']:<15}")
