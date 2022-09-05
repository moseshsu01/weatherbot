import weather


def handleResponse(message):
    if message.startswith('!weather'):
        index = message.find(' ')

        if index > 0:
            location = message[index + 1:]
            res = weather.getWeather(location)
            return res

    return None
