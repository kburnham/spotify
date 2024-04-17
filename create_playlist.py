import spotipy
from spotipy.oauth2 import SpotifyOAuth
# import spotipy.util as util
# from dotenv import load_dotenv
import pandas as pd
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

# load_dotenv()

scope = "playlist-modify-public"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, cache_handler=spotipy.CacheFileHandler(cache_path="tmp/.cache")))

sp_user = sp.current_user()
username = sp_user['id']
playlist_name = 'httc-all-songs'

# this code creates the playlist if it doesn't already exist
# httc_all_metadata = sp.user_playlist_create(user = username, name=playlist_name)
# httc_all_id = httc_all_metadata['id']

httc_all_id = '2DJbIZtFfYuHEYI4vjxau6'



def get_httc_playlists() -> pd.DataFrame:
    pl = sp.current_user_playlists()
    pldf = pd.DataFrame(pl['items'])
    httc_pl = pldf[(pldf.name.str.contains('httc')) & (pldf.name != 'httc-all-songs')][['name', 'id']]
    return(httc_pl)

def get_track_data(td):
    """unpack the dictionary with the track data and return as a series"""
    album_name = td['album']['name']
    href = td['href']
    id = td['id']
    uri = td['uri']
    artist = td['artists'][0]['name']
    track_name = td['name']

    return(pd.Series([track_name, album_name, href, id, uri, artist], index = ['track_name', 'album_name', 'href', 'id', 'uri', 'artist']))

def get_playlist_tracks(username: str, playlist_id: str) -> pd.DataFrame: 
    results = sp.user_playlist_tracks(username, playlist_id)
    tracks = results['items']
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
    tracks_df = pd.DataFrame(tracks)


    track_data = tracks_df.apply(lambda row: get_track_data(row['track']), axis=1)
    track_data['playlist_id'] = playlist_id
    return(track_data)


# make a master function that does it all   
def update_httc_all(sp: spotipy.client.Spotify, httc_all_id: str) -> None:
    username = sp.current_user()['id']

    # get the current list of tracks on httc-all
    httc_all_tracks_df = get_playlist_tracks(username=username, playlist_id=httc_all_id)
    httc_all_track_uris = list(httc_all_tracks_df.uri)

    print(f'there are currently {len(httc_all_track_uris)} tracks on httc-all')

    # get list of all songs on all httc playlists
    httc_playlists = get_httc_playlists()
    all_songs_list = [pd.DataFrame(get_playlist_tracks(username, track_id)) for track_id in httc_playlists.id]
    all_songs_df = pd.concat(all_songs_list)
    all_tracks = list(set(all_songs_df.uri))

    print(f'there are {len(httc_playlists)} monthly httc playlists with a total of {len(all_songs_df)} tracks ({len(all_tracks)} are unique)')

    new_tracks = [at for at in all_tracks if at not in list(httc_all_track_uris)]


    if len(new_tracks) > 0:

        print(f'adding {len(new_tracks)} new tracks to httc-all')

        # this adds all these new tracks to httc-all, we can only add 100 at a time
        while new_tracks:
            results = sp.user_playlist_add_tracks(user=username, playlist_id=httc_all_id, tracks=new_tracks[:100], position=None)
            new_tracks = new_tracks[100:]
    else:
        print('No new tracks to add')

    print('Done')
    return(None)



httc_playlists = get_httc_playlists()


# dec_23_tracks = get_playlist_tracks(username, '2gUX6CIxEElKw3ceDVzi1a')
pl_id = '7ilDf01wx6Rc56hkp7MgsC' # httc-jan 2024

tracks = get_playlist_tracks(username, pl_id)

pprint(tracks[['track_name', 'artist']].to_string(index=False))


pprint(tracks.style.hide(axis='index'))

blankIndex=[''] * len(tracks)
tracks.index=blankIndex
print(tracks[['track_name', 'artist']])

# update_httc_all(sp=sp, httc_all_id=httc_all_id)

len(tracks)
for index, row in tracks.iterrows():
    print(f'{row["track_name"]} - {row["artist"]}')


results = sp.user_playlist_tracks(username, '2gUX6CIxEElKw3ceDVzi1a')

tracks = results['items']
tracks_df = pd.DataFrame(tracks)
tracks_df.columns

pprint(tracks_df.iloc[0]['track']['name'])




# DONE TODO refine to only add from the current list (or better yet anything after the last update?)
# TODO make a google cloud function that runs this regularly (or when I visit a URL)
# TODO have cloud function report what it's doing to slack
# TODO 
    






