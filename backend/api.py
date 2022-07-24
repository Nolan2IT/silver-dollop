from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from util import url_to_id, auth, get_playlist, get_song_data, download, clear, delete
import os
import uvicorn
import json
import random
import wget

app = FastAPI()
origins = ["*"]

games = set()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_songs(playlist_url: str, game_path: str) -> int:
    token = auth()
    playlist_id = url_to_id(playlist_url)
    playlist = get_playlist(token, playlist_id)
    song_data = get_song_data(playlist)
    os.mkdir(f"{game_path}/songs")
    for name, artist, preview in song_data:
        os.mkdir(f"{game_path}/songs/{name}")
        info = {'name': name, 'artist': artist, 'path': f"{game_path}/songs/{name}/{name}.mp3"}
        f = open(f"{game_path}/songs/{name}/info.json", "w")
        json.dump(info, f)
        f.close()
        wget.download(preview, f'{game_path}/songs/{name}/{name}.mp3')
    
    return len(song_data)

def create_id():
    id = os.urandom(16).hex()
    while id in games:
        id = os.urandom(16).hex()
    games.add(id)
    return id 


@app.get("/health")
async def health():
    return {"status": "ok"}

@app.post("/create_game")
async def create_game(request: Request):
    playlist_url = request.headers.get('playlist_url')
    game_id = create_id()
    game_path = f"games/{game_id}"
    os.mkdir(game_path)
    num_songs = get_songs(playlist_url, game_path)

    players = request.headers.get('players')
    rounds = request.headers.get('rounds')

    f = open(f"{game_path}/info.json", "w+")
    data = {"players": players, "rounds": rounds, "num_songs": num_songs}
    json.dump(data, f)
    f.close()

    f = open(f"{game_path}/played_songs.json", "w+")
    json.dump([], f)
    f.close()

    return Response(status_code=200, content=f"{game_id}")

@app.post("/delete_game")
async def delete_game(request: Request):
    game_id = request.headers.get('game_id')
    game_path = f"games/{game_id}"
    delete(game_path)

    return Response(status_code=200, content=f"{game_id}")

@app.get("/game_info")
async def get_game_info(request: Request):
    game_id = request.headers.get('game_id')
    game_path = f"games/{game_id}"
    f = open(f"{game_path}/info.json", "r")
    data = json.load(f)
    f.close()
    return Response(status_code=200, content=f"{data}")

@app.get("/random_song")
async def get_random_song(request: Request):
    game_id = request.headers.get('game_id')
    game_path = f"games/{game_id}"
    try:
        f = open(f"{game_path}/played_songs.json", "r")
        played_songs = json.load(f)
        f.close()
    except:
        played_songs = []

    set_played_songs = set(played_songs)
    songs = os.listdir(f"{game_path}/songs")
    song = songs[int(len(songs) * random.random())]
    while song in set_played_songs:
        song = songs[int(len(songs) * random.random())]
    f = open(f"{game_path}/songs/{song}/info.json", "r")
    data = json.load(f)
    f.close()

    played_songs.append(data['name'])
    
    f = open(f"{game_path}/played_songs.json", "w+")
    json.dump(played_songs, f)
    f.close()

    return Response(status_code=200, content=f"{data}")



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port="5000")