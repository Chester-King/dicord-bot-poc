import json
  
import discord

# Opening JSON file
f = open('token.json')
  
# returns JSON object as 
# a dictionary
data = json.load(f)

async def send_message(message, resp):
    
    
    try:
        await message.channel.send(resp)
        await message.channel.send(file=discord.File('2.png'))
    except Exception as e:
        print(e)


def run_discord_bot():
    TOKEN = data["token"]
    client = discord.Client()

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print("Begin -",user_message[:7])
        print("End -",user_message[-1])

        if(user_message[:7]=='/draw "' and user_message[-1]=='"'):
            if(channel=="random"):
                print("Concerned Text : ",user_message[7:len(user_message)-1])
                ct = user_message[7:len(user_message)-1]
                await send_message(message,ct)

        print(f"{username} said '{user_message}' ({channel})")


    client.run(TOKEN)

def handle_response(message) -> str:
    p_message = message.lower()
    
    if p_message == 'hello':
        return 'Hey There!'

run_discord_bot()