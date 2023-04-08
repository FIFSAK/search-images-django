from flask import Flask, render_template, request
import json
import requests

app = Flask(__name__, template_folder='.')

API_KEY = "DuaCuEifyNh8i0cjdYoGt6du82vYVxD3KwaR5sqSxiElaBERgiFgZttg"
ENDPOINT = "https://api.pexels.com/v1/curated"

def get_photo_urls(query):
    url = "https://api.pexels.com/v1/search"
    headers = {"Authorization": API_KEY}
    params = {"query": query, "per_page": 10}
    response = requests.get(url, headers=headers, params=params)
    photos = response.json()["photos"]
    photo_urls = [f"https://images.pexels.com/photos/{photo['id']}/pexels-photo-{photo['id']}.jpeg" for photo in photos]
    return photo_urls

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        search_value = request.form['search']
        search_data = {'searchTerm': search_value}
        with open('search-data.json', 'w') as f:
            json.dump(search_data, f)

        photo_urls = get_photo_urls(search_value)
        with open('search-data.json', 'w') as f:
            json.dump(photo_urls, f)

        return "Input and photo URLs saved to search-data.json"

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
