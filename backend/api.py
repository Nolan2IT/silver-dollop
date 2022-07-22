from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from util import url_to_id, auth, get_playlist, get_previews, download, clear
import os
import uvicorn

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.post("/start_game/{id}")
async def start_game(request: Request, id: str):
    playlist_url = request.headers.get('playlist_url')
    token = auth()
    playlist_id = url_to_id(playlist_url)
    playlist = get_playlist(token, playlist_id)
    previews = get_previews(playlist)
    if not os.path.exists(f'playlists/{playlist_id}'):
        os.mkdir(f'playlists/{playlist_id}')
        download(previews, f'playlists/{playlist_id}')
    return {"status": "ok", "path": "playlists/" + playlist_id}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port="5000")
