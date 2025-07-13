import os, json , bcrypt, pwinput

class UserAuth:
  def __init__(self):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    self.users_file = os.path.join(base_dir, "data", "users.json")
    self.users = self.load_users()
 
  def load_users(self):
      if os.path.exists(self.users_file):
          with open(self.users_file, "r") as f:
              return json.load(f)
      else:
          return []


  def save_users(self):
     with open(self.users_file, "w") as f:
          json.dump(self.users,f,indent=2) 


  def register(self):
     username=input("Enter Your username: ") 
     password = pwinput.pwinput(prompt='Enter Your Password: ',mask="*").encode('utf-8')         

     for users in self.users:
           if users["username"] == username:
              print("Username Already Exists")
              return
     role = input("Enter the Role(admin/staff): ").lower()
     shops = [shop.strip() for shop in input("Enter Shops ID(comma-separated): ").split(",")]
            

     #Hash_password:
     hashed = bcrypt.hashpw(password, bcrypt.gensalt()).decode('utf-8')

     #save_users
     self.users.append({'username':username,'password':hashed
                        , "role":role, "shops":shops})
     self.save_users()
     print("Registration Successful ")
     print(f"Welcome Onboard, {username}")
     return users
  def login_user(self):
      username=input("Enter Your username: ") 
      password = pwinput.pwinput(prompt='Enter Your Password: ',mask="*").encode('utf-8')
      for user in self.users:
         if user["username"] == username:
            stored_hash = user['password'].encode('utf-8')
            if bcrypt.checkpw(password,stored_hash):
               print(f"Welcome, {username} ")
               return user
            else:
               print("Invalid Password")
               return False   
      
      print("Username not Found")
      return False      
   
   
      