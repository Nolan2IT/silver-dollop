from util import url_to_id, auth, get_playlist, get_previews, download, clear
# File for testing functions in util.py

url = 'https://open.spotify.com/playlist/37i9dQZF1DX76t638V6CA8'
token = auth()
playlist_id = url_to_id(url)
playlist = get_playlist(token, playlist_id)

previews = get_previews(playlist)

clear('songs')
download(previews, 'songs')




