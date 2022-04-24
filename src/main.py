from flask import Flask, redirect, request, make_response
import requests 

import os
from spotify_auth import authenticate_with_code, request_auth_code, refresh_token

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
    

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('SPOTIFY_YTMUSIC_PORT', 3000))
    app.run(host='localhost', port=port)