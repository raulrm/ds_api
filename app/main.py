from telnetlib import STATUS
from turtle import st
import joblib
import re
from sklearn.neural_network import MLPClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from fastapi import FastAPI, status
import sys
sys.path.append("..")

app = FastAPI()

model = joblib.load('models/modelo_lg.mod')

models = {'lg':'logistic-regression','nb': 'naive-bayes', 'nn':'neural-network', 'rf':'random-forest', 'ab':'adaboost', 'xg': 'XGBoost'}

campos = ["algun_contenido_publicado.",
		"comentario_creado",
		"curso_visto",
		"entrega_creada.",
		"finalización_actividad_curso",
		"formulario_entrega_visto.",
		"comenzado_intento",
		"intento_cuestionario_visualizado",
		"intento_cuestionario_revisado",
		"ntento_enviado",
		"mensaje_creado",
		"modulo_curso_visto",
		"perfil_usuario_visto",
		"resumen_intento_cuestionario_visualizado",
		"enviado_entrega",
		"suscrito_discusión",
		"visualizado_estado_entrega.",
		"tema_creado",
		"tema_visto",
		"fichero_subido",
		"usuario_calificado",
		"lista_usuarios_vista",
		"mensaje_borrado",
		"borrado_suscripcion_discusion",
		"tema_borrado",
		"informe_notas_usuario_visto",
		"mensaje_actualizado",
		"instancia_módulo_curso_visualizada",
		"informe_resumen_notas_visto",
		"lista_insignias_vista",
		"envío_actualizado",
		"usuario_matriculado_curso",
		"elemento_calificacion_actualizado",
		"informe_usuario_visualizado",
		"informe_usuario_curso_visto",
		"suscripcion_activada",
		"curso_actualizado",
		"elemento_calificacio_creado",
		"completo"]

@app.get('/')
def get_root():
	""" Presentacion de la API

	Returns:
		dict : mensaje
	"""
	return {'mensaje': 'Welcome to the unab data science test api'}


@app.get('/models')
async def show_models():
	""" Mostramos los modelos que tenemos configurados

	Returns:
		dict : lista de modelos
	"""
	return {'modelos':models}


@app.get('/metric/{model}')
async def show_metric(model: str):

	return {'modelo elegido':model}


@app.post('/predict/{model}')
async def show_predict(model: str, algun_contenido_publicado: str = ''):

	return {'modelo elegido':model, 'algun_contenido_publicado': algun_contenido_publicado}
