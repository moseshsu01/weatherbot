import requests
import os


def getWeather(location):
    apiKey = os.environ['WEATHER_API_KEY']

    baseUrl = 'http://api.weatherapi.com/v1'

    parameters = {
        'key': apiKey,
        'q': location
    }

    requestUrl = baseUrl + '/current.json'

    try:
        response = requests.get(requestUrl, parameters).json()
        locationObj = response['location']
        currentObj = response['current']

        weatherInfo = {
            'name': locationObj['name'],
            'temperature': str(currentObj['temp_c']) + '°C',
            'feelsLike': str(currentObj['feelslike_c']) + '°C',
            'condition': currentObj['condition']['text']
        }

        return weatherInfo
    except Exception as e:
        if e == 'location':
            return 'Error: invalid location'

    return 'Error: weather not found'
