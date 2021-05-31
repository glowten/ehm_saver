import discord
import json
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--fail_times", type=int, default=0, help="number of times it's failed")
parser.add_argument("--crash", action="store_true", help="crashed")
args = parser.parse_args()

with open(os.path.expanduser('~/Desktop/autosave_scripts/tokens.json'), 'r') as t:
    tokens_json = json.load(t)
    token = tokens_json['discord_token']
    nematode_channel = tokens_json['nematode_channel_id']

times_failed = args.fail_times
crashed = args.crash
intents = discord.Intents.default()
intents.typing = False
intents.presences = False
client = discord.Client(intents=intents)


async def alert_nematodes():
    print('alerting nematodes')
    channel = client.get_channel(int(nematode_channel))
    everyone = channel.guild.default_role
    if times_failed == 10:
        await channel.send(everyone)
    # await channel.send('this is just a test sorry everyone im doing the yeet alert thing')
    if crashed:
        await channel.send(f'game probably crashed')
    else:
        await channel.send(f'save failed {str(times_failed)} times ethernet needs to be yoted')
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