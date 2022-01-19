import os, sys, time, discord

async def embed(client, ttitle, ddescription):
    embedVar = discord.Embed(title=ttitle, description=ddescription, color=0xff0000)
    # embedVar.add_field(name="Field1", value="hi", inline=False)
    # embedVar.add_field(name="Field2", value="hi2", inline=False)
    await client.channel.send(embed=embedVar)