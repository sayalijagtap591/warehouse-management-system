import requests

url = "http://127.0.0.1:5000/warehouses/5"

data = {
    "name": "Updated Test Warehouse",
    "address": "Gangapur Road",
    "city": "Nashik",
    "state": "Maharashtra"
}

response = requests.put(url, json=data)

print("Status:", response.status_code)
print("Response:", response.text)