from utils import run_every
from dotenv import load_dotenv
from urllib.parse import urlencode

import requests
import base64
import os

load_dotenv()

def request_auth_code():
    redirect_uri = os.environ.get('REDIRECT_URL')
    client_id    = os.environ.get('CLIENT_ID')
    query_params = { 
        'redirect_uri' : redirect_uri,
        'response_type' : 'code', 
        'client_id': client_id,
    }
    query_string = urlencode(query_params)
    return 'https://accounts.spotify.com/authorize?' + query_string

def authenticate_with_code(code):
    redirect_uri = os.environ.get('REDIRECT_URL')
    data = {
        'code': code, 
        'redirect_uri': redirect_uri,
        'grant_type': 'authorization_code'
    }
    response = spotify_auth_request(data)
    return SpotifyAuth(response.get('access_token'), response.get('refresh_token'))

class SpotifyAuth():
    def __init__(self, access_token, refresh_token):
        self.access_token = access_token
        self.refresh_token = refresh_token
        self.refresher()

    @run_every(5)
    def refresher(self):
        data = {
            'grant_type': 'refresh_token',
            'refresh_token': self.refresh_token
        }
        response = spotify_auth_request(data)
        self.access_token = response.get('access_token')       

def spotify_auth_request(data):
    response = requests.post('https://accounts.spotify.com/api/token', headers=__auth_request_headers(), data=data)  
    response.raise_for_status()
    return response.json()

def __client_header():
    client_id     = os.environ['CLIENT_ID']
    client_secret = os.environ['CLIENT_SECRET']

    client_auth = f"{client_id}:{client_secret}"
    
    client_auth_bytes = client_auth.encode('ascii')
    base64_bytes      = base64.b64encode(client_auth_bytes)
    
    return base64_bytes.decode('ascii')

def __auth_request_headers():
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': f'Basic {__client_header()}'
    }
    return headers


