from flask import Flask, render_template, request
import json

app = Flask(__name__, template_folder='.')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        search_value = request.form['search']
        search_data = {
            'searchTerm': search_value
        }

        with open('search-data.json', 'w') as f:
            json.dump(search_data, f)

        return "Input saved to search-data.json"

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
