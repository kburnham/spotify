
import spotipy
import pandas as pd
from spotipy.oauth2 import SpotifyOAuth
import json
import os
from google.cloud import secretmanager
from pprint import pprint


client = secretmanager.SecretManagerServiceClient()
secret_name = "spotify_creds"
project_id = "kb-data-391220"
request = {"name": f"projects/{project_id}/secrets/{secret_name}/versions/latest"}
response = client.access_secret_version(request)
secret_string = response.payload.data.decode("UTF-8")
secret_dict = json.loads(secret_string)

os.environ['SPOTIPY_CLIENT_ID'] = secret_dict['SPOTIFY_CLIENT_ID']
os.environ['SPOTIPY_CLIENT_SECRET'] = secret_dict['SPOTIFY_CLIENT_SECRET']
os.environ['SPOTIPY_REDIRECT_URI'] = 'http://localhost:8080'

scope = "playlist-modify-public"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, cache_handler=spotipy.CacheFileHandler(cache_path="tmp/.cache")))

sp_user = sp.current_user()
username = sp_user['id']
playlist_name = 'France - Top 50'
results = sp.search(q='playlist:' + playlist_name, type='playlist')

results['playlists']['items'][0]