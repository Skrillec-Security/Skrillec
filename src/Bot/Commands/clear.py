import os, sys, time, discord
from ..discord_utils import *

# def Clear_System(client, fmsg, msg_args):
#     if client.message.author.guild_permissions.administrator or client.author.id == "":
#         if len(msg_args) < 1:
#             ## nuke the channel
#         else:
#             await 


async def Clear_System(client, fmsg, msg_args):
    try:
        admin = client.author.guild_permissions.administrator;

        if admin == False: await discordUtils.error_Message(client, '***You do not have the required permissions to use this command!***') ; return

        elif admin:
            if len(msg_args) > 1:
                amount = msg_args[1]
                if amount == '': await discordUtils.error_Message(client, '***Usage:*** ```>clear <amount>```') ; return
                else:
                    await client.channel.purge(limit=int(amount))
                    await discordUtils.successful_Message(client, '***Successfully cleared {} messages***'.format(amount))
    except:
        await discordUtils.error_Message(client, "***Don't forget to use a number between 1-100!***")
