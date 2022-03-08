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

