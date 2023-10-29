import pandas as pd
from fastapi import FastAPI
import numpy as np
from pydantic import BaseModel
import pickle

app = FastAPI()
model_predict = pickle.load(open("app/train-model/model.pkl", "rb"))


class Model(BaseModel):
    Años: float
    Años_de_experiencia: float
    Cargo: str

@app.get("/")
def main():
    return "Bienvenido to Machine Learning FastAPI"

# Request body
@app.post("/api/")
def model(data: Model):
    # Import the saved model
    input_data = pd.DataFrame({'Años': [data.Años],'Años_de_experiencia': [data.Años_de_experiencia], 'Cargo': [data.Cargo]})

    
    user_salary = model_predict.predict(input_data)

    return {"Sueldo": int(user_salary[0])}


# Query parameters
@app.get("/api/")
def model(Años:float,Años_de_experiencia:float,Cargo:str):
    # Import the saved model
    input_data = pd.DataFrame({'Años': [Años],'Años_de_experiencia': [Años_de_experiencia], 'Cargo': [Cargo]})

    
    user_salary = model_predict.predict(input_data)

    return {"Sueldo": int(user_salary[0])}

