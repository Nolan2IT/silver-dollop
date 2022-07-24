import requests
import base64
from secrets import clientId, clientSecret
import json
import wget
import os
import glob
import shutil

def url_to_id(url: str) -> str:
    print("Getting playlist id...")
    return url.split('/')[-1]

def auth() -> str:
    url = "https://accounts.spotify.com/api/token"
    headers = {}
    data = {}

    print("Encoding message...")
    message = f"{clientId}:{clientSecret}"
    messageBytes = message.encode("ascii")
    base64Bytes = base64.b64encode(messageBytes)
    base64Message = base64Bytes.decode("ascii")

    headers['Authorization'] = f"Basic {base64Message}"
    data['grant_type'] = "client_credentials"

    print("Making request...")
    r = requests.post(url, headers=headers, data=data)
    token = r.json()['access_token']
    return token

def get_playlist(token: str, playlist_id: str) -> dict:
    url = f"https://api.spotify.com/v1/playlists/{playlist_id}?market=US"
    headers = {'Authorization': f'Bearer {token}'}
    print("Requesting playlist...")
    r = requests.get(url, headers=headers)
    return r.json()

def get_song_data(playlist: dict) -> list:
    print("Getting previews...")
    tracks = playlist['tracks']['items']
    data = []
    for track in tracks:
        name = track['track']['name']
        artist = track['track']['artists'][0]['name']
        preview = track['track']['preview_url']
        if preview is not None:
            data.append((name, artist, preview))
    return data

# No longer used
def download(previews: list, path: str) -> None:
    for name, preview in previews:
        wget.download(preview, f'{path}/{name}.mp3')
    print("Done downloading!")

def clear(path: str) -> None:
    for file in glob.glob(f'{path}/*'):
        os.remove(file)
    print("Cleared!")

def delete(path: str) -> None:
    shutil.rmtree(path)
    print("Deleted!")
    
