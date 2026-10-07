from app import create_app, db
from app.models import User, Warehouse, Location, Product
from flask_bcrypt import Bcrypt

app = create_app()
bcrypt = Bcrypt(app)

with app.app_context():

    # Admin User
    existing_user = User.query.filter_by(username="admin").first()

    if not existing_user:
        hashed_password = bcrypt.generate_password_hash(
            "Admin@123"
        ).decode("utf-8")

        admin = User(
            username="admin",
            email="admin@warehouse.com",
            password=hashed_password,
            role="admin"
        )

        db.session.add(admin)
        db.session.commit()

        print("✅ Admin user created!")
    else:
        print("ℹ️ Admin user already exists!")