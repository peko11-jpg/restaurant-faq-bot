import discord
from config import DISCORD_TOKEN

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Bot je online kao {client.user}")


client.run(DISCORD_TOKEN)