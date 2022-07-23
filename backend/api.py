from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from util import url_to_id, auth, get_playlist, get_previews, download, clear, delete
import os
import uvicorn

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
    previews = get_previews(playlist)
    os.mkdir(f"{game_path}/songs")
    download(previews, f"{game_path}/songs")
    return len(previews)

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

    f = open(f"{game_path}/info.py", "a")
    f.write(f"players = {players}\n")
    f.write(f"rounds = {rounds}\n")
    f.write(f"num_songs = {num_songs}\n")
    f.close()

    return Response(status_code=200, content=f"{game_id}")

@app.post("/delete_game")
async def delete_game(request: Request):
    game_id = request.headers.get('game_id')
    game_path = f"games/{game_id}"
    delete(game_path)

    return Response(status_code=200, content=f"{game_id}")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port="5000")