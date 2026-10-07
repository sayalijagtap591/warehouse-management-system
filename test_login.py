import requests

url = "http://127.0.0.1:5000/login"

data = {
    "username": "admin",
    "password": "admin123"
}

print("Sending data:", data)

response = requests.post(
    url,
    json=data,
    headers={"Content-Type": "application/json"}
)

print("Status:", response.status_code)
print("Response:", response.text)