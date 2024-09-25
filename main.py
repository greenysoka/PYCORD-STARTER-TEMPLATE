# EASY TEMPLATE TO START WITH PY-CORD
import discord                                          #insert this to your terminal: pip install py-cord
from discord.ext import tasks, commands
import os
import random

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True
intents.messages = True
intents.presences = True


# configure your bot. You'll need it for all commands and ui components
# If you only use slash commands, you don't need a command_prefix
bot = commands.Bot(command_prefix='!bot', intents=intents)


# Send a message in your console when the bot is ready.
@bot.event
async def on_ready():
    change_status.start()
    latency_rounded = round(bot.latency, 2)
    print(f"❱ Bot started as:")
    print(f"『 {bot.user.name} 』")
    print("")
    print("❱ Ping:")
    print(f"『 {latency_rounded}ms 』")


# Auto-changing status for your bot
@tasks.loop(seconds=50) 
async def change_status():
    serverid = int(1177508137511694357) # put in correct server id!
    # Check server ID with "guild"
    guild = bot.get_guild(serverid)
    if guild:
        # Count server members
        member_count = guild.member_count
        # Get latency in seconds
        latency_rounded = round(bot.latency, 2)
    else:
        print("Wrong server ID! (404 not found) => line 35")
        
    # Here you can put in your custom message that should be displayed
    status_messages = [
    "Playing with admin commands", 
    "Made with 🤍 by @greenysoka", 
    f"Ping: {latency_rounded}s", 
    "eating pizza",
    f"chatting with {member_count} users"
]
    new_status = random.choice(status_messages)
    # Set the status for the bot
    await bot.change_presence(activity=discord.CustomActivity(new_status), status=discord.Status.online)



        ##############################

# define ping slash command
@bot.slash_command(name="ping", description="Check the ping for the template bot!")
# define async function
async def pingcmd(ctx):
    # reply with the latency of the bot
    await ctx.respond(f"Bot is online! > Ping: {bot.latency}s")

        ##############################


# Get your Token from the .env File and start bot. Don't change these lines
token = "abc" # REPLACE WITH YOUR REAL TOKEN
bot.run(token)

# TEMPLATE BY GREENY > (Discord: @greenysoka)
# Contact me for questions or suggestions!