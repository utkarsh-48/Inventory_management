# Multi-Shop Inventory Management System

A Python-based Inventory Management System for managing multiple shops or branches with:
- A shared product catalog
- Per-shop stock tracking
- User authentication with roles (admin or staff)
- Secure password storage
- Global and per-shop reports

---

## Features

**User Authentication**
- Register and login with hashed passwords (bcrypt)
- Role-based access: admin or staff
- Single `users.json` for all users, with assigned shops

**Multi-Shop Support**
- Central product catalog (`products.json`)
- Stock tracked per shop (`stock.json`)
- Shop selection prompt only if user has more than one shop assigned

**Inventory Management**
- Add, update, delete, and view products
- Shared product list, stock adjusted per shop
- Reorder levels and low stock alerts

**Sales Tracking**
- Record sales transactions per shop
- Sales history saved in `sales.json`

**Reporting**
- Generate per-shop or global inventory and sales reports
- Optional export to CSV

---

## Project Structure

```

inventory\_management\_system/
│
├── main.py                # Entry point
│
├── core/                  # Core logic modules
│   ├── **init**.py
│   ├── user\_auth.py
│   ├── product.py
│   ├── inventory.py
│   ├── shop.py
│   ├── reports.py
│
├── data/                  # Persistent data files
│   ├── products.json
│   ├── users.json
│   ├── stock.json
│   ├── sales.json
│
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation

```

## How It Works

1. Run `main.py`
2. Register or login as a user
3. If the user is assigned to multiple shops, select a shop to work in
4. Manage inventory: add, update, delete products, adjust stock for the selected shop
5. Record product sales
6. Generate per-shop or global reports

---

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone <your-repo-url>
   cd inventory_management_system
``

2. (Optional) Create a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate     # Windows
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the system:

   ```bash
   python main.py
   ```

---

## Dependencies

* `bcrypt` for secure password hashing
* `tabulate` for formatted CLI tables
* `pwinput` for masked password input in the terminal

---

## Planned Improvements

* Improved password hashing and salting
* Backup and restore for JSON data
* Option to switch to SQLite or another database in the future
* Optional web interface

---

## Author

Developed by Utkarsh for educational purposes and practice with Python, file handling, and simple CLI application design.

---

## License

Free to use, modify, and extend. Add an appropriate open-source license if needed.

