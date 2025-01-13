// src/Recommendations.js
import React, { useState } from 'react';
import axios from 'axios';

const Recommendations = () => {
    const [mood, setMood] = useState('happy');
    const [recommendations, setRecommendations] = useState([]);

    const fetchRecommendations = async () => {
        try {
            const response = await axios.post('http://127.0.0.1:8000/recommend/', { mood });
            setRecommendations(response.data); // Assuming response.data is an array of recommendations
        } catch (error) {
            console.error('Error fetching recommendations:', error);
        }
    };

    return (
        <div>
            <h1>Game Recommendations</h1>
            <button onClick={fetchRecommendations}>Get Recommendations</button>
            <ul>
                {recommendations.map((game, index) => (
                    <li key={index}>{game.name}</li> // Adjust according to your JSON structure
                ))}
            </ul>
        </div>
    );
};

export default Recommendations;