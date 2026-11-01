import requests

response = requests.get("https://jsonplaceholder.typicode.com/users/1")

print(response.status_code)
data = response.json()
print(data)
print(f"Name: {data['name']}", f"Email: {data['email']}")