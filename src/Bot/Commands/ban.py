import discord

"""
Advanced Banning System With Unbanning
"""
async def Ban_Syetem(client, fmsg, msg_args):
    try:
        if client.author.guild_permissions.administrator or client.author.id == "909116206668214282": ## Owner ID
            reason = "" ## Empty as no reason for ban
            if len(msg_args) > 1:
                userid = msg_args[1]
                if "<@" in userid: userid = userid.replace("<@", "").replace(">","").replace("!", "")
                userid = int(userid)
                if len(msg_args) > 2:
                    if msg_args[2].startswith("reason="): 
                        reason = msg_args[2].replace("reason=", "")
                        reason += "\nBanned By Skrillec Bot!"
                        await client.channel.send("Banning <@{}>!\nRequested By: <@{}>".format(userid, client.author.id))
                        await client.guild.ban(discord.Object(id=userid), reason=reason)
                    elif msg_args[2] == "1":
                        await client.channel.send("Unbanning <@{}>!\nRequested By <@{}>".format(userid, client.author.id))
                        await client.guild.unban(discord.Object(id=userid))
                else:
                    await client.channel.send("Banning <@{}>!\nRequested By: <@{}>".format(userid, client.author.id))
                    await client.guild.ban(discord.Object(id=userid), reason=reason)
            # else:
            #     await client.channel.send("```[x] Invalid argument!\nUsage: >ban <userid> <reason/1> (use 1 for reason to unban user)\nExample: >ban @skrillec```")
    except:
        await client.channel.send("```[x] Invalid argument!\nUsage: >ban <userid> <reason/1> (use 1 for reason to unban user)\nExample: >ban @skrillec```")