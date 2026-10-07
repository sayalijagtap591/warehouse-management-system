import requests

url = "http://127.0.0.1:5000/stock/2"

data = {
    "quantity": 70
}

response = requests.put(url, json=data)

print("Status:", response.status_code)
print("Response:", response.text)