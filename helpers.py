import pandas as pd
import spotipy
import json
import os
from spotipy.oauth2 import SpotifyOAuth
import requests


def get_httc_playlists(sp: spotipy.client.Spotify) -> pd.DataFrame:
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

    return(pd.Series([album_name, href, id, uri, artist], index = ['album_name', 'href', 'id', 'uri', 'artist']))

def get_playlist_tracks(sp: spotipy.client.Spotify, username: str, playlist_id: str) -> pd.DataFrame: 
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
def update_httc_all(sp: spotipy.client.Spotify, httc_all_id: str, slack_webhook: str) -> None:
    username = sp.current_user()['id']

    # get the current list of tracks on httc-all
    httc_all_tracks_df = get_playlist_tracks(sp=sp, username=username, playlist_id=httc_all_id)
    httc_all_track_uris = list(httc_all_tracks_df.uri)

    msg = f'there are currently {len(httc_all_track_uris)} tracks on httc-all'
    print(msg)
    slack_message(slack_webhook, msg)

    # get list of all songs on all httc playlists
    httc_playlists = get_httc_playlists(sp)
    all_songs_list = [pd.DataFrame(get_playlist_tracks(sp, username, track_id)) for track_id in httc_playlists.id]
    all_songs_df = pd.concat(all_songs_list)
    all_tracks = list(set(all_songs_df.uri))

    msg = f'there are {len(httc_playlists)} monthly httc playlists with a total of {len(all_songs_df)} tracks ({len(all_tracks)} are unique)'
    print(msg)
    slack_message(slack_webhook, msg)

    new_tracks = [at for at in all_tracks if at not in list(httc_all_track_uris)]


    if len(new_tracks) > 0:

        msg = f'adding {len(new_tracks)} new tracks to httc-all'
        print(msg)
        slack_message(slack_webhook, msg)

        # this adds all these new tracks to httc-all, we can only add 100 at a time
        while new_tracks:
            results = spotipy.user_playlist_add_tracks(user=username, playlist_id=httc_all_id, tracks=new_tracks[:100], position=None)
            new_tracks = new_tracks[100:]
    else:
        msg = 'No new tracks to add'
        print(msg)
        slack_message(slack_webhook, msg)

    print('Done')
    slack_message(slack_webhook, 'Done')
    return(None)


def slack_message(webhook, message):
  headers = {'Content-type':'application/json'}
  data = {'text': message}
  res = requests.post(url=webhook, headers=headers, data=json.dumps(data))