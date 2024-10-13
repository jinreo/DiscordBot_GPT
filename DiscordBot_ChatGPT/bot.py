# bot.py
import os
import discord
from dotenv import load_dotenv
from chatgpt import send_to_chatGpt

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
CHANNEL_ID = os.getenv('CHANNEL_ID')

intents = discord.Intents.all()
client = discord.Client(command_prefix='!', intents=intents)

@client.event
async def on_ready():
  print(f'We have logged in as {client.user.name}')
  channel = client.get_channel(int(CHANNEL_ID))
  await channel.send("GPT 준비 완료")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    messages = [{"role": "user", "content": message.content}]
    response = send_to_chatGpt(messages)

    await message.channel.send(response)

# start the bot
client.run(TOKEN)
