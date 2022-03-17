import joblib
from fastapi import FastAPI, status, Form
import sys
from os.path import exists

#sys.path.append("..")

# Entry point!!!!
app = FastAPI()

# Lista MANUAL de modelo ya creados (ver TODO de ruta /models)
models = {'lg':'logistic-regression','nb': 'naive-bayes', 'nn':'neural-network', 'rf':'random-forest', 'ab':'adaboost', 'xg': 'XGBoost'}

# Campos del dataset TODO ver si pydantic ayuda creando una estructura de datos
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
		"visualizado_estado_entrega",
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
	# TODO rutear a un template html 
	return {'mensaje': 'Welcome to the unab data science test api'}


@app.get('/models')
async def show_models():
	""" Mostramos los modelos que tenemos configurados

	Returns:
		dict : lista de modelos
	"""
	# TODO hacer que lea los modelos desde la carpeta donde se hayan los mismos
	return {'modelos':models}


@app.get('/metric/{model}')
async def show_metric(model: str):
	"""_summary_

	Args:
		model (str): El modelo que nos interesa 

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


@app.post('/predict/{model}')
async def show_predict(model: str, algun_contenido_publicado: str = ''):
	""" Recibe un modelo y una query 

	Args:
		model (str): modelo
		algun_contenido_publicado (str, optional): todos los campos del dataset. Defaults to ''.

	Returns:
		json : Retorna si completa o no el curso
	"""
	# TODO TODO
	# cargamos std y mean
	# normalizamos los valores
	# creamos el filename completo
	# vemos si existe el modelo (el archivo)
	# cargamos el modelo
	# hacemos el predict
	# convertimos a lista la salida
	# lo retornamos
	return {'modelo elegido':model, 'algun_contenido_publicado': algun_contenido_publicado}



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