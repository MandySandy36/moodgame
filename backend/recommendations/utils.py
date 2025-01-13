# recommendations/utils.py
import pandas as pd
import joblib
import random

# Mood-to-genre mapping
mood_genre_mapping = {
    'happy': ['Action', 'Adventure', 'Sports'],
    'sad': ['Puzzle', 'Casual', 'Role-Playing'],
    'stressed': ['Strategy', 'Simulation', 'Combat'],
    "relaxed": ["simulation", "sandbox"],
    "excited": ["fps", "action"],
    "immersive": ["rpg", "adventure"],
    "creative": ["sandbox", "strategy"],
    "competitive": ["sports", "racing"],
}

# Load the model
def load_model():
    model_path = "recommendations/ml_models/game_sales_model.pkl"
    return joblib.load(model_path)

# Recommendation function
def recommend_games_by_mood(mood, X_test, original_data, processed_data, loaded_model, num_recommendations=10):
    genres = mood_genre_mapping.get(mood.lower(), [])
    genre_cols = [col for col in processed_data.columns if any(genre in col.lower() for genre in genres)]

    recommendations = pd.DataFrame(X_test, columns=processed_data.columns)
    recommendations['Predicted_Sales'] = loaded_model.predict(X_test)
    recommendations['Name'] = original_data['Name'].values[:len(recommendations)]

    if genres:
        filtered_recommendations = recommendations[recommendations[genre_cols].sum(axis=1) > 0]
    else:
        filtered_recommendations = recommendations

    if filtered_recommendations.empty:
        filtered_recommendations = recommendations

    randomized_recommendations = filtered_recommendations.sample(
        n=min(num_recommendations, len(filtered_recommendations)), 
        random_state=random.randint(1, 10000)
    )

    return randomized_recommendations[['Name', 'Predicted_Sales']]
