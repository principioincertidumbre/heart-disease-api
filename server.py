import joblib
import numpy as np
import io
import uvicorn
from enum import Enum
from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

xgb = joblib.load("./model/heart_model.joblib")

def predict_heart_disease(features_patient, confidence):
    """Recibe un vector de características de un paciente y predice si padece o no una enfermedad cardíaca.

    Argumentos:
        features_trip (array): Características del viaje, vector de tamaño 14.
        confidence (float, opcional): Nivel de confianza. Por defecto es 0.5.
    """

    pred_value = xgb.predict_proba(features_patient.reshape(1, -1))[0][1]
    if pred_value >= confidence:
      return 1
    else:
      return 0

# Asignamos una instancia de la clase FastAPI a la variable "app".
# Interacturaremos con la API usando este elemento.
app = FastAPI(title='Implementando un modelo de predicción de presencia de enfermedades cardíacas usando FastAPI')

# Creamos una clase para el vector de features de entrada
class Item(BaseModel):
    age: int
    sex: int
    cp:  int
    trestbps: int
    chol: int
    fbs:  int
    restecg: int
    thalach: int
    exang: int
    oldpeak: float
    slope: int
    ca: int
    thal: int

# Usando @app.get("/") definimos un método GET para el endpoint / (que sería como el "home").
@app.get("/")
def home():
    return "¡Felicitaciones! Tu API está funcionando según lo esperado. Anda ahora a http://localhost:8000/docs."


# Este endpoint maneja la lógica necesaria para clasificar.
# Requiere como entrada el vector de características del viaje y el umbral de confianza para la clasificación.
@app.post("/predict")
def prediction(item: Item, confidence: float):


    # 1. Correr el modelo de clasificación
    features_patient = np.array([item.age, item.sex, item.cp, item.trestbps, item. chol, item.fbs,
                    item.restecg, item.thalach, item.exang, item.oldpeak, item.slope, item.ca, item.thal])
    pred = predict_heart_disease(features_patient, confidence)

    # 2. Transmitir la respuesta de vuelta al cliente

    # Retornar el resultado de la predicción
    return {'predicted_class': pred}

# Donde se hospedará el servidor
host = "127.0.0.1"

# ¡Iniciemos el servidor!
uvicorn.run(app, host=host, port=8000)
