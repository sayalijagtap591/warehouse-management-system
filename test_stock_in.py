import requests

url = "http://127.0.0.1:5000/stock-movements"

data = {
    "product_id": 2,
    "movement_type": "IN",
    "quantity": 10
}

response = requests.post(url, json=data)

print("Status:", response.status_code)
print("Response:", response.json())