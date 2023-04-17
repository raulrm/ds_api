import uvicorn
import joblib
from fastapi import FastAPI, status, Form, Request
from fastapi.templating import Jinja2Templates
import sys
import glob
import os.path 
import pandas as pd
import json
from pathlib import Path



# database 
import sqlite3
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


db_name = os.path.dirname(os.path.abspath(__file__)) + '/../data/ds_api.sqlite'

#sys.path.append("..")
#templates = Jinja2Templates(directory = '/templates/')
BASE_DIR = Path(__file__).resolve().parent

templates = Jinja2Templates(directory=str(Path(BASE_DIR, 'templates')))



# Entry point!!!!
app = FastAPI()

# Lista MANUAL de modelo ya creados (ver TODO de ruta /models)
# models = {'lg':'logistic-regression','nb': 'naive-bayes', 'nn':'neural-network', 'rf':'random-forest', 'ab':'adaboost', 'xg': 'XGBoost'}

# con glob obtenemos los archivos de los modelos compilados
file_models = glob.glob("models/*.mod")
# de esa lista mostramos el substring que define el modelo
# lamentablemente no tenemos un descripcion del modelo
models = [name[14:16] for name in file_models]


# funcion auxiliar para obtener los campos de la BBDD
# oooorivle, ya se...
#SQLALCHEMY_DATABASE_URL = "sqlite:///../data/ds_api.sqlite"

#engine = create_engine(
#    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
#)
#SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#Base = automap_base()
#Base.prepare(engine, reflect=True)
#Desercion = Base.classes.desercion

print(db_name)

def getCampos() -> dict:
	conn = sqlite3.connect(db_name)
	cursor = conn.cursor()
	#data=cursor.execute('''SELECT * FROM desercion''')
	data = cursor.execute("SELECT replace(name,'(','') , type FROM PRAGMA_table_info('desercion'); ")
	return list(data)



# Campos del dataset TODO ver si pydantic ayuda creando una estructura de datos
# campos = ["algun_contenido_publicado",
# 		"comentario_creado",
# 		"curso_visto",
# 		"entrega_creada.",
# 		"finalización_actividad_curso",
# 		"formulario_entrega_visto.",
# 		"comenzado_intento",
# 		"intento_cuestionario_visualizado",
# 		"intento_cuestionario_revisado",
# 		"ntento_enviado",
# 		"mensaje_creado",
# 		"modulo_curso_visto",
# 		"perfil_usuario_visto",
# 		"resumen_intento_cuestionario_visualizado",
# 		"enviado_entrega",
# 		"suscrito_discusión",
# 		"visualizado_estado_entrega",
# 		"tema_creado",
# 		"tema_visto",
# 		"fichero_subido",
# 		"usuario_calificado",
# 		"lista_usuarios_vista",
# 		"mensaje_borrado",
# 		"borrado_suscripcion_discusion",
# 		"tema_borrado",
# 		"informe_notas_usuario_visto",
# 		"mensaje_actualizado",
# 		"instancia_módulo_curso_visualizada",
# 		"informe_resumen_notas_visto",
# 		"lista_insignias_vista",
# 		"envío_actualizado",
# 		"usuario_matriculado_curso",
# 		"elemento_calificacion_actualizado",
# 		"informe_usuario_visualizado",
# 		"informe_usuario_curso_visto",
# 		"suscripcion_activada",
# 		"curso_actualizado",
# 		"elemento_calificacio_creado",
# 		"completo"]

#campos = getCampos()

@app.get('/campos')
def getCamposApi(request: Request):
	salida1 = getCampos()
	#return {'mensaje': BASE_DIR}

	return templates.TemplateResponse("formulario.html", {"request": request, "campos": salida1},)

@app.get('/')
def get_root():
	""" Presentacion de la API

	Returns:
		dict : mensaje
	"""
	# TODO rutear a un template html 
	return {'mensaje': 'Welcome to the unab data science test api'}


@app.get('/models')
async def show_models():
	""" Mostramos los modelos que tenemos configurados

	Returns:
		dict : lista de modelos
	"""
	# TODO hacer que lea los modelos desde la carpeta donde se hayan los mismos
	# (en eso estamos)
	return {'modelos':models}


@app.get('/metric/{model}')
async def show_metric(model: str):
	""" Mostramos la matriz de confusion calculada para cada modelo

	Args:
		model (str): El nombre del modelo que nos interesa 

	Returns:
		json: matriz de confusion del modelo
	"""
	# TODO responder con los codigos HTTP correctos
	# reconstruimos el path del archivo
	filename = 'models/modelo_'+ model +'.mtx'
	# Mensaje por defecto
	mtx = 'No existe ese modelo'
	# chequeamos si existe el fichero, lo cargamos en la matriz y lo convertimos a lista
	if exists(filename):
		mtx = joblib.load(filename).tolist()
	# se retorna o bien la matriz o bien el mensaje de error
	return {'matriz de confusion': mtx }


@app.get('/predict/{model}')
async def show_predict(model: str, req: Request):
	""" Recibe un modelo y una query 

	Args:
		model (str): modelo
		algun_contenido_publicado (str, optional): todos los campos del dataset. Defaults to ''.

	Returns:
		json : Retorna si completa o no el curso
	"""
	# TODO TODO
	# cargamos std y mean
	desvio = joblib.load("data/desvio.dat")
	media = joblib.load('data/media.dat')
	# normalizamos los valores
	# creamos el filename completo
	# vemos si existe el modelo (el archivo)
	# cargamos el modelo
	# hacemos el predict
	# convertimos a lista la salida
	# lo retornamos
	query_params = dict(req.query_params)
	return {'modelo elegido':model,'desvio': desvio, 'media':media, 'query': query_params }
	#return {'modelo elegido':model, 'algun_contenido_publicado': algun_contenido_publicado}



@app.post('/insert/')
async def set_instancia(algun_contenido_publicado: str = ''):
	"""sumary_line
	
	Keyword arguments:
	argument -- description
	Return: return_description
	"""
	# TODO TODO
	# nos fijamos que esten todos los campos
	# abrimos la conexion
	# insertamos el registro
	# reprocesamos los modelos (apa! esto es lo dificil!!!)
	return {'algun_contenido_publicado': algun_contenido_publicado}





# Ejecutamos el codigo (esto es para debuggear)
if __name__ == "__main__":
	uvicorn.run(app, host="0.0.0.0", port=8000)
