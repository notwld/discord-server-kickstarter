from discord.ext import commands

client = commands.Bot(command_prefix = "sudo")


@client.event
async def on_ready():
    print('Live')



rules = '''\n`1`. **Do not bully, be human.**
Don’t bully others in any kind of shape or form (discriminating, shaming).

`2`. **Do not post NSFW content.**
We don't have NSFW channel, and we do not support NSFW content in any of our channels.
Posting NSFW content will result in mute or permanent ban.

`3`. **Do not spam chats, or abuse bots.**
Spamming or abusing bots is not allowed, this applies to both text channels and voice channels.
Doing so will result in mute or permanent ban.

`4`. **Do not be racist.**
Racism or hate speech isn't allowed and this behavior will be punished.

`5`. **Do not advertise outside advertising channels**
Advertising outside of advertise channel isn't allowed.
Doing so will result in mute. (Or in ban if done repeatedly.)

`6`. **Do not dox other members**
Doxxing isn't allowed on our server in any kind of shape or form.
Doing this will result in permanent ban with no chance to appeal.

`7`. **Do not post inappropriate images/links to images**
Posting images/links with sexual/explicit content isn't allowed.
You'll be muted and/or banned if you'll do so.

`8`. **Respect others**
Try not to discuss any sensitive topics such as politics,religion etc.
Also try to keep topics within their specific channels.'''

@client.event
async def on_message(message):
    
    global rules

    if client.user.mentioned_in(message):


        id=[server.id for server in client.guilds][0]
        memberCount=[server.member_count for server in client.guilds][0]
        
        server=client.get_guild(id)


        with open('icon.jpg','rb+') as img:
            icon=img.read()

        await server.edit(icon=icon) #for server's icon
        # await client.user.edit(avatar=icon) #for bot's pfps

        [await vc.delete() for server in client.guilds for vc in server.voice_channels]
        
        [await channels.delete() for server in client.guilds for channels in server.text_channels]

        [await cat.delete() for server in client.guilds for cat in server.categories]

        await server.create_voice_channel(f"Member Count : {memberCount}",perm=False)

        
        welcome=await server.create_category('Welcome')
        ch=await server.create_text_channel('rules',category=welcome)
        members=await server.create_text_channel('members',category=welcome)
        roles=await server.create_text_channel('roles',category=welcome)

        await client.get_channel(ch.id).send(f"**___`R    u   l   e   s`___**\n{rules}")


        text_ch=['tawk','media','memes','spam','bot commands','dank memer','wholesome']

        media_ch=['selfies','pets','art','photofraphy']

        vc_ch=['vc000','vc001','vc010','stream000','stream001','stream010','music000','music010','music010','afk000']
        

        cat1=await server.create_category('text channels')
        [await server.create_text_channel(channel,category=cat1) for channel in text_ch]

        cat2=await server.create_category('media')
        [await server.create_text_channel(channel,category=cat2) for channel in media_ch]

        cat3=await server.create_category('vc')
        [await server.create_voice_channel(channel,category=cat3) for channel in vc_ch]


    
client.run('ODUwNDU3MDMwOTY3Njg5MjE3.YLp_1A.4ug5JF7rx3Gwze0NCgmwHH90wnA')