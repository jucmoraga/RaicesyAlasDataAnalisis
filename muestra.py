import pandas as pd
import numpy as np
from faker import Faker
from resultados import respuestas_aleatorias

class Encuestado:
    def __init__(self):
        fake = Faker()
        generos = ['Masculino', 'Femenino']
        facultades = ["FACULTAD DE EDUCACION","FACULTAD DE BELLAS ARTES","FACULTAD DE EDUCACION FISICA",
                    "FACULTAD DE HUMANIDADES","FACULTAD DE CIENCIA Y TECNOLOGIA"]
        sesgoGenero = [0.6, 0.4] 
        genero = np.random.choice(generos, p=sesgoGenero)
        if genero == 'Masculino':
            nombre = fake.name_male()
        else:
            nombre = fake.name_female()
        
        facultad = np.random.choice(facultades)
        semestre = np.random.randint(1, 11) 
        
        identificacion = pd.DataFrame(columns=["Nombre","Genero", "Facultad", "Semestre"],
                                    data=[[nombre, genero, facultad, semestre]])
        self.data = pd.concat([identificacion, respuestas_aleatorias()],axis=1)



class Muestra():
    def __init__(self):
        self.data= pd.DataFrame()

    def generar_datos_aleatorios(self):
        for i in range(500):
            encuestado = Encuestado()
            datos = encuestado.data
            self.data = pd.concat([self.data, datos], ignore_index=True)

    def prueba(self):
        print(self.data)

