document.getElementById('recommendationForm').addEventListener('submit', async function (e) {
    e.preventDefault();

    const mood = document.getElementById('mood').value;
    const numRecommendations = document.getElementById('numRecommendations').value;

    const response = await fetch('/get_recommendations/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCSRFToken(), // Ensure CSRF token is included
        },
        body: JSON.stringify({ mood, num_recommendations: numRecommendations }),
    });

    if (response.ok) {
        const data = await response.json();
        displayResults(data.recommendations);
    } else {
        console.error('Error fetching recommendations');
    }
});

function displayResults(recommendations) {
    const resultsDiv = document.getElementById('results');
    resultsDiv.innerHTML = '<h2>Recommended Games:</h2>';
    const ul = document.createElement('ul');
    recommendations.forEach(game => {
        const li = document.createElement('li');
        li.textContent = `${game.name} - ${game.genre} (${game.year})`;
        ul.appendChild(li);
    });
    resultsDiv.appendChild(ul);
}

function getCSRFToken() {
    return document.querySelector('[name=csrfmiddlewaretoken]').value;
}
