import requests

url = "http://127.0.0.1:5000/receivings/3"

data = {
    "product_id": 2,
    "quantity": 25
}

response = requests.put(url, json=data)

print("Status:", response.status_code)
print("Response:", response.text)