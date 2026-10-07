import requests

url = "http://127.0.0.1:5000/products"

data = {
    "sku": "PROD001",
    "name": "Laptop",
    "category": "Electronics",
    "price": 50000,
    "quantity": 10
}

response = requests.post(url, json=data)

print("Status:", response.status_code)
print("Response:", response.json())