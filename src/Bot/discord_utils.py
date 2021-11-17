import discord

class discordUtils:
    async def send_Message(client, Title, Description):
        embed = discord.Embed(title=Title, description=Description, color=discord.Color.red())
        await client.channel.send(embed=embed)
