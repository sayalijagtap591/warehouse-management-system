import requests

url = "http://127.0.0.1:5000/shipments/2"

data = {
    "tracking_number": "TRK002-UPDATED",
    "status": "Shipped"
}

response = requests.put(url, json=data)

print("Status:", response.status_code)
print("Response:", response.text)
