from flask import Flask, redirect, request, make_response
import requests 

import os
from spotify.auth import authenticate_with_code, request_auth_code, refresh_token

app = Flask(__name__)


@app.route('/spotify/login')
def spotify_login():

    url = request_auth_code()
    return redirect(
        url,
    )

@app.route('/spotify/auth_callback')
def spotify_callback():
    refresh_token = authenticate_with_code(
        request.args.get('code'),
    )
    resp = make_response('Logged in!')
    resp.set_cookie('refresh_token', refresh_token)
    return resp


@app.route('/spotify/test')
def spotify_test():
    _refresh_token = request.cookies.get('refresh_token')
    access_token = refresh_token(_refresh_token)
    return f"access token: ${access_token}"
    
@app.route('/spotify/export/<user>')
def export(user):
    from playlist_extract   import extract_playlists_tracks
    from playlist_transform import transform_playlists_tracks
    from playlist_export    import export_playlist_tracks
    from view               import playlist_to_html
    #user = request.view_args['user']
    _refresh_token = request.cookies.get('refresh_token')
    access_token   = refresh_token(_refresh_token)
    ext_playlists  = extract_playlists_tracks(access_token, user=user)
    playlists      = transform_playlists_tracks(ext_playlists)

    for playlist in playlists:
        print("Exporting: ", playlist['title'])
        export_playlist_tracks(playlist)

    return playlist_to_html(playlists)


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 3000.
    port = int(os.environ.get('SPOTIFY_YTMUSIC_PORT', 3000))
    app.run(host='localhost', port=port)