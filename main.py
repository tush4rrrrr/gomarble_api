from flask import Flask, render_template, request, jsonify
from scraper.scraper import scrape_reviews  #Importing scraper logic

app = Flask(__name__)

#Front-end route
@app.route('/')
def index():
    return render_template('index.html')

#API route for scraping
@app.route('/api/reviews', methods=['GET'])
def get_reviews():
    url = request.args.get('page')
    if not url:
        return jsonify({"error": "URL parameter is required"}), 400

    reviews = scrape_reviews(url)
    return jsonify(reviews)

if __name__ == "__main__":
    app.run(debug=True)
