# heart-disease-api
API para predecir presencia de enfermedad cardíaca

## Disclaimer
**La información y API contenidas en este repositorio no deben utilizarse durante ninguna emergencia de salud, ni para el diagnóstico o tratamiento de alguna patología o trauma por accidente. Por favor, consulte a un médico.**

## Estructura del repositorio

```
|-model (contiene el modelo XGBoost)
|-notebooks (contiene Jupyter Notebook para probar el servidor de forma local e interactiva)
|-src (contiene código fuente para desplegar la API)
|-02_client.ipynb
|-requirements.txt (dependencias para utilizar el servidor y cliente en forma local)
|-server.py (servidor local)
```
## Descarga del repositorio
```
git clone https://github.com/principioincertidumbre/heart-disease-api/
``` 

## Pasos previos usando Conda

Prerequisito: Tener [conda]( https://docs.conda.io/en/latest/contributing.html) instalado en tu computador.
### 1. Creando el entorno virtual (Virtual Environment)
```
conda create --name heart-disease-api python=3.11
```
Luego debemos activar el ambiente virtual:

```
conda activate heart-disease-api
```
### 2. Instalando las dependencias usando PIP
```
pip install -r requirements.txt
```
### 3. Instalando el kernel de Jupyter Lab correspondiente al proyecto
```
python -m ipykernel install --user --name heart-disease-api
``` 
### 4. Iniciando Jupyter Lab
```
jupyter lab
```
Después de completar estos pasos puede ejecutar el script del servidor desde la terminal de Python 3 y el Jupyter Notebook del cliente localmente.

## Pasos previos usando uv

Prerequisito: Tener [uv](https://docs.astral.sh/uv/) instalado en tu computador.
uv es una herramienta moderna y rápida para gestionar entornos virtuales y dependencias de Python. Como alternativa a conda, puedes usar uv que ofrece un rendimiento significativamente mejor.

### 1. Instalando uv

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

### 2. Creando el entorno virtual con uv
Navega al directorio heart-disease-api y crea un entorno virtual:
 ```
 uv venv
 ```
### 3. Activando el entorno virtual

 * Windows:
 
 ```
  heart-disease-api\Scripts\activate
```
* MacOS/Linux:
 ```  
 source .venv/bin/activate
```
### 4. Instalando las dependencias con uv

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

### 5. Instalando el kernel de Jupyter Lab correspondiente al proyecto
```
python -m ipykernel install --user --name heart-disease-api
``` 
### 6. Iniciando Jupyter Lab
```
jupyter lab
```
## API en Render

Para realizar consultas de forma remota a la API, se encuentra disponible en la siguiente URL:

https://heart-disease-api-m7x0.onrender.com/

## Información para realizar consultas a la API

Para realizar consultas desde su computador, el Jupyter Notebook que contiene el cliente le permite ajustar los valores del JSON de entrada y el nivel de confianza de los resultados entregados por el modelo.

### Estructura JSON de entrada
``` 
item_features =  {
    "age": int,
    "sex": int,
    "cp":  int,
    "trestbps": int,
    "chol": int,
    "fbs":  int,
    "restecg": int,
    "thalach": int,
    "exang": int,
    "oldpeak": int,
    "slope": int,
    "ca": int,
    "thal": int
}
``` 
### Valores esperados para cada campo

El conjunto de datos seleccionado para entrenar el modelo es "Heart Disease Dataset", el cual considera las siguientes variables o atributos:

age: edad del paciente (el rango de edad considerado en el modelo es de 29 a 77 años)

sex: sexo (1 = hombre, 0 = mujer)

cp: tipo de dolor en el pecho (categorías de 1 a 4, denominadas 1: angina típica, 2: angina atípica, 3: dolor torácico que no es causado por angina, 4: asintomático)

trestbps: presión arterial en reposo (en mm Hg, rango estudiado: 94-200 mmHg)

chol: nivel de colesterol en sangre (mg/dl, rango estudiado: 126-564 mg/dL)

fbs: glucemia en ayunas (> 120 mg/dl, 1 = verdadero; 0 = falso)

restecg: resultados del electrocardiograma en reposo (0: normal, 1: tiene anomalías de la onda ST-T (inversiones de la onda T y/o elevación o depresión ST de > 0.05 mV), 2: muestra probablemente o definitivamente hipertrofia del ventrículo izquierdo según los criterios de Estes)

thalach: frecuencia cardíaca máxima alcanzada (rango estudiado: 71-202)

exang: angina inducida por ejercicio (1 = sí, 0 = no)

oldpeak: depresión ST inducida por el ejercicio en relación al reposo (rango estudiado: 0.0-6.2)

slope: Pendiente del segmento ST del ejercicio máximo. (1: ascendente, 2: plana, 3: descendente)

ca: número de vasos principales coloreados por fluoroscopia (de 0 a 3)

thal: talasemia (1 = normal, 2 = defecto fijo, 3 = defecto reversible)

**Resultados esperados de una consulta válida:**

target: variable objetivo (1 = presencia de enfermedad cardíaca, 0 = ausencia de enfermedad cardíaca)

### Ejemplos de consultas válidas

Ejemplo 1:
``` 
item_features =  {
    "age": 41,
    "sex": 1,
    "cp":  0,
    "trestbps": 110,
    "chol": 172,
    "fbs":  0,
    "restecg": 0,
    "thalach": 158,
    "exang": 0,
    "oldpeak": 0,
    "slope": 2,
    "ca": 3,
    "thal": 2
}

prediction = response_from_server(full_url, item_features)
prediction.text

¡Todo funcionó bien!

'{"predicted_class":0}'
``` 



