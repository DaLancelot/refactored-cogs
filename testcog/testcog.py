import discord
from discord.ext import commands
from .utils import checks
import asyncio
import grequests

class test:
    """a test cog"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def geturl(self, ctx):
        """Gets a invalid URL"""
        r = grequests.get("http://1894328959479797964879346.com", stream=True)

def setup(bot):
    n = test(bot)
    bot.add_cog(n)
