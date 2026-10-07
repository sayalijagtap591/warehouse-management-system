import requests

url = "http://127.0.0.1:5000/shipments/4"

data = {
    "order_id": 2,
    "tracking_number": "TRK004-UPDATED",
    "status": "Shipped"
}

response = requests.put(url, json=data)

print("Status:", response.status_code)
print("Response:", response.text)