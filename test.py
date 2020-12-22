# Name: bot.py
# Kind: Main bot file
# Version: 0.1.0

import os
from configparser import ConfigParser
from pathlib import Path

import discord
from discord.ext import commands
from discord_slash.utils import manage_commands

VERSION = os.getenv("DISCORD_BOT_VERSION")
PREFIX = os.getenv("DISCORD_BOT_PREFIX")
TOKEN = os.getenv("DISCORD_BOT_TOKEN")
BOT_ID = int(os.getenv("DISCORD_BOT_ID"))
GUILD_ID = int(os.getenv("DISCORD_BOT_GUILD_ID"))


class Bot(commands.Bot):  # Main bot class
    def __init__(self):
        self._cogs = [p.stem for p in Path(".").glob(
            "./bot/cogs/*.py")]  # load cogs as a glob
        super().__init__(command_prefix=PREFIX,
                         case_insensitive=True, intents=discord.Intents.all())  # Set intends, prefix, etc

    # Cog setup
    def setup(self):  # Triggerd by run
        print("Running setup...")  # Print running setup

        for cog in self._cogs:  # Go trough every cog in cogs folder
            self.load_extension(f"bot.cogs.{cog}")  # Load the cog
            print(f" Loaded [{cog}] cog!")  # Print cog ready

        print("Setup complete.")  # Print setup complete

    # Run the bot
    def run(self):  # Trigger on script start
        self.setup()  # Run the setup process
        self.token = TOKEN

        print(f"Running bot [v{VERSION}].")  # Print running
        super().run(self.token, reconnect=True)  # Run bot with TOKEN

    # Shutdown bot
    async def shutdown(self):  # Trigger on keyboard interrupt
        # Print closing the connection to the discord servers
        print("Closing connection to Discord...")
        await super().close()  # Close the bot

    # Close bot
    async def close(self):  # Triggered by shutdown
        print("Closing on keyboard interrupt...")  # Print closing
        await self.shutdown()  # Kill bot application

    # When connected to discord
    async def on_connect(self):  # Trigger on bot connected to discord servers
        # Print connected and get latecy to discord servers
        print(f" Connected to Discord (latency: {self.latency*1000:,.0f} ms)")

    # When bot resumed
    async def on_resumed(self):  # Trigger on bot resumed
        print("Bot resumed.")  # Print resumed

    # When bot disconnected from discord servers
    async def on_disconnect(self):  # Trigger on disconnect from discord servers
        print("Bot disconnected.")  # Print disconnected

    # When an error occurs
    async def on_error(self, err, *args, **kwargs):  # Trigger on error
        error_channel = self.bot.get_channel(
            768867099614773358)  # Get error channel by id
        error_channel.send("An error occured.")  # Log "An error occured"

    # When the bot is ready
    async def on_ready(self):  # Trigger on bot ready
        self.client_id = (await self.application_info()).id

        print("Registering slash commands...")

        await manage_commands.add_slash_command(BOT_ID, TOKEN, GUILD_ID, "ping", "Returns the ping of the bot to the discord servers.")
        print(" Registered [ping] slash command.")
        await manage_commands.add_slash_command(BOT_ID, TOKEN, GUILD_ID, "add", "Returns the result of a addition.")
        print(" Registered [add] slash command.")

        print("Done registering slash commands.")

        print("Bot ready.")  # Print ready

        # activity = discord.Activity(
        #     name='my activity', type=discord.ActivityType.custom)
        # await self.bot.change_presence(activity=activity)

    # Define the prefix
    async def prefix(self, bot, msg):  # Define the prefix
        return commands.when_mentioned_or(PREFIX)(bot, msg)

    # Process commands
    async def process_commands(self, msg):  # Process commands
        ctx = await self.get_context(msg, cls=commands.Context)

        if ctx.command is not None:
            await self.invoke(ctx)

    # When a message is sent
    async def on_message(self, msg):  # Trigger on message
        if not msg.author.bot:  # If the user is not a bot
            await self.process_commands(msg)  # Process the command
        else:  # If the user is a bot ignore the command
            pass
