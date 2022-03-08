# ds_api
Una api para trabajar con los datos de deserción de alumnos en la UNAB

## Configuracion del entorno
  conda create --name <env> python=3.10  
  conda activate <env>  
  conda install uvicorn fastapi joblib  
  conda install -c conda-forge scikit-learn  
  
## Ejecucion
  cd app/  
  uvicorn main:app --reload  
  
## Endpoints
  ### /models
    Lista todos los modelos disponibles
  ### /metric/{model}
    Informa matriz de confusion y metricas del modelo
  ### /predict/{model}/?query
    Informa las probabilidades calculadas por el modelo sobre el caso presentado en los query parameters. Esto es para poder usarlo desde un form html



