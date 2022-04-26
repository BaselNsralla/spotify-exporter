import requests
from utils import paginated_request, flat_accumulate

class SpotifyClient:
    def __init__(self, access_token):
        self.access_token = access_token
        self.headers = {
            'Authorization': f'Bearer {self.access_token}',
            'Content-Type': 'application/json'
        }

    @flat_accumulate
    def __collect_playlists(self, paginator):
        #print("SSADASDASD", paginator)
        result = requests.get(next(paginator), headers=self.headers).json()
        playlists = result['items']
        return (playlists, result['next'])

    def playlists(self):
        paginator = paginated_request('https://api.spotify.com/v1/users/zilkvey/playlists?offset={}&limit={}', start=0, step=20)
        return self.__collect_playlists(paginator())