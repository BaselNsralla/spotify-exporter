# Spotify YTMusic 
Export Spotify playlists to Youtube

### Endpoints

| Endpoint | Description |
| ---      | --- |
| `/spotify/login` | Login to Spotify |
| `'/spotify/export/<user>'` | Export playlists of user |


## YoutubeMusic API
This program uses ytmusicapi as a dependency to export to interact with youtube music API.

In order to authenticate please follow the guide provide by the library [here](https://ytmusicapi.readthedocs.io/en/latest/setup.html#authenticated-requests). `hearder_raw.json` and `headers.json` with empty cookie value examples are included. Paste the cookies in their corresponding file.

## How to Run
* `pip install -r requirements.txt``
* `make run`

