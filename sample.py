import requests

request = requests.get("http://127.0.0.1:8086/")

print(request.json())