import discord

async def on_Join(client):
    role = 'Members'


    add_Roles = discord.utils.get(client.guild.roles, name=role)
    await client.author.add_roles(add_Roles)
    print('{} was given {} role!'.format(client.author, add_Roles))