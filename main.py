from flask import Flask, request, jsonify
from scraper.scraper import scrape_reviews


app = Flask(__name__)

# Removed query parameter from the route definition
@app.route('/api/reviews', methods=['GET'])
def get_reviews():
    # Query parameter is handled inside the function
    url = request.args.get('page')
    if not url:
        return jsonify({"error": "URL parameter is required"}), 400
    
    if not url.startswith("http") :
        return jsonify({"error" : "Invalid URL format. Must start with http/https"}), 400
    
    try:
        reviews = scrape_reviews(url)
        return jsonify({
            "reviews_count": len(reviews),
            "reviews": reviews
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
