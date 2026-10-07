import requests

url = "http://127.0.0.1:5000/products/1"

response = requests.delete(url)

print("Status:", response.status_code)
print("Response:", response.json())