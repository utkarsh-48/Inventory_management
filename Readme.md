# Multi-Shop Inventory Management System

A Python-based inventory management CLI tool for managing multiple shops or branches, with shared product data, per-shop stock tracking, role-based user access, and secure data storage. Designed for educational use and as a foundation for real-world extensions.

---

## Features

### User Authentication

* Register and log in securely with hashed passwords using `bcrypt`.
* Role-based access control (admin or staff).
* All user accounts stored in a single `users.json` file, with support for multiple shops per user.

### Multi-Shop Support

* Central product catalog (`products.json`).
* Stock tracked separately for each shop (`stock.json`).
* Shop selection is only required if a user has more than one shop assigned.

### Inventory Management

* Add, update, delete, and view products.
* Manage stock levels independently for each shop.
* Reorder levels and low stock reports help ensure proper stock levels.

### Sales Tracking

* Record sales transactions per shop.
* Automatically adjusts stock on each sale.
* Sales history saved to `sales.json`.

### Reporting

* Generate per-shop or global sales and inventory reports.
* Compare sales across shops.
* Low stock and reorder alerts.

---

## Project Structure

```
inventory_management_system/
│
├── main.py                # Entry point for the CLI
│
├── core/                  # Core modules
│   ├── __init__.py
│   ├── auth.py
│   ├── product.py
│   ├── inventory.py
│   ├── sales.py
│   ├── reports.py
│   ├── shops.py
│
├── data/                  # Persistent data files
│   ├── products.json
│   ├── users.json
│   ├── stock.json
│   ├── sales.json
│   ├── shops.json
│
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
```

---

## How It Works

1. Run `main.py`.
2. Register or log in as a user.
3. If assigned to multiple shops, select which shop to manage.
4. Manage the inventory: add, update, delete products, adjust stock levels.
5. Record product sales, which automatically adjust shop stock.
6. Generate reports for a single shop or compare multiple shops.

---

## Setup Instructions

**Clone the repository**

```bash
git clone <your-repo-url>
cd inventory_management_system
```

**(Optional) Create a virtual environment**

```bash
python -m venv venv
# Activate (Windows)
venv\Scripts\activate
# Or activate (macOS/Linux)
source venv/bin/activate
```

**Install dependencies**

```bash
pip install -r requirements.txt
```

**Run the system**

```bash
python main.py
```

---

## Dependencies

* `bcrypt` for password hashing.
* `pwinput` for masked password input in the terminal.
* `tabulate` (optional) for formatted CLI tables.

---

## Planned Improvements

* Better backup and restore options for JSON files.
* Switch to a database backend (e.g., SQLite) for improved data integrity.
* Web or GUI front-end for broader usability.
* Improved logging and audit trails.

---

## License

This project is open for educational use. Feel free to adapt, modify, or extend it. Consider adding an appropriate open-source license for any public or production use.

---

## Author

Developed by Utkarsh for hands-on practice with Python file handling, simple authentication, and modular CLI app design.

---

**For questions or contributions, open an issue or submit a pull request.**

---
