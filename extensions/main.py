# // Imports //
import discord
from discord.ext import commands
from discord import app_commands

# // Commands //
class Main(commands.Cog, name = 'Main Commands'): # creating a class to be an extension
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name = 'ping') # creating a slash command
    async def ping(self, interaction: discord.Interaction): # setting the required parameters
        await interaction.response.send_message('pong!')

async def setup(bot: commands.Bot):
    await bot.add_cog(Main(bot)) # adding the extension to the bot