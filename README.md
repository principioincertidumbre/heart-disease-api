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
## 2. Instalando las dependencias usando PIP
```
pip install -r requirements.txt
```
## 3. Instalando el kernel de Jupyter Lab correspondiente al proyecto
```
python -m ipykernel install --user --name heart-disease-api
``` 
## 4. Iniciando Jupyter Lab
```
jupyter lab
```
Después de completar estos pasos puede ejecutar el script del servidor desde la terminal de Python 3 y el Jupyter Notebook del cliente localmente.

# Pasos previos usando uv

Prerequisito: Tener [uv](https://docs.astral.sh/uv/) instalado en tu computador.
uv es una herramienta moderna y rápida para gestionar entornos virtuales y dependencias de Python. Como alternativa a conda, puedes usar uv que ofrece un rendimiento significativamente mejor.

## 1. Instalando uv

Si no tienes uv instalado, puedes instalarlo con:

* Windows (PowerShell)
  ```
  powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
  ``` 
  
* Windows/MacOS/Linux (usando pip)
  ``` 
  pip install uv
  ```
* MacOS/Linux
  ```
  curl -LsSf https://astral.sh/uv/install.sh | sh
  ```

## 2. Creando el entorno virtual con uv
Navega al directorio heart-disease-api y crea un entorno virtual:
 ```
 uv venv
 ```
## 3. Activando el entorno virtual

 * Windows:
 
 ```
  heart-disease-api\Scripts\activate
```
* MacOS/Linux:
 ```  
 source .venv/bin/activate
```
## 4. Instalando las dependencias con uv

Con el entorno activado, instala Jupyter Lab si no lo ha instalado anteriormente:

```
uv pip install jupyter lab
```
Si prefiere instalar Jupyter Lab a nivel de sistema operativo:
``` 
uvx jupyter lab
```
Luego instala todas las dependencias directamente desde requirements.txt:
``` 
uv pip install -r requirements.txt
```
Este comando es significativamente más rápido que pip tradicional y maneja mejor la resolución de dependencias.

## 5. Instalando el kernel de Jupyter Lab correspondiente al proyecto
```
python -m ipykernel install --user --name heart-disease-api
``` 
## 6. Iniciando Jupyter Lab
```
jupyter lab
```
# API en Render
https://heart-disease-api-m7x0.onrender.com/
