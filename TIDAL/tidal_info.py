import tidalapi

session = tidalapi.Session()
session.login("USERNAME", "PASSWORD")

def get_currently_plazing():
    track = session.get_current_track()
    if track is not None:
        track_name = track.name
        artist_name = track.artist.name
        return track_name, artist_name
    return None, None

