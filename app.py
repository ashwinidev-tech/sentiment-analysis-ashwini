from flask import Flask, render_template, request, jsonify
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from pymongo import MongoClient
app = Flask(__name__)
analyzer = SentimentIntensityAnalyzer()
client = MongoClient("mongodb://localhost:27017/") 
db = client["sentimentDB"]
collection = db["analysis"]
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    text = data.get('text', '').strip()
    if not text:
        sentiment = 'Neutral'
        confidence = 0.0
    else:
        scores = analyzer.polarity_scores(text)
        compound = scores['compound']
        if compound >= 0.05:
            sentiment = 'Positive'
        elif compound <= -0.05:
            sentiment = 'Negative'
        else:
            sentiment = 'Neutral'
        confidence = round(abs(compound), 2)
    collection.insert_one({
        "text": text,
        "sentiment": sentiment,
        "confidence": confidence
    })
    return jsonify({
        'sentiment': sentiment,
        'confidence': confidence
    })
if __name__ == '__main__':
    app.run(debug=True,use_reloader=False)
