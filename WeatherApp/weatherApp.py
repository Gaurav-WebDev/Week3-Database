import requests

url = "https://weatherapi-com.p.rapidapi.com/current.json"

locationName = input("Enter your location : ")

querystring = {"q":locationName}

headers = {
	"x-rapidapi-key": "f10810918fmsha9dca74b2bad392p146933jsn23a62edfe815",
	"x-rapidapi-host": "weatherapi-com.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

data = response.json()

location = data['location']
current = data['current']

print("--------------")

print(f"Weather in {location['name']}({location['region']} , {location['country']})")
print(f"Condition : {current['condition']['text']}")
print(f"Current Temp. ( in celcius ) : {current['temp_c']}")
print(f"Humidity : {current['humidity']}")
print(f"HeatIndex ( in celcius ) : {current['heatindex_c']}")