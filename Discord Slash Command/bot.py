import random

import discord
from discord.ext import commands
from discord_slash import SlashCommand
from discord_slash.model import SlashContext
from discord_slash.utils import manage_commands
import requests

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
slash = SlashCommand(bot)

# url = "https://discord.com/api/v8/applications/777129864477278219/guilds/503104675256729600/commands"

# json = {
#     "name": "ping",
#     "description": "Returns the ping of the bot."
# }

# headers = {
#     "Authorization": "Bot " + "Nzc3MTI5ODY0NDc3Mjc4MjE5.X6-8lg.--FZPMfi3ZfaOdRAS6ljQ0pPHe8"
# }


@bot.event
async def on_ready():
    # r = requests.post(url, headers=headers, json=json)
    # print(r)
    await manage_commands.add_slash_command(
        777129864477278219, "Nzc3MTI5ODY0NDc3Mjc4MjE5.X6-8lg.--FZPMfi3ZfaOdRAS6ljQ0pPHe8", 503104675256729600, "hehe", "Sends hoho")

    print("Ready!")


@slash.slash(name="ping")
async def ping_slash(ctx):  # Normal usage.
    await ctx.send(content=f"Pong! (`{round(bot.latency*1000)}`ms)")


@slash.slash(name="hehe")
async def hehe_slash(ctx):  # Normal usage.
    await ctx.send(content="Hoho")


bot.run("Nzc3MTI5ODY0NDc3Mjc4MjE5.X6-8lg.--FZPMfi3ZfaOdRAS6ljQ0pPHe8")
