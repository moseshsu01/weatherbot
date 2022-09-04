import discord
import responses
import os


async def sendMessage(message, userMessage, isPrivate):
    try:
        response = responses.handleResponse((userMessage))
        await message.author.send(response) if isPrivate else await message.channel.send(response)
    except Exception as e:
        print(e)


def runBot():
    TOKEN = os.environ['WEATHERIA_TOKEN']
    intents = discord.Intents.default()
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'Logged in as {client.user}')

    client.run(TOKEN)
