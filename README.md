# Mood-Based Game Recommendation System 🎮

This project is an AI/ML-powered Mood-Based Game Recommendation System that suggests games to users based on their mood. It leverages a machine learning model trained using Random Forest, with a Django backend and a React frontend to deliver an interactive and seamless user experience.

## Features ✨
- **Mood-Based Recommendations**: Users can select a mood (e.g., Happy, Sad, Relaxed) to get personalized game recommendations.
- **Interactive UI**: A modern, responsive frontend built using React with a neon-themed design.
- **Backend API**: A robust backend powered by Django to handle recommendations and data processing.
- **AI-Powered Suggestions**: The recommendation engine is powered by a Random Forest model trained on game-related data.
- **REST API**: Built using Django REST Framework for smooth communication between frontend and backend.

---

## Tech Stack 🛠️

### Machine Learning
- **Algorithm**: Random Forest
- **Training Data**: A dataset of games with features like genre, platform, and release year.

### Backend
- **Framework**: Django
- **API**: Django REST Framework
- **Language**: Python

### Frontend
- **Library**: React
- **Styling**: Custom CSS with a neon gaming theme

---

## Installation & Setup 🚀

### Prerequisites
Ensure you have the following installed:
- Python 3.8+
- Node.js 16+
- npm or yarn
- pip (Python package manager)

### Backend Setup
1. Clone the repository and navigate to the backend directory:
   ```bash
   git clone https://github.com/your-username/mood-game-recommendation.git
   cd mood-game-recommendation/backend

2. Install dependencies:   
   ```bash
   pip install -r requirements.txt

3. Apply migrations and start the server:
   ```bash
   python manage.py migrate
   python manage.py runserver

### Frontend Setup
1. Navigate to the frontend directory:
   ```bash
   cd ../frontend

2. Install dependencies:   
   ```bash
   npm install

3. npm start:
   ```bash
   python manage.py migrate
   python manage.py runserver

---
## Usage 🎯
1. Open the frontend in your browser at http://localhost:3000.
2. Select a mood from the list of buttons (e.g., Happy, Relaxed).
3. Click "Get Recommendations" to receive a list of games tailored to your mood.
---
## Folder Structure 📂

mood-game-recommendation/

├── backend/          
│   ├── api/         
│   ├── models/       
│   └── requirements.txt  
├── frontend/        
│   ├── public/       
│   ├── src/          
│   └── package.json  
└── README.md         
  
---
## Future Enhancements 🚀
* Add more moods and refine the recommendation algorithm.
* Integrate a database to store user preferences and feedback.
* Add user authentication for a personalized experience.
---
## Authors ✍️
* Mehatab Sanadi
* Pranjal Dhumal
---
## License 📄
This project is licensed under the MIT License and the BSD 3-Clause License. See the LICENSE file for details.

---
## Acknowledgments 🙌
* Dataset: https://www.kaggle.com/code/arthurtok/the-console-wars-ps-vs-xbox-vs-wii/input
* frontend background image: https://www.vecteezy.com/photo/32939587-futuristic-video-game-equipment-illuminated-in-nightclub
* Inspiration: AI/ML-based recommendation systems
* Support: Contributions and feedback from the open-source community