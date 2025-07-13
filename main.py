from core.auth import UserAuth
from core.product import Product

def product_options(user, product_manager):
    role = user['role']
    while True:
        print("=== Main Menu ===")
        if role == "admin":
            print("1. Add Product")
            print("2. Update Product")
            print("3. Delete Product")
            print("4. View Products")
            print("5. Logout")
        else:  # staff
            print("1. View Products")
            print("2. Logout")

        option = input("Choose an option: ")

        if role == "admin":
            if option == "1":
                product_manager.add_products()
            elif option == "2":
                product_manager.update_products()
            elif option == "3":
                product_manager.delete_products()
            elif option == "4":
                product_manager.view_products()
            elif option == "5":
                print(f"Goodbye, {user['username']}")
                break
            else:
                print("Invalid choice. Try again.")
        else:  # staff
            if option == "1":
                product_manager.view_products()
            elif option == "2":
                print(f"Goodbye,{user['username']}")
                break
            else:
                print("Invalid choice. Try again.")

def inventory_options(user,  ):
    print("hello")
def report_options(user,):
     print("hello")
def sales_options(user,):
     print("hello")     
def main():
    auth = UserAuth()
    product_manager = Product()

    print("Welcome to the Inventory")
    print("1.Login 2. Register New staff")
    signup_in = input("Enter your choice: ")

    if signup_in == "1":
        user = auth.login_user()
        if not user:
            print("Login Failed> Exiting...")
            return
    elif signup_in == "2":
        auth.register()
        return
    else:
        print("Invalid choice.")
        return

    # Shop selection:
    shops = user["shops"]
    if len(shops) > 1:
        print("You have access to multiple shops")
        for i, shop in enumerate(shops, start=1):
            print(f"{i}. {shop.strip()}")
        shop_choice = int(input("Select the shop You want to manage: "))
        selected_shop = shops[shop_choice - 1].strip()
    else:
        selected_shop = shops[0].strip()

    print(f"You are Managing: {selected_shop}")

    print("What would You like to do Now: ")
    print("1.Manage Products\n"
          "2.Manage Inventory\n"
          "3.Record Sales\n"
          "4.Check Reports\n"
          "5.Logout")
    work_choice = input("Enter your Choice: ")
    if work_choice == "1":
        product_options(user, product_manager)
    elif work_choice == "2":
        inventory_options(user)
    elif work_choice == "3":
        sales_options(user)
    elif work_choice == "4":
        report_options(user)
    elif work_choice == "5":
        print(f"Goodbye, {user['username']}")
        return
    else:
        print("Invalid choice. Try again.")
        return
    

if __name__ == "__main__":
    main()