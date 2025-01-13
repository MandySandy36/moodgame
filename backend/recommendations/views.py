from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import pandas as pd
import joblib
import random
import json
from django.http import JsonResponse

# Load the trained model and dataset
MODEL_PATH = "recommendations\ml_models\game_sales_model.pkl"
DATASET_PATH = "recommendations\ml_models\Video_Games_Sales_as_at_22_Dec_2016.csv"

# Load the model and dataset during server startup
loaded_model = joblib.load(MODEL_PATH)
original_data = pd.read_csv(DATASET_PATH)

# Define a mapping of moods to genres
mood_genre_mapping = {
    'happy': ['Action', 'Adventure', 'Sports'],
    'sad': ['Puzzle', 'Casual', 'Role-Playing'],
    'stressed': ['Strategy', 'Simulation', 'Combat'],
    "relaxed": ["Simulation", "Sandbox"],
    "excited": ["FPS", "Action"],
    "immersive": ["RPG", "Adventure"],
    "creative": ["Sandbox", "Strategy"],
    "competitive": ["Sports", "Racing"],
}

@csrf_exempt

def get_recommendations(request):
    """
    Recommend games dynamically based on the user's mood.

    Method: POST
    Body: { "mood": "happy", "num_recommendations": 5 }
    """
    try:
        # Parse request data
        if request.method != 'POST':
            return JsonResponse({'error': 'Invalid request method. Use POST.'}, status=400)

        body = json.loads(request.body)
        mood = body.get('mood', '').lower()
        num_recommendations = body.get('num_recommendations', 10)

        # Validate mood
        if not mood or mood not in mood_genre_mapping:
            return JsonResponse({'error': f"Invalid mood. Available moods: {', '.join(mood_genre_mapping.keys())}"}, status=400)

        # Filter recommendations based on the mood
        genres = mood_genre_mapping.get(mood, [])
        processed_data = original_data.copy()

        # Handle 'tbd' or other non-numeric values
        processed_data = processed_data.replace('tbd', None)

        # Convert numeric columns to appropriate types
        numeric_columns = ['Global_Sales', 'User_Score', 'Critic_Score']  # Add all relevant numeric columns
        for col in numeric_columns:
            if col in processed_data.columns:
                processed_data[col] = pd.to_numeric(processed_data[col], errors='coerce')  # Convert to numeric, setting invalid values to NaN

        # Drop rows with missing values in critical columns
        processed_data = processed_data.dropna(subset=['Global_Sales', 'Year_of_Release', 'Genre', 'Platform', 'Publisher'])

        # Filter by mood-specific genres
        filtered_recommendations = processed_data[processed_data['Genre'].isin(genres)]

        if filtered_recommendations.empty:
            return JsonResponse({'error': 'No games found for this mood. Try a different mood.'}, status=404)

        # Shuffle and limit recommendations
        randomized_recommendations = filtered_recommendations.sample(
            n=min(num_recommendations, len(filtered_recommendations)),
            random_state=random.randint(1, 10000)
        )

        # Prepare the output
        result = randomized_recommendations[
            ['Name', 'Platform', 'Year_of_Release', 'Genre', 'Publisher', 'Global_Sales']
        ].to_dict(orient='records')

        # Respond with recommendations
        return JsonResponse({'mood': mood, 'recommendations': result}, status=200)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
