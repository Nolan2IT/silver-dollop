import "./App.css";
import React from "react";
import logo from "./logo.svg";
import spotify_logo from "./images/spotify_logo.png";

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <div className="Header-text"> Silver Dollop </div>
      </header>
      <body>
        <img src={spotify_logo} className="App-logo" alt="logo" />
        <div className="App-body">
          <button className="Spotify_button">Login with Spotify</button>
          <button className="Guest_button">Play as Guest</button>
        </div>
      </body>
    </div>
  );
}

export default App;
