import weather


def handleResponse(msg):
    message = msg.lower()

    if message.startswith('!weather'):
        location = message.split(' ')[1]
        res = weather.getWeather(location)

    return None
