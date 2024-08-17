import spotipy
from spotipy.outh2 import SpotifyOAuth

sp = spotify.Spotify(auth_manager=SpotifyOAuth(
    client_id='CLIENT_ID',
    client_secret='CLIENT_SECRET',
    redirect_uri='REDIRECT_URI',
    scope='USR_READ_PLAYBACK_STATE'
))


def get_currently_playing():
    current_track = sp.current_playback()
    if current_track is not None and current_track['is_playing']:
        track_id = current_track['item']['id']
        tarck_name = current_track['item']['name']
        artist_name = current_track['item']['artist'][0]['name']
        return track_id, tarck_name, artist_name
    return None, None, None
