import requests

# API URL
url = "https://catfact.ninja/fact"

response = requests.get(url)

data = response.json()

print(f"Fact : {data['fact']}")