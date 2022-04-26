
from spotify.client import SpotifyClient
import json

def playlists_to_songs(access_token):
    client = SpotifyClient(access_token)
    playlists = client.playlists()
    for playlist in playlists:
        print(json.dumps(playlist, indent=4))
    """ For each playlist extract songs via api calls """ 
    return ["hi-ok"]