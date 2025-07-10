import os , json , bcrypt, pwinput

class User_auth:
  def __init__(self):
    self.users_file = "users.json"
    self.users = self.load_users()

  def load_users(self):
      try:
         with open(self.users_file,"r") as f:
            return json.load(f)
      except FileNotFoundError:
         return []


  def save_users(self):
     with open(self.users_file, "w") as f:
          json.dump(self.users,f,indent=2) 


  def register(self):
     username=input("Enter Your username: ") 
     password = pwinput.pwinput(prompt='Enter Your Password: ',mask="🤫").encode('utf-8')         

     for users in self.users:
           if users["username"] == username:
              print("Username Already Exists")
              return

     #Hash_password:
     hashed = bcrypt.hashpw(password, bcrypt.gensalt()).decode('utf-8')

     #save_users
     self.users.append({'username':username,'password':hashed})
     self.save_users()
     print("Registration Successful ")
     print(f"Welcome Onboard, {username}")

  def login_user(self):
      username=input("Enter Your username: ") 
      password = pwinput.pwinput(prompt='Enter Your Password: ',mask="*").encode('utf-8')
      for users in self.users:
       try:
         if users["username"] == username:
            stored_hash = users['password'].encode('utf-8')
            if bcrypt.checkpw(password,stored_hash):
               print(f"Welcome, {username} ")
               return True
            else:
               print("Invalid Password")
               return False
       except ValueError:
          print("Enter a Valid Number")     
      
      print("Username not Found")
      return False      
   
   
      