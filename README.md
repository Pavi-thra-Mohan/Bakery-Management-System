# 🧁 Bakery Management System ("BAKE 'N TAKE")

An interactive, command-line interface (CLI) application built using **Python** and **MySQL** to streamline daily operations for small to medium-sized bakeries.

---
💡 Note on Authenticity: This project was designed, architected, and fully coded manually by me prior to the rise of AI coding assistants in 2022. Every SQL query, data structure, and logic flow was manually written to gain a solid, hands-on understanding of database connectivity and procedural Python programming. (Do appreciate that fact before we move on!)

## 📌 Features

* **🔐 Secure Authentication:** Protected access requiring an authorized username and password to log in.
* **📜 Interactive Menu Display:** Quick overview of all available bakery items with pricing.
* **➕ Add New Items:** Expand the menu by inserting new product details, initial stock, and pricing into the database.
* **🔍 Item Search:** Search for specific items using unique product IDs (`ItNo`).
* **🛒 Order Placement & Auto Billing:** Process multi-item customer orders, verify available stock, generate an itemized bill, and automatically update database stock.
* **✏️ Stock & Price Updation:** Easily adjust product inventory quantities or price tags.
* **📊 Full Inventory Tracking:** Display complete details of all items, stock levels, and categories stored in MySQL.

---

## 🖼️ Application Screenshots

### 1. Authentication & System Access
| Login Successful | Login Failed |
| :---: | :---: |
| ![Login Successful](screenshots/login_successful.PNG) | ![Login Failed](screenshots/login_failed.PNG) |

### 2. Adding Products & Inventory View
| Adding New Item | Added Item Displayed |
| :---: | :---: |
| ![Adding New Item](screenshots/adding_newitem.PNG) | ![Added Item Displayed](screenshots/added_newitem_displayed.PNG) |

### 3. Product Search & Displaying Records
| Search for an Item | Displaying All Records |
| :---: | :---: |
| ![Search Item](screenshots/search_for_an_item.PNG) | ![Display All Records](screenshots/displaying_all_records.PNG) |

### 4. Order Placement & Automated Receipt
| Order Placement (Part 1) | Order Placement (Part 2) |
| :---: | :---: |
| ![Order Placement 1](screenshots/order_placement1.PNG) | ![Order Placement 2](screenshots/order_placement2.PNG) |

| Generated Invoice |
| :---: |
| ![Bill Generated](screenshots/bill_generated.PNG) |

### 5. Inventory Updates & Exit
| Updating Quantity | Updated Quantity Displayed |
| :---: | :---: |
| ![Updating Quantity](screenshots/updating_quantity.PNG) | ![Updated Quantity Displayed](screenshots/updated_quantity_displayed.PNG) |

| Updating Price | Updated Price Displayed |
| :---: | :---: |
| ![Updating Price](screenshots/updating_price.PNG) | ![Updated Price Displayed](screenshots/updated_price_displayed.PNG) |

| System Exit |
| :---: |
| ![Exiting Program](screenshots/exiting_program.PNG) |

---

## 🛠️ System Requirements

### Hardware
* **Processor:** Intel Core i3 or equivalent
* **RAM:** 2 GB minimum

### Software
* **Operating System:** Windows 7 or higher / macOS / Linux.
* **Python:** 3.x installed
* **Database:** MySQL Server

---

## 🚀 Installation & Setup

### 1. Clone the Repository
```bash
git clone [https://github.com/your-username/bakery-management-system.git](https://github.com/your-username/bakery-management-system.git)
cd bakery-management-system
```

### 2. Install Required Python Packages
```bash
pip install mysql-connector-python
```

### 3. Database Setup
Ensure your MySQL server is running. Modify the database credentials in `src/main.py` if necessary:
```python
con = sql.connect(
    host="localhost",
    user="root",
    password="your_mysql_password"
)
```
*Note: The application automatically creates the database `BMS` and table `Products` upon the first run.*

### 4. Default Login Credentials
* **Username:** `Manager`
* **Password:** `sweets4life`

### 5. Run the Application
```bash
python src/main.py
```

---

## 🗄️ Database Schema

The system manages a table called `Products` within the `BMS` database:

| Field | Type | Constraint | Description |
| :--- | :--- | :--- | :--- |
| `ItNo` | `INT` | Unique Primary Key | Item Number |
| `Category` | `VARCHAR(25)` | - | Food Category (e.g., Cake, Puffs) |
| `Item` | `VARCHAR(25)` | - | Name of the Item |
| `Stock` | `INT` | - | Available Quantity|
| `Price` | `INT` | - | Unit Price in INR |

---
## 🗄️ Database Architecture

The application requires the `BMS` database and `Products` table. While the Python script automatically initializes this setup upon launch, you can also manually initialize the database schema using the provided SQL script:

* **SQL Script Location:** [`database/schema.sql`](database/schema.sql)

To import the schema directly into MySQL via command line:
```bash
mysql -u root -p < database/schema.sql

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).
