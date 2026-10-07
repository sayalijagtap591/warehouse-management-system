from flask import Blueprint, request, jsonify, render_template
from app import db, bcrypt
from app.models import (
    User,
    Warehouse,
    Location,
    Product,
    StockMovement,
    Order,
    Shipment,
    Receiving
)

routes = Blueprint("routes", __name__)


# =========================================================
# PAGE ROUTES
# =========================================================

@routes.route("/", methods=["GET"])
def dashboard_page():
    return render_template("dashboard.html")


@routes.route("/login", methods=["GET"])
def login_page():
    return render_template("login.html")


@routes.route("/products-page", methods=["GET"])
def products_page():
    return render_template("products.html")


@routes.route("/inventory", methods=["GET"])
def inventory_page():
    return render_template("inventory.html")


@routes.route("/warehouses-page", methods=["GET"])
def warehouses_page():
    return render_template("warehouses.html")


@routes.route("/locations-page", methods=["GET"])
def locations_page():
    return render_template("locations.html")


@routes.route("/orders-page", methods=["GET"])
def orders_page():
    return render_template("orders.html")


@routes.route("/shipments-page", methods=["GET"])
def shipments_page():
    return render_template("shipments.html")


@routes.route("/receivings-page", methods=["GET"])
def receivings_page():
    return render_template("receives.html")


@routes.route("/reports-page", methods=["GET"])
def reports_page():
    return render_template("reports.html")


# =========================================================
# LOGIN API
# =========================================================

@routes.route("/login", methods=["POST"])
def login():
    data = request.get_json() or {}

    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({
            "message": "Username and password are required"
        }), 400

    user = User.query.filter_by(username=username).first()

    if not user:
        return jsonify({
            "message": "Invalid username or password"
        }), 401

    try:
        password_valid = bcrypt.check_password_hash(
            user.password,
            password
        )
    except Exception as e:
        return jsonify({
            "message": "Password verification failed",
            "error": str(e)
        }), 500

    if not password_valid:
        return jsonify({
            "message": "Invalid username or password"
        }), 401

    return jsonify({
        "message": "Login successful",
        "user": {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "role": user.role
        }
    }), 200


# =========================================================
# WAREHOUSE API
# =========================================================

@routes.route("/warehouses", methods=["GET"])
def get_warehouses():

    warehouses = Warehouse.query.all()

    result = []

    for warehouse in warehouses:
        result.append({
            "id": warehouse.id,
            "name": warehouse.name,
            "address": warehouse.address,
            "city": warehouse.city,
            "state": warehouse.state
        })

    return jsonify(result), 200


@routes.route("/warehouses", methods=["POST"])
def add_warehouse():

    data = request.get_json() or {}

    name = data.get("name")

    if not name:
        return jsonify({
            "message": "Warehouse name is required"
        }), 400

    warehouse = Warehouse(
        name=name,
        address=data.get("address"),
        city=data.get("city"),
        state=data.get("state")
    )

    db.session.add(warehouse)
    db.session.commit()

    return jsonify({
        "message": "Warehouse added successfully",
        "warehouse": {
            "id": warehouse.id,
            "name": warehouse.name,
            "address": warehouse.address,
            "city": warehouse.city,
            "state": warehouse.state
        }
    }), 201


@routes.route("/warehouses/<int:id>", methods=["PUT"])
def update_warehouse(id):

    warehouse = Warehouse.query.get(id)

    if not warehouse:
        return jsonify({
            "message": "Warehouse not found"
        }), 404

    data = request.get_json() or {}

    warehouse.name = data.get("name", warehouse.name)
    warehouse.address = data.get("address", warehouse.address)
    warehouse.city = data.get("city", warehouse.city)
    warehouse.state = data.get("state", warehouse.state)

    db.session.commit()

    return jsonify({
        "message": "Warehouse updated successfully"
    }), 200


@routes.route("/warehouses/<int:id>", methods=["DELETE"])
def delete_warehouse(id):

    warehouse = Warehouse.query.get(id)

    if not warehouse:
        return jsonify({
            "message": "Warehouse not found"
        }), 404

    db.session.delete(warehouse)
    db.session.commit()

    return jsonify({
        "message": "Warehouse deleted successfully"
    }), 200


# =========================================================
# LOCATION API
# =========================================================

@routes.route("/locations", methods=["GET"])
def get_locations():

    locations = Location.query.all()

    result = []

    for location in locations:
        result.append({
            "id": location.id,
            "warehouse_id": location.warehouse_id,
            "location_code": location.location_code,
            "description": location.description
        })

    return jsonify(result), 200


@routes.route("/locations", methods=["POST"])
def add_location():

    data = request.get_json() or {}

    warehouse_id = data.get("warehouse_id")
    location_code = data.get("location_code")

    if not warehouse_id or not location_code:
        return jsonify({
            "message": "Warehouse ID and location code are required"
        }), 400

    warehouse = Warehouse.query.get(warehouse_id)

    if not warehouse:
        return jsonify({
            "message": "Warehouse not found"
        }), 404

    location = Location(
        warehouse_id=warehouse_id,
        location_code=location_code,
        description=data.get("description")
    )

    db.session.add(location)
    db.session.commit()

    return jsonify({
        "message": "Location added successfully",
        "location": {
            "id": location.id,
            "warehouse_id": location.warehouse_id,
            "location_code": location.location_code,
            "description": location.description
        }
    }), 201


@routes.route("/locations/<int:id>", methods=["PUT"])
def update_location(id):

    location = Location.query.get(id)

    if not location:
        return jsonify({
            "message": "Location not found"
        }), 404

    data = request.get_json() or {}

    location.warehouse_id = data.get(
        "warehouse_id",
        location.warehouse_id
    )

    location.location_code = data.get(
        "location_code",
        location.location_code
    )

    location.description = data.get(
        "description",
        location.description
    )

    db.session.commit()

    return jsonify({
        "message": "Location updated successfully"
    }), 200


@routes.route("/locations/<int:id>", methods=["DELETE"])
def delete_location(id):

    location = Location.query.get(id)

    if not location:
        return jsonify({
            "message": "Location not found"
        }), 404

    db.session.delete(location)
    db.session.commit()

    return jsonify({
        "message": "Location deleted successfully"
    }), 200
# =========================================================
# PRODUCT API
# =========================================================

@routes.route("/products", methods=["GET"])
def get_products():

    products = Product.query.all()

    result = []

    for product in products:
        result.append({
            "id": product.id,
            "sku": product.sku,
            "name": product.name,
            "category": product.category,
            "price": product.price,
            "quantity": product.quantity
        })

    return jsonify(result), 200


@routes.route("/products", methods=["POST"])
def add_product():

    data = request.get_json() or {}

    sku = data.get("sku")
    name = data.get("name")

    if not sku or not name:
        return jsonify({
            "message": "SKU and product name are required"
        }), 400

    existing_product = Product.query.filter_by(
        sku=sku
    ).first()

    if existing_product:
        return jsonify({
            "message": "SKU already exists"
        }), 409

    product = Product(
        sku=sku,
        name=name,
        category=data.get("category"),
        price=data.get("price", 0),
        quantity=data.get("quantity", 0)
    )

    db.session.add(product)
    db.session.commit()

    return jsonify({
        "message": "Product added successfully",
        "product": {
            "id": product.id,
            "sku": product.sku,
            "name": product.name,
            "category": product.category,
            "price": product.price,
            "quantity": product.quantity
        }
    }), 201


@routes.route("/products/<int:id>", methods=["PUT"])
def update_product(id):

    product = Product.query.get(id)

    if not product:
        return jsonify({
            "message": "Product not found"
        }), 404

    data = request.get_json() or {}

    new_sku = data.get("sku", product.sku)

    duplicate = Product.query.filter(
        Product.sku == new_sku,
        Product.id != id
    ).first()

    if duplicate:
        return jsonify({
            "message": "SKU already exists"
        }), 409

    product.sku = new_sku
    product.name = data.get("name", product.name)
    product.category = data.get(
        "category",
        product.category
    )
    product.price = data.get(
        "price",
        product.price
    )
    product.quantity = data.get(
        "quantity",
        product.quantity
    )

    db.session.commit()

    return jsonify({
        "message": "Product updated successfully"
    }), 200


@routes.route("/products/<int:id>", methods=["DELETE"])
def delete_product(id):

    product = Product.query.get(id)

    if not product:
        return jsonify({
            "message": "Product not found"
        }), 404

    db.session.delete(product)
    db.session.commit()

    return jsonify({
        "message": "Product deleted successfully"
    }), 200


# =========================================================
# STOCK API
# =========================================================

@routes.route("/stock", methods=["GET"])
def get_stock():

    products = Product.query.all()

    result = []

    for product in products:
        result.append({
            "id": product.id,
            "sku": product.sku,
            "name": product.name,
            "category": product.category,
            "quantity": product.quantity,
            "price": product.price
        })

    return jsonify(result), 200


@routes.route("/stock/<int:product_id>", methods=["PUT"])
def update_stock(product_id):

    product = Product.query.get(product_id)

    if not product:
        return jsonify({
            "message": "Product not found"
        }), 404

    data = request.get_json() or {}

    quantity = data.get("quantity")

    if quantity is None:
        return jsonify({
            "message": "Quantity is required"
        }), 400

    product.quantity = quantity

    db.session.commit()

    return jsonify({
        "message": "Stock updated successfully",
        "quantity": product.quantity
    }), 200


# =========================================================
# STOCK MOVEMENT API
# =========================================================

@routes.route("/stock-movements", methods=["GET"])
def get_stock_movements():

    movements = StockMovement.query.order_by(
        StockMovement.id.desc()
    ).all()

    result = []

    for movement in movements:
        result.append({
            "id": movement.id,
            "product_id": movement.product_id,
            "type": movement.movement_type,
            "quantity": movement.quantity,
            "created_at": str(movement.created_at)
        })

    return jsonify(result), 200


@routes.route("/stock-movements", methods=["POST"])
def add_stock_movement():

    data = request.get_json() or {}

    product_id = data.get("product_id")
    movement_type = data.get("movement_type")
    quantity = data.get("quantity")

    if not product_id or not movement_type or quantity is None:
        return jsonify({
            "message": "Product, movement_type and quantity are required"
        }), 400

    product = Product.query.get(product_id)

    if not product:
        return jsonify({
            "message": "Product not found"
        }), 404

    movement_type = movement_type.upper()

    if movement_type not in ["IN", "OUT"]:
        return jsonify({
            "message": "movement_type must be IN or OUT"
        }), 400

    if quantity <= 0:
        return jsonify({
            "message": "Quantity must be greater than 0"
        }), 400

    if movement_type == "IN":

        product.quantity += quantity

    elif movement_type == "OUT":

        if product.quantity < quantity:
            return jsonify({
                "message": "Insufficient stock"
            }), 400

        product.quantity -= quantity

    movement = StockMovement(
        product_id=product_id,
        movement_type=movement_type,
        quantity=quantity
    )

    db.session.add(movement)
    db.session.commit()

    return jsonify({
        "message": "Stock movement added successfully",
        "new_quantity": product.quantity
    }), 201


# =========================================================
# ORDER API
# =========================================================

@routes.route("/orders", methods=["GET"])
def get_orders():

    orders = Order.query.order_by(
        Order.id.desc()
    ).all()

    result = []

    for order in orders:
        result.append({
            "id": order.id,
            "order_number": order.order_number,
            "customer_name": order.customer_name,
            "status": order.status,
            "created_at": str(order.created_at)
        })

    return jsonify(result), 200


@routes.route("/orders", methods=["POST"])
def add_order():

    data = request.get_json() or {}

    order_number = data.get("order_number")
    customer_name = data.get("customer_name")

    if not order_number or not customer_name:
        return jsonify({
            "message": "Order number and customer name are required"
        }), 400

    existing_order = Order.query.filter_by(
        order_number=order_number
    ).first()

    if existing_order:
        return jsonify({
            "message": "Order number already exists"
        }), 409

    order = Order(
        order_number=order_number,
        customer_name=customer_name,
        status=data.get("status", "Pending")
    )

    db.session.add(order)
    db.session.commit()

    return jsonify({
        "message": "Order created successfully",
        "order": {
            "id": order.id,
            "order_number": order.order_number,
            "customer_name": order.customer_name,
            "status": order.status,
            "created_at": str(order.created_at)
        }
    }), 201


@routes.route("/orders/<int:id>", methods=["PUT"])
def update_order(id):

    order = Order.query.get(id)

    if not order:
        return jsonify({
            "message": "Order not found"
        }), 404

    data = request.get_json() or {}

    new_order_number = data.get(
        "order_number",
        order.order_number
    )

    duplicate = Order.query.filter(
        Order.order_number == new_order_number,
        Order.id != id
    ).first()

    if duplicate:
        return jsonify({
            "message": "Order number already exists"
        }), 409

    order.order_number = new_order_number

    order.customer_name = data.get(
        "customer_name",
        order.customer_name
    )

    order.status = data.get(
        "status",
        order.status
    )

    db.session.commit()

    return jsonify({
        "message": "Order updated successfully"
    }), 200


@routes.route("/orders/<int:id>", methods=["DELETE"])
def delete_order(id):

    order = Order.query.get(id)

    if not order:
        return jsonify({
            "message": "Order not found"
        }), 404

    db.session.delete(order)
    db.session.commit()

    return jsonify({
        "message": "Order deleted successfully"
    }), 200
# =========================================================
# SHIPMENT API
# =========================================================

@routes.route("/shipments", methods=["GET"])
def get_shipments():

    shipments = Shipment.query.order_by(
        Shipment.id.desc()
    ).all()

    result = []

    for shipment in shipments:
        result.append({
            "id": shipment.id,
            "order_id": shipment.order_id,
            "tracking_number": shipment.tracking_number,
            "status": shipment.status,
            "shipped_at": str(shipment.shipped_at)
            if shipment.shipped_at else None
        })

    return jsonify(result), 200


@routes.route("/shipments", methods=["POST"])
def add_shipment():

    data = request.get_json() or {}

    order_id = data.get("order_id")
    tracking_number = data.get("tracking_number")

    if not order_id:
        return jsonify({
            "message": "Order ID is required"
        }), 400

    order = Order.query.get(order_id)

    if not order:
        return jsonify({
            "message": "Order not found"
        }), 404

    shipment = Shipment(
        order_id=order_id,
        tracking_number=tracking_number,
        status=data.get("status", "Pending")
    )

    db.session.add(shipment)
    db.session.commit()

    return jsonify({
        "message": "Shipment created successfully",
        "shipment": {
            "id": shipment.id,
            "order_id": shipment.order_id,
            "tracking_number": shipment.tracking_number,
            "status": shipment.status,
            "shipped_at": str(shipment.shipped_at)
            if shipment.shipped_at else None
        }
    }), 201


@routes.route("/shipments/<int:id>", methods=["PUT"])
def update_shipment(id):

    shipment = Shipment.query.get(id)

    if not shipment:
        return jsonify({
            "message": "Shipment not found"
        }), 404

    data = request.get_json() or {}

    if "order_id" in data:

        order = Order.query.get(data["order_id"])

        if not order:
            return jsonify({
                "message": "Order not found"
            }), 404

        shipment.order_id = data["order_id"]

    shipment.tracking_number = data.get(
        "tracking_number",
        shipment.tracking_number
    )

    shipment.status = data.get(
        "status",
        shipment.status
    )

    db.session.commit()

    return jsonify({
        "message": "Shipment updated successfully"
    }), 200


@routes.route("/shipments/<int:id>", methods=["DELETE"])
def delete_shipment(id):

    shipment = Shipment.query.get(id)

    if not shipment:
        return jsonify({
            "message": "Shipment not found"
        }), 404

    db.session.delete(shipment)
    db.session.commit()

    return jsonify({
        "message": "Shipment deleted successfully"
    }), 200


# =========================================================
# RECEIVING API
# =========================================================

@routes.route("/receivings", methods=["GET"])
def get_receivings():

    receivings = Receiving.query.order_by(
        Receiving.id.desc()
    ).all()

    result = []

    for receiving in receivings:
        result.append({
            "id": receiving.id,
            "product_id": receiving.product_id,
            "quantity": receiving.quantity,
            "received_at": str(receiving.received_at)
        })

    return jsonify(result), 200


@routes.route("/receivings", methods=["POST"])
def add_receiving():

    data = request.get_json() or {}

    product_id = data.get("product_id")
    quantity = data.get("quantity")

    if not product_id or quantity is None:
        return jsonify({
            "message": "Product ID and quantity are required"
        }), 400

    product = Product.query.get(product_id)

    if not product:
        return jsonify({
            "message": "Product not found"
        }), 404

    if quantity <= 0:
        return jsonify({
            "message": "Quantity must be greater than 0"
        }), 400

    receiving = Receiving(
        product_id=product_id,
        quantity=quantity
    )

    product.quantity += quantity

    db.session.add(receiving)
    db.session.commit()

    return jsonify({
        "message": "Receiving added successfully",
        "receiving": {
            "id": receiving.id,
            "product_id": receiving.product_id,
            "quantity": receiving.quantity,
            "received_at": str(receiving.received_at)
        },
        "new_stock": product.quantity
    }), 201


@routes.route("/receivings/<int:id>", methods=["PUT"])
def update_receiving(id):

    receiving = Receiving.query.get(id)

    if not receiving:
        return jsonify({
            "message": "Receiving not found"
        }), 404

    data = request.get_json() or {}

    old_product = Product.query.get(
        receiving.product_id
    )

    if not old_product:
        return jsonify({
            "message": "Old product not found"
        }), 404

    new_product_id = data.get(
        "product_id",
        receiving.product_id
    )

    new_quantity = data.get(
        "quantity",
        receiving.quantity
    )

    new_product = Product.query.get(new_product_id)

    if not new_product:
        return jsonify({
            "message": "New product not found"
        }), 404

    if new_quantity <= 0:
        return jsonify({
            "message": "Quantity must be greater than 0"
        }), 400

    # Remove old receiving quantity
    old_product.quantity -= receiving.quantity

    if old_product.quantity < 0:
        old_product.quantity = 0

    # Add new receiving quantity
    new_product.quantity += new_quantity

    receiving.product_id = new_product_id
    receiving.quantity = new_quantity

    db.session.commit()

    return jsonify({
        "message": "Receiving updated successfully"
    }), 200


@routes.route("/receivings/<int:id>", methods=["DELETE"])
def delete_receiving(id):

    receiving = Receiving.query.get(id)

    if not receiving:
        return jsonify({
            "message": "Receiving not found"
        }), 404

    product = Product.query.get(
        receiving.product_id
    )

    if product:
        product.quantity -= receiving.quantity

        if product.quantity < 0:
            product.quantity = 0

    db.session.delete(receiving)
    db.session.commit()

    return jsonify({
        "message": "Receiving deleted successfully"
    }), 200


# =========================================================
# REPORT - STOCK
# =========================================================

@routes.route("/reports/stock", methods=["GET"])
def stock_report():

    products = Product.query.all()

    result = []

    for product in products:

        price = float(product.price or 0)
        quantity = product.quantity or 0

        result.append({
            "id": product.id,
            "product": product.name,
            "sku": product.sku,
            "quantity": quantity,
            "price": price,
            "stock_value": price * quantity
        })

    return jsonify(result), 200


# =========================================================
# REPORT - ORDERS
# =========================================================

@routes.route("/reports/orders", methods=["GET"])
def orders_report():

    orders = Order.query.order_by(
        Order.id.desc()
    ).all()

    result = []

    for order in orders:
        result.append({
            "id": order.id,
            "order_number": order.order_number,
            "customer_name": order.customer_name,
            "status": order.status,
            "created_at": str(order.created_at)
        })

    return jsonify(result), 200


# =========================================================
# REPORT - SHIPMENTS
# =========================================================

@routes.route("/reports/shipments", methods=["GET"])
def shipments_report():

    shipments = Shipment.query.order_by(
        Shipment.id.desc()
    ).all()

    result = []

    for shipment in shipments:
        result.append({
            "id": shipment.id,
            "order_id": shipment.order_id,
            "tracking_number": shipment.tracking_number,
            "status": shipment.status,
            "shipped_at": str(shipment.shipped_at)
            if shipment.shipped_at else None
        })

    return jsonify(result), 200


# =========================================================
# REPORT - SUMMARY
# =========================================================

@routes.route("/reports/summary", methods=["GET"])
def reports_summary():

    products = Product.query.all()

    total_products = len(products)

    total_stock = sum(
        (product.quantity or 0)
        for product in products
    )

    total_stock_value = sum(
        (float(product.price or 0) *
         (product.quantity or 0))
        for product in products
    )

    low_stock_products = sum(
        1
        for product in products
        if (product.quantity or 0) < 10
    )

    return jsonify({
        "total_products": total_products,
        "total_stock": total_stock,
        "total_stock_value": total_stock_value,
        "low_stock_products": low_stock_products,
        "total_warehouses": Warehouse.query.count(),
        "total_locations": Location.query.count(),
        "total_orders": Order.query.count(),
        "total_shipments": Shipment.query.count(),
        "total_receivings": Receiving.query.count()
    }), 200


# =========================================================
# DASHBOARD API
# =========================================================

@routes.route("/dashboard", methods=["GET"])
def dashboard():

    products = Product.query.all()

    total_stock = sum(
        (product.quantity or 0)
        for product in products
    )

    total_stock_value = sum(
        float(product.price or 0) *
        (product.quantity or 0)
        for product in products
    )

    low_stock_products = sum(
        1
        for product in products
        if (product.quantity or 0) < 10
    )

    return jsonify({
        "total_warehouses": Warehouse.query.count(),
        "total_locations": Location.query.count(),
        "total_products": Product.query.count(),
        "total_orders": Order.query.count(),
        "total_shipments": Shipment.query.count(),
        "total_receivings": Receiving.query.count(),
        "total_stock": total_stock,
        "low_stock_products": low_stock_products,
        "total_stock_value": total_stock_value
    }), 200