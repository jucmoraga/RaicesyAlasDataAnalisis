import pandas as pd
import numpy as np

Preguntas = [
    {
        id: 1,
        "seccion": 2,
        "abr": "s2-p1",
        "texto": "¿Sueles leer afiches, murales, grafitis o anuncios en las paredes de la Universidad?",
        "opciones": ["Si","No"]
    },
    {
        id: 2,
        "seccion": 2,
        "abr": "s2-p2",
        "texto": "¿Asistes a la Biblioteca Central de la Universidad a hacer préstamos de libros?",
        "opciones": ["Si","No"]
    },
    {
        id: 3,
        "seccion": 2,
        "abr": "s2-p3",
        "texto": "¿Asistes a bibliotecas públicas para hacer préstamos de libros?",
        "opciones": ["Si","No"]
    },
    {
        id: 4,
        "seccion": 2,
        "abr": "s2-p4",
        "texto": "¿Asistes a bibliotecas comunitaria para hacer préstamos de libros?",
        "opciones": ["Si","No"]
    },
    {
        id: 5,
        "seccion": 2,
        "abr": "s2-p5",
        "texto": "¿Tienes una biblioteca personal o familiar en tu casa?",
        "opciones": ["Si","No"]
    },
    {
        id: 6,
        "seccion": 2,
        "abr": "s2-p6",
        "texto": "¿Cuando eras pequeño/a recuerdas que alguien te leyera? ",
        "opciones": ["Si","No"]
    },
    {
        id: 7,
        "seccion": 2,
        "abr": "s2-p7",
        "texto": "¿Te gusta leer literatura? (novela, cuentos, poesía, teatro)",
        "opciones": ["Si","No"]
    },
    {
        id: 8,
        "seccion": 2,
        "abr": "s2-p8",
        "texto": "¿Acostumbras a escribir textos personales? (diarios, notas, opiniones, blogs…)",
        "opciones": ["Si","No"]
    },
    {
        id: 9,
        "seccion": 2,
        "abr": "s2-p9",
        "texto": "¿Acostumbras a escribir textos literarios? (ej. Relatos, cuentos, historias, poemas, etc.)",
        "opciones": ["Si","No"]
    },
    {
        id: 10,
        "seccion": 2,
        "abr": "s2-p10",
        "texto": "¿Asistes a librerías de la ciudad para hacer compra de libros?",
        "opciones": ["Si","No"]
    },
    {
        id: 11,
        "seccion": 2,
        "abr": "s2-p11",
        "texto": "En este año ¿has asistido a alguna comunidad lectora? (club o círculo de lectura, grupo de estudio, grupos de investigación etc.)",
        "opciones": ["Si","No"]
    },
    {
        id: 12,
        "seccion": 2,
        "abr": "s2-p12",
        "texto": "En este año ¿Has leído en voz alta a alguna persona o grupo?",
        "opciones": ["Si","No"]
    },
    {
        id: 13,
        "seccion": 2,
        "abr": "s2-p13",
        "texto": "En este año ¿Has leído un libro de literatura (novela, cuentos poesía) completo?",
        "opciones": ["Si","No"]
    },
    {
        id: 14,
        "seccion": 2,
        "abr": "s2-p14",
        "texto": "En este año ¿has leído algún libro completo de teoría o desarrollo de tu campo disciplinar?",
        "opciones": ["Si","No"]
    },
    {
        id: 15,
        "seccion": 2,
        "abr": "s2-p15",
        "texto": "¿Utilizas alguna red social para compartir tus opiniones de lo que lees o enterarte de novedades de lectura?",
        "opciones": ["Si","No"]
    },
    {
        id: 16,
        "seccion": 2,
        "abr": "s2-p16",
        "texto": "¿Consideras que tus prácticas de lectura y escritura cambiaron después de la pandemia Covid19?",
        "opciones": ["Si","No"]
    },
    {
        id: 17,
        "seccion": 2,
        "abr": "s2-p17",
        "texto": "¿Consideras que tus hábitos de lectura y escritura mejoraron al ingresar a la Universidad?",
        "opciones": ["Si","No"]
    },
    {
        id: 18,
        "seccion": 2,
        "abr": "s2-p18",
        "texto": "¿Haces uso de la Inteligencia Artificial Generativa (de ahora en adelante IAG) (Chat GPT, Deep seek, etc.) en tus actividades académicas?",
        "opciones": ["Si","No"]
    },
    {
        id: 19,
        "seccion": 2,
        "abr": "s2-p19",
        "texto": "¿Utilizas la IAG para apoyar la escritura de trabajos académicos asignados?",
        "opciones": ["Si","No"]
    },
    {
        id: 20,
        "seccion": 2,
        "abr": "s2-p20",
        "texto": "¿Te apoyas en la IAG (Chat GPT, Deep seek, etc.) para comprender textos académicos asignados?",
        "opciones": ["Si","No"]
    },
    {
        id: 21,
        "seccion": 2,
        "abr": "s2-p21",
        "texto": "¿Consideras que el uso de la IAG afecta negativamente tu proceso de lectura y escritura?",
        "opciones": ["Si","No"]
    },
    {
        id: 22,
        "seccion": 3,
        "abr": "s3-p1",
        "texto": "¿Qué tanto te gusta leer?",
        "opciones": ["Nada","Poco","Medianamente","Mucho"]
    },
]

def dar_abrs():
    lista_abr = [pregunta["abr"] for pregunta in Preguntas]
    return lista_abr

def dar_texto(abr: str)->str:
    for pregunta in Preguntas:
        if pregunta["abr"] == abr:
            return pregunta["texto"]
    return None

def dar_seccion(abr: str)->int:
    for pregunta in Preguntas:
        if pregunta["abr"] == abr:
            return pregunta["seccion"]
    return None

def respuestas_aleatorias():
    respuestas = []
    for pregunta in Preguntas:
        respuesta = np.random.choice(pregunta["opciones"])
        respuestas.append(respuesta)
    return pd.DataFrame([respuestas], columns=dar_abrs())
