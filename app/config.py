class Config:
    SECRET_KEY = "warehouse-secret-key"

    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:root%40123@localhost/warehouse_db"

    SQLALCHEMY_TRACK_MODIFICATIONS = False