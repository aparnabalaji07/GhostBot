import discord
from discord.ext import commands
import random

# --- SETUP ---
intents = discord.Intents.default()
intents.message_content = True  # allow bot to read messages

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

# --- ANONYMOUS MESSAGE COMMAND ---
@bot.command()
async def ghost(ctx, *, message: str):
    """Send an anonymous message to the #anonymous-chat channel"""
    # Delete user's original message
    try:
        await ctx.message.delete()
    except discord.errors.Forbidden:
        # bot can't delete messages
        pass

    # Find the anonymous chat channel
    channel = discord.utils.get(ctx.guild.text_channels, name="anonymous-chat")

    if channel:
        # Create a random anonymous ID
        anon_id = random.randint(100, 999)
        await channel.send(f"💬 AnonMeow#{anon_id}: {message}")
    else:
        await ctx.send("⚠️ Could not find #anonymous-chat channel. Make sure it exists.")

# --- RUN BOT ---
bot.run("MTQzNzYwNDA1NDgyOTEwOTM3MA.GHw6fv.6JhUfIb0oRm4Pr4Xg0NwZQTAvzU8ehTOFCjFyY")
