import joblib
import numpy as np
import io
import uvicorn
from enum import Enum
from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel, ValidationError, field_validator

try:
   cbt = joblib.load("./model/heart_model.joblib")
except FileNotFoundError:
    print("Error: heart_model.joblib no fue encontrado.")
    raise SystemExit


def predict_heart_disease(features_patient, confidence):
    """Recibe un vector de características de un paciente y predice si padece o no una enfermedad cardíaca.

    Argumentos:
        features_trip (array): Características del viaje, vector de tamaño 14.
        confidence (float, opcional): Nivel de confianza. Por defecto es 0.5.
    """

    pred_value = cbt.predict_proba(features_patient.reshape(1, -1))[0][1]
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

    @field_validator('age', mode='after')

    @classmethod
    def is_age(cls, value: int) -> int:
        if value > 77 or value < 29:
            raise ValueError(f'{value} es un valor fuera de rango')
        return value

    @field_validator('sex', mode='after')

    @classmethod
    def is_sex(cls, value: int) -> int:
        if value > 1 or value < 0:
            raise ValueError(f'{value} no es un valor válido')
        return value

    @field_validator('cp', mode='after')

    @classmethod
    def is_cp(cls, value: int) -> int:
        if value > 4 or value < 0:
            raise ValueError(f'{value} no es un valor válido')
        return value


    @field_validator('trestbps', mode='after')

    @classmethod
    def is_trestbps(cls, value: int) -> int:
        if value > 200 or value < 94:
            raise ValueError(f'{value} es un valor fuera de rango')
        return value

    @field_validator('chol', mode='after')

    @classmethod
    def is_chol(cls, value: int) -> int:
        if value > 564 or value < 126:
            raise ValueError(f'{value} es un valor fuera de rango')
        return value

    @field_validator('fbs', mode='after')

    @classmethod
    def is_fbs(cls, value: int) -> int:
        if value > 1 or value < 0:
            raise ValueError(f'{value} no es un valor válido')
        return value

    @field_validator('restecg', mode='after')

    @classmethod
    def is_restecg(cls, value: int) -> int:
        if value > 2 or value < 0:
            raise ValueError(f'{value} no es un valor válido')
        return value

    @field_validator('thalach', mode='after')

    @classmethod
    def is_thalach(cls, value: int) -> int:
        if value > 202 or value < 71:
            raise ValueError(f'{value} es un valor fuera de rango')
        return value

    @field_validator('exang', mode='after')

    @classmethod
    def is_exang(cls, value: int) -> int:
        if value > 1 or value < 0:
            raise ValueError(f'{value} no es un valor válido')
        return value

    @field_validator('oldpeak', mode='after')

    @classmethod
    def is_oldpeak(cls, value: float) -> float:
        if value > 6.2 or value < 0.0:
            raise ValueError(f'{value} es un valor fuera de rango')
        return value

    @field_validator('slope', mode='after')

    @classmethod
    def is_slope(cls, value: int) -> int:
        if value > 3 or value < 0:
            raise ValueError(f'{value} no es un valor válido')
        return value

    @field_validator('ca', mode='after')

    @classmethod
    def is_ca(cls, value: int) -> int:
        if value > 3 or value < 0:
            raise ValueError(f'{value} no es un valor válido')
        return value

    @field_validator('thal', mode='after')

    @classmethod
    def is_thal(cls, value: int) -> int:
        if value > 3 or value < 0:
            raise ValueError(f'{value} no es un valor válido')
        return value

# Usando @app.get("/") definimos un método GET para el endpoint / (que sería como el "home").
@app.get("/")
def home():
    return "¡Felicitaciones! Tu API está funcionando según lo esperado. Anda ahora a http://localhost:8000/docs."


# Este endpoint maneja la lógica necesaria para clasificar.
# Requiere como entrada el vector de características del viaje y el umbral de confianza para la clasificación.
@app.post("/predict")
def prediction(item: Item, confidence: float):
    if model is None:
        raise HTTPException(status_code=500, detail="Modelo no fue cargado correctamente.")
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
