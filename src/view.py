
def playlist_to_html(playlists):
    content = r""
    for playlist in playlists:
        content += "<h2>"+playlist['name']+"</h2>"
        content += r"</br>".join(playlist['tracks'])
        content += r"</br>=====================</br>"

    return content