
import spotipy
import pandas as pd
from spotipy.oauth2 import SpotifyOAuth
import json
import os
from pprint import pprint
from dotenv import load_dotenv

# ---- SET THESE VARIABLES ----
NEW_PLAYLIST_NAME = 'primavera_sound_2024'
ARTIST_SOURCE_FILE = 'artist_lists/primavera_sound_2024.txt'
TRACKS_PER_ARTIST = 5
# -----------------------------

load_dotenv()
scope = "playlist-modify-public"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, cache_handler=spotipy.CacheFileHandler(cache_path="tmp/.cache")))
sp_user = sp.current_user()
username = sp_user['id']


playlist_metadata = sp.user_playlist_create(user = username, name=NEW_PLAYLIST_NAME)


new_playlist_id = playlist_metadata['id'] 


with open(ARTIST_SOURCE_FILE) as file:
    artists = [line.rstrip() for line in file]



def search_artist_name(artist_name: str, sp: spotipy.client.Spotify) -> str:
    results = sp.search(q='artist:' + artist_name, type='artist')
    items = results['artists']['items']
    if items == []:
        return(None)
    artist_id = items[0]['id']
    artist_uri = f'spotify:artist:{artist_id}'
    return(artist_uri)


def get_artist_top_tracks_uris(artist_uri: str, count:int, sp: spotipy.client.Spotify) -> str:
    top_tracks = sp.artist_top_tracks(artist_uri)
    top_tracks_df = pd.DataFrame(top_tracks['tracks'])
    if len(top_tracks) == 0:
        return(None)
    top_tracks_uris = list(top_tracks_df.uri)[0:count]
    return(top_tracks_uris)



track_count = TRACKS_PER_ARTIST
already_done = list()
fails = list()
for artist in artists:
    print(artist)
    if artist in already_done:
        print(f'{artist} already done.')
        continue
    if artist in fails:
        print(f'{artist} already failed')
        continue
    artist_uri = search_artist_name(artist, sp)
    print(artist_uri)
    try: 
        top_tracks = get_artist_top_tracks_uris(artist_uri, track_count, sp)
    except:
        print(f'no tracks found for {artist}')
        fails.append(artist)
        continue
    print(f'length of top tracks: {len(top_tracks)}')
    try: 
        sp.user_playlist_add_tracks(user=username, playlist_id=new_playlist_id, tracks=top_tracks, position=None)
        print(f'{len(top_tracks)} tracks added to playlist for {artist}')
        already_done.append(artist)
    except:
        print(f'adding tracks for {artist} failed')
        fails.append(artist)
