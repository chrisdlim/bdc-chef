import random
from discord.ext import commands
import discord

class DiscordBot(commands.Bot):

    chef_roles = ['BURGER FLIPPER', 'BAKER', 'PIT MASTER', 'VEGGIE LOVER', 'FRYER', 'SOUS CHEF']

    def __init__(self, easter_egg_names):
       super().__init__(command_prefix='/')
       self.easter_egg_names = easter_egg_names

    def get_random_role(self):
        return random.choice(self.chef_roles)
    
    async def send(self, channel, msg):
        await channel.send(msg)

    def is_easter(self, user):
        return str(user).lower() in self.easter_egg_names

    def get_chefs_message(self, user: discord.Member):
        user_id = user.id
        role = self.get_random_role()
        msg = f"In need of a {role}!. LET <@{user_id}> COOK!"

        if self.is_easter(user):
            msg = msg + f" Approximately {random()*100}% chance of winning..."
        
        return msg
