import requests

url = "http://127.0.0.1:5000/orders/4"

data = {
    "order_number": "ORD001-UPDATED",
    "customer_name": "Sayali Updated",
    "status": "Processing"
}

response = requests.put(url, json=data)

print("Status:", response.status_code)
print("Response:", response.text)