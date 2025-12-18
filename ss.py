from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()
def analyze_sentiment(text):
    scores = analyzer.polarity_scores(text)
    compound = scores['compound']
    if compound >= 0.05:
        sentiment = "Positive"
        confidence = round(compound, 2)
    elif compound <= -0.05:
        sentiment = "Negative"
        confidence = round(abs(compound), 2)
    else:
        sentiment = "Neutral"
        confidence = round(1 - abs(compound), 2)  
    return sentiment, confidence
