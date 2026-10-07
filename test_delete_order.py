import requests

url = "http://127.0.0.1:5000/orders/4"

response = requests.delete(url)

print("Status:", response.status_code)
print("Response:", response.text)