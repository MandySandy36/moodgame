import React, { useState } from "react";
import axios from "axios";
import './App.css'; // Import the CSS file

function App() {
  const [mood, setMood] = useState("");
  const [recommendations, setRecommendations] = useState([]);
  const [error, setError] = useState("");

  const moods = [
    { name: "happy", color: "#FFD300" },
    { name: "sad", color: "#1E90FF" },
    { name: "stressed", color: "#FF4500" },
    { name: "relaxed", color: "#32CD32" },
    { name: "excited", color: "#FF1493" },
    { name: "immersive", color: "#9400D3" },
    { name: "creative", color: "#FFA500" },
    { name: "competitive", color: "#DC143C" },
  ];

  const fetchRecommendations = async () => {
    try {
      setError("");
      const response = await axios.post("http://127.0.0.1:8000/api/recommend/", {
        mood: mood,
        num_recommendations: 10,
      });
      setRecommendations(response.data.recommendations);
    } catch (err) {
      setRecommendations([]);
      setError(err.response?.data?.error || "An error occurred.");
    }
  };

  return (
    <div className="app-container">
      <div className="main-container">
        <div className="header-container">
          <h1>Mood-Based Game Recommendation System</h1>
        </div>

        <div className="mood-container">
          <p>Select a mood to get game recommendations:-</p>
          {moods.map((m) => (
            <button
              key={m.name}
              onClick={() => setMood(m.name)}
              className={`mood-button ${mood === m.name ? "selected" : ""}`}
              style={{ color: m.color }}
            >
              {m.name.charAt(0).toUpperCase() + m.name.slice(1)}
            </button>
          ))}
        </div>
          
        <button
          onClick={fetchRecommendations}
          className="get-recommendations-button"
          disabled={!mood}
        >
          Get Recommendations
        </button>

        {error && <p className="error-message">Error: {error}</p>}

        <div className="recommendations-container">
          <h2>Recommendations :-</h2>
          {recommendations.length > 0 ? (
            <ol className="recommendations-list">
              {recommendations.map((game, index) => (
                <li key={index}>
                  <strong>{game.Name}</strong> ({game.Genre}) - {game.Platform} (
                  {game.Year_of_Release})
                </li>
              ))}
            </ol>
          ) : (
            <p>No recommendations available. Select a mood and try again.</p>
          )}
        </div>

        <div className="footer">
          &copy; {new Date().getFullYear()} 
          <a href="https://www.linkedin.com/in/mehatabsanadi/"><strong>Mehatab Sanadi</strong></a>  
          & 
          <a href="https://www.linkedin.com/in/pranjaldhumal/"><strong>Pranjal Dhumal</strong></a>. 
          All Rights Reserved.
        </div>
      </div>
    </div>
  );
}

export default App;
