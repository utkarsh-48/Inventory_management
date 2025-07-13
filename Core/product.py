import json , os
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
     with open(self.products_file,"w") as f:
       json.dump(self.products_file,f,indent=2)
       
   def add_products(self):
     print("add")
      
   def update_products(self):
      print("update")
   def delete_products(self):
    print("delete")
    
   def view_products(self):
     print("view")   