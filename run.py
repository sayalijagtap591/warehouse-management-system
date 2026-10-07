from app import create_app, db
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

app = create_app()
print(app.url_map)

with app.app_context():
    db.create_all()
    print("✅ Database tables created successfully!")

if __name__ == "__main__":
    app.run(debug=True)