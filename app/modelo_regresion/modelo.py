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

y_train=np.ravel(y_train)
y_test=np.ravel(y_test)

#Codificacion de variable categorica
preprocessor = ColumnTransformer(
    transformers=[
        ('cat', OneHotEncoder(), ['Cargo'])
    ],
    remainder='passthrough'
)

# Entrenamiento del modelo
modelo_1 = Pipeline([
    ('preprocessor', preprocessor),
    ('regressor', LinearRegression())
])

modelo_2 = Pipeline([
    ('preprocessor', preprocessor),
    ('regressor', MLPRegressor(solver="lbfgs",max_iter=5000,hidden_layer_sizes=(30,30)))
])


modelo_1.fit(X_train, y_train)
modelo_2.fit(X_train, y_train)

y_pred_1 = modelo_1.predict(X_test)
y_pred_2 = modelo_2.predict(X_test)

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
print(modelo_1.score(X_test, y_test),modelo_2.score(X_test, y_test))


#Guardamos el modelo
pickle.dump(modelo_1, open('modelo_1.pkl','wb'))

#Importamos el modelo guardado
modelo_1 = pickle.load(open('modelo_1.pkl','rb'))

#Guardamos el modelo
pickle.dump(modelo_2, open('modelo_2.pkl','wb'))

#Importamos el modelo guardado
modelo_2 = pickle.load(open('modelo_2.pkl','rb'))

#Input para ingresar la edad,experiencia y cargo
experiencia = float(input('Ingrese el valor de Años de experiencia: '))
edad = float(input('Ingrese el valor de Edad: '))
cargo = input('Ingrese el Cargo: ')

# Se almacenan valores de entrada en un data frame
data = pd.DataFrame({'Años': [edad],'Años_de_experiencia': [experiencia], 'Cargo': [cargo]})

#Predicción del sueldo.
sueldo_1 = modelo_1.predict(data)
sueldo_2 = modelo_2.predict(data)

#Se redondea la prediccion del sueldo
sueldo_1= int(sueldo_1[0])
sueldo_2= int(sueldo_2[0])

score_1=modelo_1.score(data,sueldo_1)

print("sueldo 1",sueldo_1,"sueldo 2",sueldo_2)