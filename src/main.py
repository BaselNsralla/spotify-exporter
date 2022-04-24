from flask import Flask, redirect, request
import requests 

import os
from spotify_auth import authenticate_with_code, SpotifyAuth, request_auth_code

app = Flask(__name__)


@app.route('/spotify/login')
def spotify_login():

    url = request_auth_code()
    return redirect(
        url,
    )

    #return 'Hello, World!'
@app.route('/spotify/auth_callback')
def spotify_callback():
    spotify_auth = authenticate_with_code(
        request.args.get('code'),
    )
    return spotify_auth.access_token

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('SPOTIFY_YTMUSIC_PORT', 3000))
    app.run(host='localhost', port=port)