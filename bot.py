# // Imports //
import yaml
import asyncio
import discord
from discord.ext import commands

# // Settings //
with open('config.yaml', 'r') as f: # opening the yaml config file in 'read' mode
    config = yaml.safe_load(f)

    token = config['Token'] # getting the token from config
    prefix = config['Prefix']
    extensions = config['Extensions']

intents = discord.Intents.default() # getting discord intents
intents.members = True
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix = prefix, intents = intents) # creating the bot object

# // Events //
@bot.event
async def on_ready(): # creating an event that runs when the bot starts
    print(f'Logged in as {bot.user}')

# // Startup //
async def main():
    for i in extensions: # looping through the list of extensions from config and loading them
        await bot.load_extension(i)

    async with bot:
        await bot.start(token = token) # staring the bot with the token

asyncio.run(main())