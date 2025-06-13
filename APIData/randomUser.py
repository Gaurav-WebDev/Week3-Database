import requests

# API URL

url = "https://randomuser.me/api"

response = requests.get(url)

data = response.json()

print(f"Random User Name : {data['results'][0]['name']['first']}")
print(f"Email : {data['results'][0]['email']}")
print(f"Age : {data['results'][0]['dob']['age']}")
