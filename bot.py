import discord
import json
import os

with open(os.path.expanduser('~/Desktop/autosave_scripts/tokens.json'), 'r') as t:
    tokens_json = json.load(t)
    token = tokens_json['discord_token']
    nematode_channel = tokens_json['nematode_channel_id']

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
client = discord.Client(intents=intents)


async def alert_nematodes():
    print('alerting nematodes')
    channel = client.get_channel(int(nematode_channel))
    everyone = channel.guild.default_role
    await channel.send(everyone)
    # await channel.send('this is just a test sorry everyone im doing the yeet alert thing')
    await channel.send(f'save failed 4 times ethernet needs to be yoted')
    await client.close()


@client.event
async def on_ready():
    for guild in client.guilds:
        print(
            f"{client.user} is connected to the following servers:\n"
            f"{guild.name}(id: {guild.id})"
        )
    await alert_nematodes()

client.run(token)