import requests

url = "http://127.0.0.1:5000/receivings"

data = {
    "product_id": 2,
    "quantity": 10
}

response = requests.post(url, json=data)

print("Status:", response.status_code)
print("Response:", response.text)