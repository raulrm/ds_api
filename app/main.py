import joblib
import re
from sklearn.neural_network import MLPClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from fastapi import FastAPI
import sys
sys.path.append("..")

app = FastAPI()

model = joblib.load('models/modelo_lg.mod')

models = {'logistic_regression':'lg','naive-bayes':'nb', 'neural':'nn', 'random-forest':'rf', 'adaboost':'ab'}

@app.get('/')
def get_root():

	return {'message': 'Welcome to the unab data science test api'}


@app.get('/models')
async def show_models():

	return {'modelos':models}


@app.get('/metric/{model}')
async def show_metric():

	return {'modelos':models}


@app.get('/predict/{model}/query')
async def show_predict():

	return {'modelos':models}
