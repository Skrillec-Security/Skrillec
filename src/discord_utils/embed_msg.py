import os, sys, time, discord, random

async def embed(client, ttitle, ddescription):
    embedVar = discord.Embed(title=ttitle, description=ddescription, color=0xff0000)
    lul = ['https://c.tenor.com/ccKhodmHDUEAAAAC/la-capone.gif',
    'https://media1.giphy.com/media/11Ad7FqUiNMRAA/giphy.gif',
    'https://i.imgur.com/S1yXrH8.gif',
    'https://c.tenor.com/ofYCY_OJQ1kAAAAd/hacker-hack.gif',
    'https://media3.giphy.com/media/YQitE4YNQNahy/giphy-downsized-large.gif']
    embedVar.set_image(url=lul[random.randrange(0, len(lul))])
    # embedVar.add_field(name="Field1", value="hi", inline=False)
    # embedVar.add_field(name="Field2", value="hi2", inline=False)
    await client.channel.send(embed=embedVar)