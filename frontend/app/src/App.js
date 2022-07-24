import "./App.css";
import React, { useState } from "react";
import spongebob from "./characters/spongebob.jpeg";
import patrick from "./characters/patrick.png";
import ArrowBackIosIcon from "@mui/icons-material/ArrowBackIos";
import ArrowForwardIosIcon from "@mui/icons-material/ArrowForwardIos";
import TextField from "@mui/material/TextField";

function App() {
  const character = [patrick, spongebob];
  const buttons = [
    "Spotify_button",
    "Guest_button",
    "Spotify_button_hidden",
    "Guest_button_hidden",
  ];
  const [count, setCount] = useState(0);
  const [num, setNum] = useState(0);
  return (
    <div className="App">
      <header className="App-header">
        <div className="Header-text"> Silver Dollop </div>
      </header>
      <body>
        <div className="Chracter-content">
          <button className="Arrow_button" onClick={() => setCount(count - 1)}>
            <ArrowBackIosIcon />
          </button>
          <img
            src={character[Math.abs(count % character.length)]}
            className="App-logo"
            alt="logo"
          />
          <button className="Arrow_button" onClick={() => setCount(count + 1)}>
            <ArrowForwardIosIcon />
          </button>
        </div>
        <div className="Text-box">
          <form>
            <label>
              <input
                className="Text-input"
                type="text"
                name="Nickname"
                placeholder="Nickname"
                color="white"
              />
            </label>
          </form>
        </div>
        <div className="App-body">
          <button className="Play_button">Play</button>
          <button className="Host_button" onClick={() => setNum(num + 1)}>
            Host
          </button>
          <button className={buttons[(2 * num) % buttons.length]}>
            Log in with Spotify
          </button>
          <button className={buttons[(1 + 2 * num) % buttons.length]}>
            Continue as Guest
          </button>
        </div>
      </body>
    </div>
  );
}

export default App;
