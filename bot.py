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
        response = responses.handleResponse(userMessage)

        if response:
            await message.channel.send(response)

    client.run(TOKEN)
