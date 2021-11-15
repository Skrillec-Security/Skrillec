import discord

help_cmds = r""

class Skrillec(discord.Client):
    async def on_ready(self):
        print("\nbot has started")

    async def on_message(self, msg):
        msg_args = msg.content.split(" ")
        if msg.author == self.user:
            return

        if "help" in msg.content and msg.content != "help":
            await msg.channel.send("```{}```".format(help_cmds))

        if "clear" in msg.content:
            if len(msg_args) == 1:
                await msg.channel.send("[x] Invalid argument\nUsage: clear <amount>")
            else:
                await msg.channel.purge(limit = int(msg_args[1]))

        print(msg.content)
        


'''
@client.command()
async def clear(ctx, amount):
    await ctx.channel.purge(limit = amount)


input = int(input(">>> "))
print(input)
'''