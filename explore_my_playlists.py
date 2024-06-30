
import spotipy
import pandas as pd
from spotipy.oauth2 import SpotifyOAuth
import json
import os
from pprint import pprint
from dotenv import load_dotenv


load_dotenv()
scope = "playlist-modify-public"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, cache_handler=spotipy.CacheFileHandler(cache_path="tmp/.cache")))
sp_user = sp.current_user()
username = sp_user['id']
