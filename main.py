import discord
from discord.ext import commands
import requests
from datetime import datetime, timezone

token = ''  # put your bot token here
verification_channel_id =   # put the id of your verification channel here (the one the users will send !verify in
verified_role =  # put the id of your "verified" role that would have access to the channels
min_age = # put the minimum age (in days) that you want both accounts to be

intents = discord.Intents.default()
intents.members = True
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

def discord_account_age(discord_id): 
    timestamp = ((int(discord_id) >> 22) + 1420070400000) / 1000  
    account_creation_date = datetime.fromtimestamp(timestamp, timezone.utc)
    current_date = datetime.now(timezone.utc)
    age = current_date - account_creation_date
    return age.days

@bot.command()
async def verify(ctx):
    if ctx.channel.id == verification_channel_id:
        roblox_username = ctx.author.display_name 
        search_url = f"https://users.roblox.com/v1/users/search?keyword={roblox_username}&limit=10"
        search_response = requests.get(search_url)

        if search_response.status_code == 200 and search_response.json().get("data"):
            roblox_user_info = search_response.json()["data"][0]  
            roblox_id = roblox_user_info["id"]
            

            user_info_url = f"https://users.roblox.com/v1/users/{roblox_id}"
            user_info_response = requests.get(user_info_url)
            if user_info_response.status_code == 200:
                account_creation_date = user_info_response.json().get("created")
                creation_date = datetime.fromisoformat(account_creation_date.rstrip('Z') + '+00:00')
                current_date = datetime.now(timezone.utc)
                roblox_account_age = (current_date - creation_date).days

                discord_age = discord_account_age(ctx.author.id)

                if discord_age > min_age and roblox_account_age > min_age:
                    role = discord.utils.get(ctx.guild.roles, id=verified_role)
                    if role:
                        await ctx.author.add_roles(role)
                        await ctx.send(f"Verified")
                    else:
                        await ctx.send("role not found")
                else:
                    await ctx.send("Not verified (too young accounts)")
            else:
                await ctx.send("User data fetching threw an error")
        else:
            await ctx.send("Roblox user not found")
    


bot.run(token)
