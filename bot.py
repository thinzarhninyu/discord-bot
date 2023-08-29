import discord
from discord.ext import commands
import responses
import gpt
import os
from dotenv import load_dotenv
# from help_cog import help_cog
# from music_cog import music_cog

# bot = commands.Bot(command_prefix='/')

# bot.remove_command('help')

# bot.add_cog(help_cog(bot))
# bot.add_cog(music_cog(bot))

load_dotenv()   

def create_intents():
    intents = discord.Intents.default()
    intents.message_content = True
    return intents

async def send_message(command, message, user_message, is_private):
    try:
        if command == '/ai' or command == '/gpt':   
            response = gpt.handle_response(user_message)
        else:
            response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print (e)
        
def run_discord_bot():
    TOKEN = os.getenv('TOKEN') 
    client = discord.Client(intents = create_intents())
    
    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')
        
    @client.event
    async def on_message(message):

        if message.author == client.user:
            return
        
        username = str(message.author)
        user_message = '';
        command = ''
        
        for text in ['/ai', '/bot', '/gpt']:
            if message.content.startswith(text):
                command = message.content.split(' ')[0]
                user_message = message.content.replace(text, '')
            else: 
                user_message = str(message.content)
      
        channel = str(message.channel)
        
        print(f"{username} said: '{user_message}' ({channel})")
        
        if user_message.strip() and user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(command, message, user_message, is_private=True)
        else:
            await send_message(command, message, user_message, is_private=False)
        
    client.run(TOKEN)