import json
from core.auth import UserAuth
from core.product import Product
from core.inventory import Inventory
from core.sales import Sales
from core.reports import Reports
from core.shops import ShopManager

def load_shops():
    with open("data/shops.json") as f:
        return json.load(f)

def product_options(user, product_manager):
    role = user['role']
    while True:
        print("\n=== Product Menu ===")
        if role == "admin":
            print("1. Add Product")
            print("2. Update Product")
            print("3. Delete Product")
            print("4. View Products")
            print("5. Back")
        else:
            print("1. View Products")
            print("2. Back")

        option = input("Choose option: ")

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
                break
            else:
                print("Invalid choice.")
        else:
            if option == "1":
                product_manager.view_products()
            elif option == "2":
                break
            else:
                print("Invalid choice.")

def inventory_options(user, inventory_manager, products, selected_shop_id, shops_dict):
    role = user['role']
    shop_name = shops_dict[selected_shop_id]

    while True:
        print(f"\n=== Inventory Menu for {shop_name} ===")
        if role == "admin":
            print("1. Add Stock")
            print("2. Remove Stock")
            print("3. View Stock")
            print("4. Low Stock Report")
            print("5. Back")
        else:
            print("1. View Stock")
            print("2. Back")

        option = input("Choose option: ")

        if role == "admin":
            if option == "1":
                inventory_manager.add_stock(selected_shop_id, products)
            elif option == "2":
                inventory_manager.remove_stock(selected_shop_id, products)
            elif option == "3":
                inventory_manager.view_stock(selected_shop_id, products)
            elif option == "4":
                inventory_manager.low_stock_report(selected_shop_id, products)
            elif option == "5":
                break
            else:
                print("Invalid choice.")
        else:
            if option == "1":
                inventory_manager.view_stock(selected_shop_id, products)
            elif option == "2":
                break
            else:
                print("Invalid choice.")

def sales_options(user, sales_manager, selected_shop_id, products, shops_dict):
    shop_name = shops_dict[selected_shop_id]
    while True:
        print(f"\n=== Sales Menu for {shop_name} ===")
        print("1. Record Sale")
        print("2. Back")
        option = input("Choose option: ")
        if option == "1":
            sales_manager.record_sale(selected_shop_id, products, user)
        elif option == "2":
            break
        else:
            print("Invalid choice.")

def report_options(user, reports_manager, selected_shop_id, shops_dict):
    role = user['role']
    shop_name = shops_dict[selected_shop_id]

    while True:
        print(f"\n=== Reports Menu for {shop_name} ===")
        print("1. Sales Report for Shop")
        print("2. Sales Report for User")
        print("3. Sales by Date Range")
        if role == "admin":
            print("4. Global Sales Comparison")
            print("5. Stock Report for Shop")
            print("6. Back")
        else:
            print("4. Stock Report for Shop")
            print("5. Back")

        option = input("Choose option: ")

        if option == "1":
            reports_manager.sales_by_shop(selected_shop_id)
        elif option == "2":
            reports_manager.sales_by_user(user['username'])
        elif option == "3":
            start = input("Start date (YYYY-MM-DD): ")
            end = input("End date (YYYY-MM-DD): ")
            reports_manager.sales_by_date_range(start, end)
        elif option == "4" and role == "admin":
            reports_manager.global_sales_comparison()
        elif (option == "5" and role == "admin") or (option == "4" and role != "admin"):
            reports_manager.stock_report(selected_shop_id)
        elif (option == "6" and role == "admin") or (option == "5" and role != "admin"):
            break
        else:
            print("Invalid choice.")

def main():
    auth = UserAuth()
    product_manager = Product()
    inventory_manager = Inventory()
    sales_manager = Sales()
    reports_manager = Reports()
    shop_manager = ShopManager()
    products = product_manager.load_products()

    print("Welcome to the Inventory")
    print("1. Login\n2. Register New Staff")
    signup_in = input("Enter your choice: ")

    if signup_in == "1":
        user = auth.login_user()
        if not user:
            print("Login failed. Exiting.")
            return
    elif signup_in == "2":
        auth.register()
        return
    else:
        print("Invalid choice.")
        return

    print("\nYour available shops:")
    shop_manager.view_shops()
    print("Your assigned shops:", user['shops'])

    # If user has multiple shops, ask
    if len(user['shops']) > 1:
        shop_choice = input("Enter the shop ID you want to manage: ")
        if shop_choice not in user['shops']:
            print("Invalid shop ID.")
            return
        selected_shop_id = shop_choice
    else:
        selected_shop_id = user['shops'][0]

    shops_dict = shop_manager.shops

    while True:
        print("\nWhat would you like to do now?")
        print("1. Manage Products")
        print("2. Manage Inventory")
        print("3. Record Sales")
        print("4. Check Reports")
        print("5. Logout")

        work_choice = input("Enter your choice: ")

        if work_choice == "1":
            product_options(user, product_manager)
        elif work_choice == "2":
            inventory_options(user, inventory_manager, products, selected_shop_id, shops_dict)
        elif work_choice == "3":
            sales_options(user, sales_manager, selected_shop_id, products, shops_dict)
        elif work_choice == "4":
            report_options(user, reports_manager, selected_shop_id, shops_dict)
        elif work_choice == "5":
            print(f"Goodbye, {user['username']}")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()