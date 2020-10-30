import requests

response = requests.get("http://randomfox.ca/floof")
fox = response.json()
print(response.status_code)
print(response.text)
print(fox['image'])