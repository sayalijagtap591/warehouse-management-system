import requests

url = "http://127.0.0.1:5000/products/1"

data = {
    "sku": "PROD001",
    "name": "Dell Laptop",
    "category": "Electronics",
    "price": 55000,
    "quantity": 15
}

response = requests.put(url, json=data)

print("Status:", response.status_code)
print("Response:", response.json())