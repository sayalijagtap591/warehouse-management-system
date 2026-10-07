import requests

url = "http://127.0.0.1:5000/locations/4"

data = {
    "warehouse_id": 1,
    "location_code": "C-02",
    "description": "Updated Storage Area"
}

response = requests.put(url, json=data)

print("Status:", response.status_code)
print("Response:", response.text)