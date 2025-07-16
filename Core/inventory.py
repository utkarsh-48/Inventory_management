import os , json

class Inventory:
  def __init__(self):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    self.stock_file = os.path.join(base_dir, "data", "stock.json")
    self.stock = self.load_stock()
    
    
  def load_stock(self):
    try:
        with open(self.stock_file, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
      
  def save_stock(self):
     with open(self.stock_file,"w") as f:
       json.dump(self.stock,f,indent=2)    
       
  def add_stock(self, shop, products):
        print("\n=== Add Stock ===")
        self.view_stock(shop, products)

        product_id = input("Enter Product ID to add stock: ").strip()
        if product_id not in [str(p['id']) for p in products]:
            print("Invalid Product ID.")
            return

        qty = int(input("Enter quantity to add: "))

        # Ensure shop exists in stock dict
        if shop not in self.stock:
            self.stock[shop] = {}

        # Add or update stock
        self.stock[shop][product_id] = self.stock[shop].get(product_id, 0) + qty

        self.save_stock()
        print("Stock updated successfully.")

  def remove_stock(self, shop, products):
        print("\n=== Remove Stock ===")
        self.view_stock(shop, products)

        product_id = input("Enter Product ID to remove stock: ").strip()
        if product_id not in [str(p['id']) for p in products]:
            print("Invalid Product ID.")
            return

        current_qty = self.stock.get(shop, {}).get(product_id, 0)
        print(f"Current stock: {current_qty}")
        qty = int(input("Enter quantity to remove: "))

        if qty > current_qty:
            print("Cannot remove more than current stock.")
            return

        self.stock[shop][product_id] = current_qty - qty

        self.save_stock()
        print("Stock updated successfully.")

  def view_stock(self, shop, products):
        print(f"\n=== Stock for {shop} ===")
        print(f"{'ID':<5} {'Name':<30} {'Qty':<10} {'Reorder Level':<15}")

        for product in products:
            pid = str(product['id'])
            qty = self.stock.get(shop, {}).get(pid, 0)
            reorder_level = product.get('reorder_level', 0)
            print(f"{pid:<5} {product['name']:<30} {qty:<10} {reorder_level:<15}")

  def low_stock_report(self, shop, products):
        print(f"\n=== Low Stock Report for {shop} ===")
        low_stock_found = False

        for product in products:
            pid = str(product['id'])
            qty = self.stock.get(shop, {}).get(pid, 0)
            reorder_level = product.get('reorder_level', 0)

            if qty <= reorder_level:
                print(f"{pid}: {product['name']} | Qty: {qty} | Reorder Level: {reorder_level}")
                low_stock_found = True

        if not low_stock_found:
            print("No low stock items.")