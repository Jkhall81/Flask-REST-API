import requests

BASE = "http://localhost:5000/"

data = {
    'name': 'My Video',
    'views': 100,
    'likes': 50
}

response = requests.get(BASE + "video/1", json=data)
print(response.json())

