import os, sys, time, discord

class Discord_Utils:
    # This function is to find a role within the same server the message was sent from
    def find_role_in_server(client, name):
        for i in client.guild.roles:
            if i.name == name:
                return i.id, i.name
        return 0

    def find_member_in_server(client, uid):
        all_members = client.guild.members
        for user in all_members:
            if user.id == uid:
                return user
        return 0

    def find_channel_in_server(client, name):
        all_channels = client.guild.channels
        return 0