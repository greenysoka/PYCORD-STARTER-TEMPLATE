# EASY TEMPLATE TO START WITH PY-CORD
# Official Py-Cord Guide: https://guide.pycord.dev/category/getting-started

# These are your imports
import discord                                          
from discord.ext import commands # For "Py-Cord" you only have to import discord and commands

# IMPORTANT
# insert this to your terminal: pip install py-cord
# IMPORTANT

# These are your intents
# You're defining the categories your bot can interact with
intents = discord.Intents.default()
intents.message_content = True # Access to messages on the server
intents.guilds = True # Access to guilds on the server
intents.members = True # Access to members on the server


# configure your bot. You'll need it for all commands and ui components
# If you only use slash commands, you don't need a command_prefix
bot = commands.Bot(command_prefix='!', intents=intents)


# Send a message in your console when the bot is ready.
@bot.event
async def on_ready():
    latency_rounded = round(bot.latency, 2)
    print(f"❱ Started as:")
    print(f"『 {bot.user.name} 』")
    print("")
    print("❱ Ping:")
    print(f"『 {latency_rounded}s 』")
    # Set the status of your bot. In this case the bot would be "online" and the status message is "Bot is online! :D"
    await bot.change_presence(activity=discord.CustomActivity("Bot is online! :D"), status=discord.Status.online)



# define ping slash command
@bot.slash_command(name="ping", description="Check the ping for your new bot!")
# define async function with ctx parameter
# you need ctx to respond to the user interaction (using the command)
async def pingcmd(ctx):
    # reply with the latency of the bot
    await ctx.respond(f"Congrats, bot is online! > Ping: {bot.latency}s")

        ##############################


# Define your token from the discord developer portal
token = "abc" # REPLACE WITH YOUR REAL TOKEN
bot.run(token)

# TEMPLATE BY GREENY > (Discord: @greenysoka)
# Contact me for questions or suggestions!

# Order your own custom discord bot for free!
# - https://sokabots.com
# - https://greenysoka.sokabots.com
# - https://discord.sokabots.com
