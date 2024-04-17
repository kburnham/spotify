import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd
import json
import os

from helpers import update_httc_all, get_httc_playlists, get_playlist_tracks, get_track_data, slack_message

SLACK_WEBHOOK = os.environ['SLACK_WEBHOOK']


def run_all(request): 
  
  secret_string = os.environ['spotify_creds']
  secret_dict = json.loads(secret_string)

  


  os.environ['SPOTIPY_CLIENT_ID'] = secret_dict['SPOTIFY_CLIENT_ID']
  os.environ['SPOTIPY_CLIENT_SECRET'] = secret_dict['SPOTIFY_CLIENT_SECRET']
  os.environ['SPOTIPY_REDIRECT_URI'] = 'http://localhost:8080'

  # load_dotenv()

  scope = "playlist-modify-public"

  sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

  sp_user = sp.current_user()
  username = sp_user['id']
  playlist_name = 'httc-all-songs'

  # this code creates the playlist if it doesn't already exist
  # httc_all_metadata = sp.user_playlist_create(user = username, name=playlist_name)
  # httc_all_id = httc_all_metadata['id']

  httc_all_id = '2DJbIZtFfYuHEYI4vjxau6'


  update_httc_all(sp=sp, httc_all_id=httc_all_id, slack_webhook=SLACK_WEBHOOK)
  return('ok')