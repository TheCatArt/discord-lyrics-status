import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

    while True:
        track_name, artist_name = get_current_playing()
        if track_name and artist_name:
            lyrics = get_lyrics(track_name, artist_name)
            if lyrics:
                lines = lyrics.split('\n')
                for line in lines:
                    await client.change_presence(activity=discord.Game(name=line))
                    await asyncio.sleep(10)
                await asyncio.sleep(5)
client.run('DISCORD_TOKEN')



