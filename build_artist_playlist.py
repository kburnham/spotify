

# a script that will take a list of artists and build a playlist with it


# components
# create a playlist with the provided name
# search and artist name and get the id
# get the top tracks for the artist


# future
# remove tracks for a given list of artists


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
new_playlist_name = 'swsx_artists_2024'

# httc_all_metadata = sp.user_playlist_create(user = username, name=new_playlist_name)
# httc_all_metadata['id'] 

sxsw_artists_2024_id = '4v2mTAFN4a8DdqKKPbmWob'


artist_name = 'Angelo Moore and the Brand New Step'

results = sp.search(q='artist:' + artist_name, type='artist')
items = results['artists']['items']



artist_id = items[0]['id']
artist_uri = f'spotify:artist:{artist_id}'


top_tracks = sp.artist_top_tracks(artist_uri)

pd.DataFrame(top_tracks)

top_tracks_df = pd.DataFrame(top_tracks['tracks'])
top_tracks_uris = list(top_tracks_df.uri)[0:5]


# add tracks to playlist
results = sp.user_playlist_add_tracks(user=username, playlist_id=sxsw_artists_2024_id, tracks=top_tracks_uris, position=None)


## load the sxsw artists list

with open('/Users/kevin/spotify/artist_lists/sxsw_2024_artists.txt') as file:
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

search_artist_name('Bob Dylan', sp)
get_artist_top_tracks_uris('spotify:artist:74ASZWbe4lXaubB36ztrGX', 5, sp)

## this block of code will iterate through the list of sxsw 2024 artists, search the name on Spotify,
# get a list of the top tracks for the artist 
# and add them to the playlist created above
track_count = 5
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
        sp.user_playlist_add_tracks(user=username, playlist_id=sxsw_artists_2024_id, tracks=top_tracks, position=None)
        print(f'{len(top_tracks)} tracks added to playlist for {artist}')
        already_done.append(artist)
    except:
        print(f'adding tracks for {artist} failed')
        fails.append(artist)




def add_artists_to_playlist(playlist_id: str, artists: list, sp: spotipy.client.Spotify, username: str, track_count: int = 5) -> dict:
    """given a list of artists, look them up and get the top `count` tracks for each artist on the list
        creates a spotify playlist for `username` and returns a dict with lists of successes and failures"""
    
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
            print(top_tracks)
            sp.user_playlist_add_tracks(user=username, playlist_id=playlist_id, tracks=top_tracks, position=None)
            print(f'{len(top_tracks)} tracks added to playlist for {artist}')
            already_done.append(artist)
        except:
            print(f'adding tracks for {artist} failed')
            fails.append(artist)
    print(f'Done. Tracks for {len(already_done)} artists were added to the playlist. {len(fails)} artists could not be added')
    return({'added': already_done, 'fails': fails})

        
artists = ['The Rolling Stones', 'Led Zeppelin', 'The Who', 'Jimi Hendrix', 'Rush']


pl_metadata = sp.user_playlist_create(user = username, name='Monsters of Rock')
pl_id = pl_metadata['id'] 

pl_id = '3imhN2NJFFgYaYVZtN8GuP'


pl_data = add_artists_to_playlist(playlist_id=pl_id, artists=artists, sp=sp, username=username)


search_artist_name('Jimi Hendrix', sp)


get_artist_top_tracks_uris(artist_uri='spotify:artist:776Uo845nYHJpNaStv1Ds4', count=5, sp=sp)