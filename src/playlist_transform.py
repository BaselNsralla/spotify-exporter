


def __track_as_text(item):
    artist_sep = "and "
    return {
        'content_title': f"{item['title']} - {artist_sep.join(item['artist_names'])}",
        'is_song': item['type'] == 'track'  
    }


def transform_playlists_tracks(playlists):
    """ Transfomr playlist songs """
    result = []
    for playlist in playlists:
        result.append({
            'title': playlist['name'], 
            'tracks': list(map(__track_as_text, playlist['tracks'])) 
        })
    return result

