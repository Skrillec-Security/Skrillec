import os, sys, time, discord, random

from .embed_msg import *

async def embed(client, ttitle, ddescription):
    embedVar = discord.Embed(title=ttitle, description=ddescription, color=0xff0000)
    # lul = ['https://media1.giphy.com/media/11Ad7FqUiNMRAA/giphy.gif',
    # 'https://i.imgur.com/S1yXrH8.gif',
    # 'https://c.tenor.com/ofYCY_OJQ1kAAAAd/hacker-hack.gif',
    # 'https://media3.giphy.com/media/YQitE4YNQNahy/giphy-downsized-large.gif']
    # embedVar.set_image(url=lul[random.randrange(0, len(lul))])
    # embedVar.add_field(name="Field1", value="hi", inline=False)
    # embedVar.add_field(name="Field2", value="hi2", inline=False)
    await client.channel.send(embed=embedVar)


class EmbedMessages:
    # lul = ['https://c.tenor.com/m-efsi4uFsoAAAAC/lil-herb-g-herbo.gif', 
    # 'https://media1.giphy.com/media/11Ad7FqUiNMRAA/giphy.gif',
    # 'https://i.imgur.com/S1yXrH8.gif',
    # 'https://c.tenor.com/ofYCY_OJQ1kAAAAd/hacker-hack.gif',
    # 'https://media3.giphy.com/media/YQitE4YNQNahy/giphy-downsized-large.gif']

    async def Help_Menu(client):
        embedVar = discord.Embed(title="Help Commands", description="List of commands", color=0xff0000)
        # embedVar.set_image(url=EmbedMessages.lul[random.randrange(0, len(EmbedMessages.lul))])
        embedVar.add_field(name="help", value="All help list", inline=False)
        embedVar.add_field(name="help acct", value="Account Commands", inline=False)
        embedVar.add_field(name="help mod", value="Moderation Commands", inline=False)
        embedVar.add_field(name="help tools", value="IP/URL Network Tools", inline=False)
        embedVar.add_field(name="help attack", value="Stresser (Premium)", inline=False)
        embedVar.add_field(name="help ansi", value="ANSI/ASCII Tools", inline=False)
        await client.channel.send(embed=embedVar)

    async def Acct_Menu(client):
        embedVar = discord.Embed(title="Help Commands", description="List of commands", color=0xff0000)
        # embedVar.set_image(url=EmbedMessages.lul[random.randrange(0, len(EmbedMessages.lul))])
        embedVar.add_field(name="register", value="Register for Attack System", inline=False)
        embedVar.add_field(name="info", value="Account plan", inline=False)
        embedVar.add_field(name="redeem", value="Redeem a token", inline=False)
        embedVar.add_field(name="help tools", value="IP/URL Network Tools", inline=False)
        await client.channel.send(embed=embedVar)
