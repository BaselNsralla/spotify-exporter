
def playlist_to_html(playlists):
    content = r""
    for playlist in playlists:
        content += "<h2>"+playlist['title']+"</h2>"
        content += r"</br>".join([x['content_title'] for x in playlist['tracks']])
        content += r"</br>=====================</br>"

    return content