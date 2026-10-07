import requests

url = "http://127.0.0.1:5000/shipments"

data = {
    "order_id": 2,
    "tracking_number": "TRK002",
    "status": "Pending"
}

response = requests.post(url, json=data)

print("Status:", response.status_code)
print("Response:", response.text)