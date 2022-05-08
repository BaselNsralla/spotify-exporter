
from spotify.client import SpotifyClient
import json

def __tracks(tracks):
    result = []
    tracks_with_content = filter(lambda t: t['track'] is not None, tracks)
    for element in tracks_with_content:
        track = element['track']
        #import json
        #print(json.dumps(track, indent=4))
        # for each track we extract the artists and their songs
        artist_names = list(map(lambda artist: artist['name'], track['album']['artists']))
        track_name   = track['name']
        result.append((track_name, artist_names))
    return result


def extract_playlists_tracks(access_token):
    client = SpotifyClient(access_token)
    playlists = client.playlists()
    for playlist in playlists:
        raw_tracks = client.tracks(playlist_url=playlist['tracks']['href'])
        

        yield {'name': playlist['name'], 'tracks': __tracks(raw_tracks)}


    #     print(json.dumps(playlist, indent=4))
    # """ For each playlist extract songs via api calls """ 
    # return ["hi-ok"]