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
        return []
      
  def save_products(self):
     with open(self.stock_file,"w") as f:
       json.dump(self.stock_file,f,indent=2)    
       
   