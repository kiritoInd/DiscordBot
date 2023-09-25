import discord
import random

token = "YOUR BOT TOKEN"  
channel_id = "channel id"

messages = ["chacha gandu h", "chacha chokke", "suiii", "jadli wah sai hato" , "anmol bkl" , "torimakiechode" ,"chutmarika"]

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}')
    
@client.event
async def on_message(message):
    print(f"Received message: {message.content}")
    if message.author == client.user:
        return
    if message.content == '':
        response = random.choice(messages)
        await message.channel.send(response)

client.run(token)
