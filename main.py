import requests

apiKey = "0ea6ae9bab874b0f93c192708220409"

baseUrl = "http://api.weatherapi.com/v1"

parameters = {
    "key": apiKey,
    "q": "Paris"
}

requestUrl = baseUrl + "/current.json"

response = requests.get(requestUrl, parameters).json()
locationObj = response["location"]
currentObj = response["current"]

weatherInfo = {
    "name": locationObj["name"],
    "temperature": str(currentObj["temp_c"]) + "°C",
    "feelsLike": str(currentObj["feelslike_c"]) + "°C",
    "condition": currentObj["condition"]["text"]
}

print(weatherInfo)
