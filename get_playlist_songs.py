from dotenv import load_dotenv
import os
import requests
import json
import pandas as pd

load_dotenv()
CLIENT_ID = os.environ.get('SPOTIFY_CLIENT_ID')
CLIENT_SECRET = os.environ.get('SPOTIFY_CLIENT_SECRET')

AUTH_URL = 'https://accounts.spotify.com/api/token'

username='kevinburnham'
auth_response = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
})

# convert the response to JSON
auth_response_data = auth_response.json()

# save the access token
access_token = auth_response_data['access_token']


headers = {
    'Authorization': 'Bearer {token}'.format(token=access_token)
}


playlist_url = f'https://api.spotify.com/v1/users/{username}/playlists?limit=50&offset=0'


res = requests.get(url = playlist_url, headers=headers)
r = res.json()
playlists = pd.DataFrame(r['items'])


## now need to get the songs for each playlist, probably can ignore a few


httc = playlists[playlists.name.str.contains('httc')][['name', 'id']]
httc

playlist_id = '2NBoVDfu9WgyEZ3KvIs94j'

tracks_url = f'https://api.spotify.com/v1/playlists/{playlist_id}/tracks'

tracks_res = requests.get(url = tracks_url, headers=headers)


tracks_json = tracks_res.json()

tracks_df = pd.DataFrame(tracks_json['items'])

tracks_df.track[0].keys()


# convert keys to list
# df = pd.DataFrame(df['column1'].values.tolist(), index=df.index).fillna(0).astype(int)


tracks = pd.DataFrame(tracks_df['track'].values.tolist(), index=tracks_df.index).fillna('').astype(str)
tracks_df['track_name'] =  tracks.name

tracks_df['album_name'] = [dict(eval(x))['name'] for x in tracks.album]

tracks_df['first_artist'] = [list(eval(x))[0]['name'] for x in tracks.artists]

tracks_df[['track_name', 'first_artist', 'album_name']]

for row in tracks_df[['track_name', 'first_artist', 'album_name']].to_dict(orient="records"):
    print(row['track_name'], '-', row['first_artist'])
# i want a function that given a playlist id (and name) returns a dataframe with 'playlist_name', 'track_name', 'first_artist', 'album_name'


def get_playlist_songs(id: str, playlists: pd.DataFrame, headers: dict):
    # get the name from the df
    playlist_name = playlists[playlists['id'] == id]['name'].values[0]

    tracks_url = f'https://api.spotify.com/v1/playlists/{id}/tracks'

    tracks_res = requests.get(url = tracks_url, headers=headers)
    tracks_json = tracks_res.json()
    tracks_df = pd.DataFrame(tracks_json['items'])

    tracks = pd.DataFrame(tracks_df['track'].values.tolist(), index=tracks_df.index).fillna('').astype(str)
    tracks_df['track_name'] =  tracks.name
    tracks_df['track_id'] = [dict(eval(x))['id'] for x in tracks.album]

    tracks_df['album_name'] = [dict(eval(x))['name'] for x in tracks.album]


    tracks_df['first_artist'] = [list(eval(x))[0]['name'] for x in tracks.artists]

    tracks_df['playlist_name'] = playlist_name

    return(tracks_df[['track_name', 'track_id', 'first_artist', 'album_name', 'playlist_name']])

playlist_id = list(httc.id)[0]

get_playlist_songs(playlist_id, playlists = httc, headers = headers)


all_tracks = [get_playlist_songs(x, httc, headers) for x in httc.id]

all_tracks[31]






playlists[playlists.id == playlist_id]['name'].values[0]

all_tracks_df = pd.concat(all_tracks)


all_tracks_df.playlist_name.value_counts()


all_tracks_df[~all_tracks_df.playlist_name.isin(ignore)].to_csv('~/spotify_playlist_tracks.csv')




playlist_name = playlists[playlists['id'] == playlist_id]['name'].values[0]

tracks_url = f'https://api.spotify.com/v1/playlists/{playlist_id}/tracks'

tracks_res = requests.get(url = tracks_url, headers=headers)
tracks_json = tracks_res.json()
tracks_df = pd.DataFrame(tracks_json['items'])


tracks_df.track[0]['id']



# create playlist


res = requests.post(url = playlist_url, headers=headers,  data = {"name": "httc-all", "description": "playlist combining all songs in httc playlists", "public": "true"})


res.json()