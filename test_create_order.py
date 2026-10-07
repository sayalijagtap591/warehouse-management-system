import requests

url = "http://127.0.0.1:5000/orders"

data = {
    "order_number": "ORD003",
    "customer_name": "Amit Sharma",
    "status": "Pending"
}

response = requests.post(url, json=data)

print("Status:", response.status_code)
print("Response:", response.text)