import joblib
import re
from sklearn.neural_network import MLPClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from fastapi import FastAPI
import sys
sys.path.append("..")

app = FastAPI()

model = joblib.load('models/spam_classifier.joblib')

models = ['naive-bayes', 'neural', 'random-forest', 'boost']

@app.get('/')
def get_root():

	return {'message': 'Welcome to the unab data science test api'}


@app.get('/models')
async def show_models():

	return {'modelos':models}