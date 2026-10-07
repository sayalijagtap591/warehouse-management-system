import requests

url = "http://127.0.0.1:5000/reports/orders"

response = requests.get(url)

print("Status:", response.status_code)
print("Response:", response.text)