import requests

url = "http://127.0.0.1:5000/locations"

data = {
    "warehouse_id": 1,
    "location_code": "A-02",
    "description": "Electronics Storage Area"
}

response = requests.post(url, json=data)

print("Status:", response.status_code)
print("Response:", response.json())