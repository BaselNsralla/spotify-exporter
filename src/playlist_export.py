from ytmusicapi import YTMusic
import json
import uuid



def __read_raw_header(filepath):
    with open(filepath, 'r') as file:
        data = file.read()
    return data

def export_playlist_tracks(playlist):
    ## TODO: Handle no search results
    YTMusic.setup(filepath="headers.json", headers_raw=__read_raw_header('headers_raw.json'))
    ytmusic = YTMusic('headers.json')
    playlist_name = playlist['title'] or str(uuid.uuid4())
    playlist_tracks = playlist['tracks']
    playlistId = ytmusic.create_playlist(playlist_name, "test description")
    
    for track in playlist_tracks:
        track_title = track['content_title']
        search_results = ytmusic.search(track_title) #**song_filter)
        results_with_video_id = list(filter(lambda x: 'videoId' in x, search_results))
        if len(results_with_video_id) == 0:
            json.dumps(search_results, indent=4)
            continue
        """results_with_video_id[0] is the top results"""
        top_result = results_with_video_id[0]
        ytmusic.add_playlist_items(playlistId, [top_result['videoId']])
