# Sentiment Analysis Web Application

This is a web-based Sentiment Analysis project built using Python Flask.
It analyzes user input text and classifies it as Positive, Negative, or Neutral
using the VADER Sentiment Analysis technique which is inbuilt model trained already.
This project uses MongoDB for storing sentiment analysis results.

## Features
- User-friendly web interface
- Real-time sentiment analysis
- Confidence score display
- Supports Positive, Negative, and Neutral classification

## Technologies Used
- Python
- Flask
- HTML/CSS
- VADER Sentiment Analysis
- NLTK
- MongoDB 

## Project Structure
app.py -> Flask,
ss.py -> Sentiment analysis logic(python file) ,
templates/index.html -> HTML files ,
requirements.txt-> Required libraries ,
README.md -> Project documentation

## How to Run the Project

1. Install Python (3.8 or above)
2. Install required libraries:
   pip install -r requirements.txt
3. Run the application:
   python app.py
4. Open browser and go to:
   http://127.0.0.1:5000/
5.Open mongodb 
MongoDB Connection URI: mongodb://localhost:27017

## Author
Ashwini S
