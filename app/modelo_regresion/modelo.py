import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

df = pd.read_csv('app/modelo_regresion/Renta.csv',sep=",",encoding='latin-1')
df =pd.DataFrame(df)

#Feature
X = df.loc[:, ['Años','Años_de_experiencia','Cargo']]

#Variable dependiente
y =df.loc[:, ['Sueldo']]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 0.2, random_state=2)

#Codificacion de variable categorica
preprocessor = ColumnTransformer(
    transformers=[
        ('cat', OneHotEncoder(), ['Cargo'])
    ],
    remainder='passthrough'
)

# Entrenamiento del modelo
modelo = Pipeline([
    ('preprocessor', preprocessor),
    ('regressor', LinearRegression())
])
modelo.fit(X_train, y_train)

y_pred = modelo.predict(X_test)

#Visualización de datos de entrenamiento
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.scatter(X_train.loc[:, ['Años']], y_train, color = 'green')
#viz_train.plot(X_train.loc[:, ['Años']], model.predict(X_train), color = 'black')
plt.title('Sueldo vs Edad')
plt.xlabel('Edad')
plt.ylabel('Sueldo')


plt.subplot(1, 2, 2)
plt.scatter(X_train.loc[:, ['Años_de_experiencia']], y_train, color = 'blue')
#viz_train.plot(X_train.loc[:, ['Años']], model.predict(X_train), color = 'black')
plt.title('Sueldo vs Años de Experiencia')
plt.xlabel('Años de Experiencia')
plt.ylabel('Sueldo')

plt.tight_layout()
plt.show()

#Visualización de datos de test
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.scatter(X_test.loc[:, ['Años']], y_test, color = 'green')
#viz_train.plot(X_train.loc[:, ['Años']], model.predict(X_train), color = 'black')
plt.title('Sueldo vs Edad')
plt.xlabel('Edad')
plt.ylabel('Sueldo')


plt.subplot(1, 2, 2)
plt.scatter(X_test.loc[:, ['Años_de_experiencia']], y_test, color = 'blue')
#viz_train.plot(X_train.loc[:, ['Años']], model.predict(X_train), color = 'black')
plt.title('Sueldo vs Años de Experiencia')
plt.xlabel('Años de Experiencia')
plt.ylabel('Sueldo')

plt.tight_layout()
plt.show()

#Score del modelo de regresion multiple
modelo.score(X_test, y_test)

#Guardamos el modelo
pickle.dump(modelo, open('app/modelo_regresion/model.pkl','wb'))

#Importamos el modelo guardado
modelo = pickle.load(open('app/modelo_regresion/model.pkl','rb'))

#Input para ingresar la edad,experiencia y cargo
experiencia = float(input('Ingrese el valor de Años de experiencia: '))
edad = float(input('Ingrese el valor de Edad: '))
cargo = input('Ingrese el Cargo: ')

# Se almacenan valores de entrada en un data frame
data = pd.DataFrame({'Años': [edad],'Años_de_experiencia': [experiencia], 'Cargo': [cargo]})

#Predicción del sueldo.
sueldo = modelo.predict(data)

#Se redondea la prediccion del sueldo
sueldo= "${:,.2f}".format(int(sueldo[0]))
sueldo