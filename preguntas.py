
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
    }
]


def dar_abrs():
    lista_abr = [pregunta["abr"] for pregunta in Preguntas]
    return lista_abr

def dar_texto(abr: str)->str:
    for pregunta in Preguntas:
        if pregunta["abr"] == abr:
            return pregunta["texto"]
    return None
