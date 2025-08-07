# heart-disease-api
API para predecir presencia de enfermedad cardíaca

# Disclaimer
**La información y API contenidas en este repositorio no deben utilizarse durante ninguna emergencia de salud, ni para el diagnóstico o tratamiento de alguna patología o trauma por accidente. Por favor, consulte a un médico.**

# Estructura del repositorio

```
|-model (contiene el modelo XGBoost)<br>
|-notebooks (contiene Jupyter Notebook para probar el servidor de forma local e interactiva)<br>
|-src (contiene código fuente para desplegar la API)<br>
|-02_client.ipybn<br>
|-requirements.txt (dependencias para utilizar el servidor y cliente en forma local)<br>
|-server.py (servidor local)
```
# Descarga del repositorio
```
git clone https://github.com/principioincertidumbre/heart-disease-api/
``` 

# Pasos previos usando Conda

Prerequisito: Tener [conda]( https://docs.conda.io/en/latest/contributing.html) instalado en tu computador.
## 1. Creando el entorno virtual (Virtual Environment)
```
conda create --name heart-disease-api python=3.11
```
Luego debemos activar el ambiente virtual:

```
conda activate heart-disease-api
```
## Instalando las dependencias usando PIP


# API en Render
https://heart-disease-api-m7x0.onrender.com/
