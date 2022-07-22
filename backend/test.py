from util import url_to_id, auth, get_playlist
# File for testing functions in util.py

url = 'https://open.spotify.com/playlist/37i9dQZF1DX76t638V6CA8'
token = auth()
playlist_id = url_to_id(url)
playlist = get_playlist(token, playlist_id)

print("From url " + url + " found songs:")
for item in playlist['tracks']['items']:
    print(item['track']['name'])


