import requests
import base64
from secrets import clientId, clientSecret
import json

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
    url = f"https://api.spotify.com/v1/playlists/{playlist_id}"
    headers = {'Authorization': f'Bearer {token}'}
    print("Requesting playlist...")
    r = requests.get(url, headers=headers)
    return r.json()


