import lyricsgenius

genius = lyricsgenius.Genius('ACCESS_TOKEN')

def get_lyrics(song_title, artist_name):
    song = genius.search_song(song_title, artist_name)
    return song.lyrics if song else None