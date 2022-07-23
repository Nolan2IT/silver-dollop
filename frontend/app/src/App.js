import "./App.css";
import React, { useState } from "react";
import logo from "./logo.svg";
import spotify_logo from "./images/spotify_logo.png";
import spongebob from "./characters/spongebob.jpeg";
import patrick from "./characters/patrick.png";
import ArrowBackIosIcon from "@mui/icons-material/ArrowBackIos";
import ArrowForwardIosIcon from "@mui/icons-material/ArrowForwardIos";

function App() {
  const character = [patrick, spongebob];
  const [count, setCount] = useState(0);
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
        <div className="App-body">
          <button className="Play_button">Play</button>
          <button className="Host_button">Host</button>
        </div>
      </body>
    </div>
  );
}

export default App;
