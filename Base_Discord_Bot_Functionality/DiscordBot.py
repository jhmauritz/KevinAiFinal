import discord
from discord import Client, utils
from Dependencies.GrabbingCreds import GrabingCreds

TOKEN = GrabingCreds().GrabCreds('discord', 'token')
GUILD = GrabingCreds().GrabCreds('discord', 'guild')
TEST_CHANNEL = GrabingCreds().GrabCreds('discord', 'test_channel')

class Discord_Handler(Client):
    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')

    async def on_member_join(self, member):
        await member.create_dm(f'Hi {member.name}, welcome to my ADHD Brain!')

    async def on_message(self, message):
        print(message.type)
        if message.type is discord.MessageType.pins_add:
            await message.delete()
        if message.author == client.user:
            return
        
        if message.channel.id == int(TEST_CHANNEL):
            await message.channel.send('Hi There')

client = Discord_Handler()