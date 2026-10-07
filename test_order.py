import requests

url = "http://127.0.0.1:5000/orders"

data = {
    "order_number": "ORD002",
    "customer_name": "Rahul Patil",
    "status": "Pending"
}

response = requests.post(url, json=data)

print("Status:", response.status_code)
print("Response:", response.json())







