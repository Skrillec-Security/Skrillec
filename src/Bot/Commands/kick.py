import discord


async def dick(client, fmsg, msg_args, reason='Bad intentions'):
    if client.author.guild_permissions.administrator == False:
        await client.channel.send('not enough perms.')
        return
    elif client.author.guild_permissions.administrator:
        if len(msg_args) > 1:
            userid = msg_args[1]
            if "<@" in userid: userid = userid.replace("<@", "").replace(">","").replace("!", "")
            elif userid == '':  await client.channel.send('missing arguments.') ; return

            userid = int(userid)
            await client.guild.kick(discord.Object(id=userid))
            kick = discord.Embed(title='User has been Kicked!', color=discord.Color.dark_purple(), description='<@{}> has been kicked'.format(userid))
            await client.channel.send(embed=kick)
