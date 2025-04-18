import discord 
from discord.ext import commands
import re
from recipeclass import Recipe
import signal
import asyncio

# Token 
with open("token.txt","r") as f:
    token=f.readline().strip()

# Global variables
recipe_list = []

# Bot definition
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

# Function to handle cleanup before shutdown
async def shutdown():
    print("Bot is shutting down...")
    global recipe_list
    print(recipe_list)
    Recipe.toxlsx(recipe_list,"myRecipes.xlsx")
    await bot.close()

# Signal handler for graceful shutdown
def signal_handler(signal_received, frame):
    loop = asyncio.get_event_loop()
    loop.create_task(shutdown())

# Register signal handlers
signal.signal(signal.SIGINT, signal_handler)  # Capture Ctrl+C
signal.signal(signal.SIGTERM, signal_handler)  # Capture termination signals

# Client events
@bot.event
async def on_message(message: discord.Message):
    if message.author.bot:
        return 
    content = message.content
    if "https://www.instagram.com" in content or "https://www.facebook.com" in content:
            link = re.search(r'(https?://[^\s]+)', content)[0]
            await message.channel.send(f'if you want to add a recipe in the recipe list please use the command /hungry')

# Commands with prefix
@bot.command()
async def test(context):
     await context.send(test)

# Slash commands
@bot.tree.command()
async def hungry(interaction: discord.Interaction, type: str, link: str, desc: str):
    global recipe_list
    newRecipe = Recipe(type,link,desc)
    recipe_list.append(newRecipe)
    print(recipe_list)
    await interaction.response.send_message(f"{desc} recipe was added to {type}")

@bot.event
async def on_ready():
    print(f'{bot.user} connected!')
    try:
        synced = await bot.tree.sync()
        print(f'{len(synced)} command(s) synced')
    except Exception as e:
        print(e)

def main():
    global recipe_list
    recipe_list = Recipe.xlsxToRecipeList('myRecipes.xlsx')    
    bot.run(token)

# Launching the client
if __name__ == '__main__':
    main()
