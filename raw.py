# This is the main.py without comments:

import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    latency_rounded = round(bot.latency, 2)
    print(f"❱ Started as:")
    print(f"『 {bot.user.name} 』")
    print("")
    print("❱ Ping:")
    print(f"『 {latency_rounded}s 』")
    await bot.change_presence(activity=discord.CustomActivity("Bot is online! :D"), status=discord.Status.online)

@bot.slash_command(name="ping", description="Check the ping for your new bot!")
async def pingcmd(ctx):
    await ctx.respond(f"Congrats, bot is online! > Ping: {bot.latency}s")

token = "abc"
bot.run(token)

# Check the main.py for detailed comments on every line!
