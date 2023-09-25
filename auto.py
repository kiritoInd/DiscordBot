import discord
import random

token = "YOUR TOKEN"  
channel_id = "Channel ID"

messages = ["chacha gandu h", "chacha chokke", "suiii", "jadli wah sai hato" , "anmol bkl" , "torimakiechode" ,"chutmarika"]
messages2 = ["accha card chaiye" , "card lelo" , "ew phir agye"]

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}')
    
@client.event
async def on_message(message):
    print(f"Received message: {message.content}")
    if message.author == client.user:
        return
    if message.content == 'Roast Deadman':
        response = random.choice(messages)
        await message.channel.send(response)
    if message.content == '<@285291001055019008> is dropping the cards':
        response = random.choice(messages1)
        await message.channel.send(response)

client.run(token)
