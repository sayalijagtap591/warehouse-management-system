📦 Warehouse Management System

A full-stack Warehouse Management System developed using Python Flask and MySQL to manage warehouses, locations, products, inventory, stock movements, orders, shipments, receivings, reports, and dashboard operations.

---

📌 Project Overview

The Warehouse Management System provides a centralized platform for managing warehouse operations efficiently.

The system helps users:

- Manage warehouses
- Manage warehouse locations
- Add and manage products
- Track inventory and stock
- Record stock movements
- Manage customer orders
- Track shipments
- Manage receiving operations
- Generate operational reports
- Monitor warehouse activities through a dashboard

---

✨ Key Features

🏢 Warehouse Management

- Add warehouses
- View warehouse details
- Manage warehouse information
- Store city, state, and address information

📍 Location Management

- Add warehouse locations
- Assign locations to warehouses
- Manage location codes
- Store location descriptions

📦 Product Management

- Add products
- Update products
- Delete products
- Search and view products
- Manage SKU, category, price, and quantity

📊 Inventory Management

- View current stock
- Update product quantity
- Track inventory levels
- Monitor available stock

🔄 Stock Movement

- Record stock IN
- Record stock OUT
- Automatically update product quantity
- Prevent stock from becoming negative
- Maintain stock movement history

🛒 Order Management

- Create orders
- Update order status
- View customer orders
- Manage order information

🚚 Shipment Management

- Create shipments
- Store tracking numbers
- Update shipment status
- Track shipment information

📥 Receiving Management

- Record received products
- Store received quantities
- Track receiving date and time

📈 Reports

The system provides reports for:

- Stock
- Orders
- Shipments
- Summary

🖥️ Dashboard

The dashboard provides a centralized view of warehouse operations and important system information.

---

🛠️ Technology Stack

Technology| Purpose
Python| Backend Programming
Flask| Web Framework
Flask-SQLAlchemy| Database ORM
MySQL| Database
HTML5| Frontend
CSS3| Styling
JavaScript| Frontend Logic
REST API| Backend Communication
Git| Version Control
GitHub| Source Code Management

---

🏗️ Project Architecture

Frontend
   │
   │ HTTP Requests
   ▼
Flask Backend
   │
   ├── Routes / REST APIs
   │
   ├── Business Logic
   │
   └── SQLAlchemy ORM
           │
           ▼
        MySQL

---

📂 Project Structure

warehouse_system/
│
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── models.py
│   └── routes.py
│
├── templates/
│   ├── dashboard.html
│   ├── products.html
│   ├── inventory.html
│   ├── warehouses.html
│   ├── locations.html
│   ├── orders.html
│   ├── shipments.html
│   ├── receivings.html
│   └── reports.html
│
├── screenshots/
│   ├── dashboard.png
│   ├── products.png
│   ├── inventory.png
│   ├── warehouses.png
│   ├── locations.png
│   ├── orders.png
│   ├── shipments.png
│   ├── receivings.png
│   └── reports.png
│
├── requirements.txt
├── README.md
└── run.py

---

⚙️ Installation

1. Clone the Repository

git clone https://github.com/sayalijagtap591/warehouse-management-system.git

2. Open the Project

cd warehouse-management-system

3. Create Virtual Environment

python -m venv venv

4. Activate Virtual Environment

Windows PowerShell:

.\venv\Scripts\Activate.ps1

5. Install Dependencies

pip install -r requirements.txt

---

🗄️ Database Configuration

Create a MySQL database and configure the database connection in:

app/config.py

Example:

SQLALCHEMY_DATABASE_URI = "mysql+pymysql://username:password@localhost/warehouse_db"

Replace:

- "username" with your MySQL username
- "password" with your MySQL password
- "warehouse_db" with your databas
