import requests

# API key and endpoint URL
api_key = "your_api_key"
url = f"http://api.openweathermap.org/data/2.5/weather?q=city_name&appid={api_key}"

# city name for which you want to retrieve the weather data
city_name = "New York"

# send a GET request to the API
response = requests.get(url.replace("city_name", city_name))

# parse the response JSON data
weather_data = response.json()

# print the temperature in Celsius
temperature = weather_data["main"]["temp"] - 273.15
print(f"The temperature in {city_name} is {temperature:.2f} Celsius")