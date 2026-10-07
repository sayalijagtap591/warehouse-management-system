import requests

url = "http://127.0.0.1:5000/warehouses/2"

data = {
    "name": "Pune Central Warehouse",
    "address": "Pune",
    "city": "Pune",
    "state": "Maharashtra"
}

response = requests.put(url, json=data)

print("Status:", response.status_code)
print("Response:", response.json())