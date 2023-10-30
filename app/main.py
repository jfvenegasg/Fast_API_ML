import pandas as pd
from fastapi import FastAPI
import numpy as np
from pydantic import BaseModel
import pickle

app = FastAPI()
modelo_regresion = pickle.load(open("app/modelo_regresion/model.pkl", "rb"))


class Model(BaseModel):
    Años: float
    Años_de_experiencia: float
    Cargo: str

@app.get("/")
def main():
    return "Bienvenido a FastAPI Sueldos"

# Parametros
@app.get("/api/")
def model(Años:float,Años_de_experiencia:float,Cargo:str):
    # Se importa el modelo de regresion
    data = pd.DataFrame({'Años': [Años],'Años_de_experiencia': [Años_de_experiencia], 'Cargo': [Cargo]})

    
    sueldo = modelo_regresion.predict(data)
    sueldo= "${:,.2f}".format(int(sueldo[0]))
    
    return {"Sueldo": sueldo}

