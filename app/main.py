import pandas as pd
from fastapi import FastAPI
import numpy as np
from pydantic import BaseModel
import pickle

app = FastAPI()
modelo_regresion = pickle.load(open("app/modelo_regresion/modelo_1.pkl", "rb"))
score_regresion = pickle.load(open("app/modelo_regresion/score_1.pkl", "rb"))

modelo_red_neuronal = pickle.load(open("app/modelo_regresion/modelo_2.pkl", "rb"))
score_red_neuronal = pickle.load(open("app/modelo_regresion/score_2.pkl", "rb"))


class Model(BaseModel):
    Años: float
    Años_de_experiencia: float
    Cargo: str

@app.get("/")
def main():
    return "Bienvenido a FastAPI Sueldos"

# Parametros
@app.get("/Regresion lineal")
def model_1(Años:float,Años_de_experiencia:float,Cargo:str):
    # Se importa el modelo de regresion
    data = pd.DataFrame({'Años': [Años],'Años_de_experiencia': [Años_de_experiencia], 'Cargo': [Cargo]})

    
    sueldo = modelo_regresion.predict(data)
    sueldo= "${:,.2f}".format(int(sueldo[0]))
    score_1=score_regresion

    return {"El Sueldo es": sueldo, "El score es de": "{:,.2f}".format(score_1)}

@app.get("/Red Neuronal")
def model_2(Años:float,Años_de_experiencia:float,Cargo:str):
    # Se importa el modelo de regresion
    data = pd.DataFrame({'Años': [Años],'Años_de_experiencia': [Años_de_experiencia], 'Cargo': [Cargo]})

    
    sueldo = modelo_red_neuronal.predict(data)
    sueldo= "{:,.2f}".format(int(sueldo[0]))
    score_2=score_red_neuronal
    
    return {"El Sueldo es": sueldo, "El score es de": "{:,.2f}".format(score_2)}