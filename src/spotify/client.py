import requests
from utils import paginated_request, page_accumulate, page_accumulate_auto


class SpotifyClient:
    def __init__(self, access_token):
        self.access_token = access_token
        self.headers = {
            'Authorization': f'Bearer {self.access_token}',
            'Content-Type': 'application/json'
        }


    @page_accumulate
    def __collect_by_key(self, paginator, key='items'):
        result = requests.get(next(paginator), headers=self.headers).json()
        items = result[key]
        return (items, result['next'])

    @page_accumulate_auto
    def __collect_by_key_auto(self, url, key='items'):
        result = requests.get(url, headers=self.headers).json()
        items = result[key]
        return (items, result['next'])

    def playlists(self):
        paginator = paginated_request('https://api.spotify.com/v1/users/zilkvey/playlists?offset={}&limit={}', start=0, step=20)
        return self.__collect_by_key(paginator=paginator())

    
    def tracks(self, playlist_url):
        return self.__collect_by_key_auto(url=playlist_url)