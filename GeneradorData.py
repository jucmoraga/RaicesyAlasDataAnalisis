import pandas as pd
import numpy as np
from faker import Faker
from Persona import Persona
from preguntas import dar_abrs, Preguntas


def crear_dataframe():
    lista_preguntas = dar_abrs()
    datos = pd.DataFrame(
        columns=["Nombre","Genero", "Facultad", "Semestre"] + lista_preguntas
    )

    for i in range(10):
        resultado = persona_aleatoria()
        datos.loc[len(datos)]=[
            resultado.nombre,
            resultado.genero,
            resultado.facultad,
            resultado.semestre
        ] + resultado.respuestas
    return datos


def persona_aleatoria():
    fake = Faker()
    generos = ['Masculino', 'Femenino']
    facultades = ["FACULTAD DE EDUCACION","FACULTAD DE BELLAS ARTES","FACULTAD DE EDUCACION FISICA","FACULTAD DE HUMANIDADES","FACULTAD DE CIENCIA Y TECNOLOGIA"]
    sesgoGenero = [0.6, 0.4] 
    genero = np.random.choice(generos, p=sesgoGenero)
    if genero == 'Masculino':
        nombre = fake.name_male()
    else:
        nombre = fake.name_female()
    facultad = np.random.choice(facultades)
    semestre = np.random.randint(1, 11) 
    respuestas = respuestas_aleatorias()
    return Persona(nombre, genero, facultad, semestre, respuestas)

def respuestas_aleatorias():
    respuestas = []
    for pregunta in Preguntas:
        respuesta = np.random.choice(pregunta["opciones"])
        respuestas.append(respuesta)
    return respuestas