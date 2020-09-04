import requests, json

f = requests.get('http://localhost:5000/restaurant/10/menu/10/JSON').json()


print(f)


