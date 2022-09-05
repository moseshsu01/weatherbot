import discord
import responses
import os
import weather


async def sendMessage(message, userMessage, isPrivate):
    try:
        response = responses.handleResponse((userMessage))
        await message.author.send(response) if isPrivate else await message.channel.send(response)
    except Exception as e:
        print(e)

weatherKeyMap = {
    'temperature': 'Temperature',
    'feelsLike': 'Feels Like',
    'condition': 'Condition'
}


def runBot():
    TOKEN = os.environ['WEATHERIA_TOKEN']
    intents = discord.Intents(messages=True, guilds=True, message_content=True)
    client = discord.Client(command_prefix=',', intents=intents)

    @client.event
    async def on_ready():
        print(f'Logged in as {client.user}')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        userMessage = str(message.content)
        result = responses.handleResponse(userMessage)

        if isinstance(result, str):
            response = discord.Embed(title='Error', description=result)
            await message.channel.send(embed=response)
        elif result is None:
            return
        else:
            name = result['name']
            response = discord.Embed(title=f'Weather in {name}')
            for key in result:
                if key != 'name':
                    response.add_field(name=weatherKeyMap[key], value=result[key], inline=False)
            await message.channel.send(embed=response)

    client.run(TOKEN)
