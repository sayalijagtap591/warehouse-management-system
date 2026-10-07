import requests

url = "http://127.0.0.1:5000/warehouses"

data = {
    "name": "Test Warehouse",
    "address": "College Road",
    "city": "Nashik",
    "state": "Maharashtra"
}

response = requests.post(url, json=data)

print("Status:", response.status_code)
print("Response:", response.text)