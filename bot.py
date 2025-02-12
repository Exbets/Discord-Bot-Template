# // Imports //
import yaml
import asyncio
import discord
from discord.ext import commands
from typing import Optional, Literal

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

# // Commands //
@bot.command() # creating a bot command
@commands.is_owner() # checking to see if the command user is the bot owner
async def sync(ctx, type: Optional[Literal['global', 'guild', 'clear']]): # setting parameters
    if type == 'global':
        synced = await bot.tree.sync() # this will sync commands globally across discord
        await ctx.reply(f'Synced {len(synced)} commands globally.')

    elif type == 'guild':
        bot.tree.copy_global_to(guild = ctx.guild) # this will sync commands with the current guild only
        synced = await bot.tree.sync(guild = ctx.guild)
        await ctx.reply(f'Synced {len(synced)} commands.') # the len(synced) is getting the amount of commands that have been synced

    elif type == 'clear': # use this if you have duplicate slash commands
        bot.tree.clear_commands(guild = ctx.guild) # clearing commands synced with the current guild
        await bot.tree.sync(guild = ctx.guild)

# // Startup //
async def main():
    for i in extensions: # looping through the list of extensions from config and loading them
        await bot.load_extension(i)

    async with bot:
        await bot.start(token = token) # staring the bot with the token

asyncio.run(main())