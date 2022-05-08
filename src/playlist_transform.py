


def __track_as_text(item):
    artist_sep = "and "
    return f"{item[0]} - {artist_sep.join(item[1])}"


def transform_playlists_tracks(playlists):
    """ Transfomr playlist songs """
    result = []
    for playlist in playlists:
        result.append({
            'name': playlist['name'], 
            'tracks': list(map(__track_as_text, playlist['tracks'])) 
        })
    return result

