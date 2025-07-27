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
    {
        id: 23,
        "seccion": 3,
        "abr": "s3-p2",
        "texto": "En qué tipo de soporte sueles leer con más frecuencia.",
        "opciones": ["Dispositivos electrónicos (pantallas).","Medios impresos (papel)"]	
    },
    {
        id: 24,
        "seccion": 3,
        "abr": "s3-p3",
        "texto": "¿Qué tanto te gusta escribir?",
        "opciones": ["Nada","Poco","Medianamente","Mucho"]
    },
    {
        id: 25,
        "seccion": 3,
        "abr": "s3-p4",
        "texto": "En qué tipo de soporte sueles escribir con más frecuencia.",
        "opciones": ["Dispositivos electrónicos (pantallas).","Medios impresos (papel)"]
    },
    {
        id: 26,
        "seccion": 3,
        "abr": "s3-p5",
        "texto": "Cuándo lees en pantalla, ¿cuál es el principal dispositivo que usas?",
        "opciones": ["Computadora de escritorio", "Computadora portátil/Laptop", "Tableta","Kindle o similar", "Smartphone", "Otro"] 
    },
    {
        id: 27,
        "seccion": 3,
        "abr": "s3-p6",
        "texto": "Cuando escribes textos de manera autónoma o personal lo haces de manera más frecuente en: ",
        "opciones": ["En un cuaderno", "En un archivo de Word", "En notas del teléfono", "En WhatsApp", "En un blog propio", "En Facebook","En Twitter o similar", "En Instagram", "Otra"]
    },
    {
        id: 28,
        "seccion": 3,
        "abr": "s3-p7",
        "texto": "Cuando escribes textos solicitados por tus profesores, lo haces de manera más frecuente en: ",
        "opciones": ["En un cuaderno", "En un archivo de Word", "En una plataforma académica", "En notas del teléfono", "En WhatsApp", "Otra"]
    },
    {
        id: 29,
        "seccion": 3,
        "abr": "s3-p8",
        "texto": "Consideras que después de la pandemia Covid-19",
        "opciones": ["Lees más", "Lees menos", "Lees igual que antes"]
    },
    {
        id: 30,
        "seccion": 3,
        "abr": "s3-p9",
        "texto": "¿Cuándo lees por tu cuenta y gusto de hacerlo, con qué frecuencia lo haces?",
        "opciones": ["Nunca","Casi nunca", "Una vez al mes", "Varias veces al mes", "Una vez por semana", "Varias veces por semana", "Diariamente"]
    },
    {
        id: 31,
        "seccion": 3,
        "abr": "s3-p10",
        "texto": "¿Cuándo escribes por tu cuenta y gusto de hacerlo, con qué frecuencia lo haces?",
        "opciones": ["Nunca","Casi nunca", "Una vez al mes", "Varias veces al mes", "Una vez por semana", "Varias veces por semana", "Diariamente"]
    },
    {
        id: 32,
        "seccion": 3,
        "abr": "s3-p11",
        "texto": "¿Tomas notas o resumes a partir de las lecturas que haces?",
        "opciones": ["Nunca", "Casi nunca", "Algunas veces", "Fecuentemente", "Siempre"]
    },
    {
        id: 33,
        "seccion": 3,
        "abr": "s3-p12",
        "texto": "Cuando escuchas hablar de lectoras, lectores, o de comunidad lectora (entendida como un grupo de personas que de manera autónoma y libre se reúnen a leer en tiempos y espacios compartidos), tu:",
        "opciones": ["Te sientes incluido como lector/a", "No te sientes incluido/a", "No sabes a qué se refieren"]
    },
    {
        id: 34,
        "seccion": 3,
        "abr": "s3-p13",
        "texto": "¿Cuánta afición y gusto por la lectura hay en tu familia?",
        "opciones": ["Hay bastantes lectores y a veces hablamos de libros.",
                     "Apenas hay lectores, y casi nunca se charla sobre lecturas y libros.",
                     "La lectura no es una afición predominante en mi familia."]
    },
    {
        id: 35,
        "seccion": 3,
        "abr": "s3-p14",
        "texto": "¿Cuánta afición y gusto por la lectura hay en tu grupo de amigos/as o compañeras/os?",
        "opciones": ["Hay bastantes lectores y a veces hablamos de libros.",
                     "Apenas hay lectores, y casi nunca se charla sobre lecturas y libros.",
                     "La lectura no es una afición predominante en mis grupos."]
    },
    {
        id: 36,
        "seccion": 3,
        "abr": "s3-p15",
        "texto": "Si te leyeron en la infancia ¿Quién que te leyó con mayor frecuencia?",
        "opciones": ["Mis maestras/os", "Mi mamá", "Mi papá", "Mis hermanos/as", "Otros familiares", "Amigos/as", "Naide"]
    },
    {
        id: 37,
        "seccion": 3,
        "abr": "s3-p16",
        "texto": "Qué personas consideras han influido de manera considerable en tus hábitos lectores.",
        "opciones": ["Mis profesoras/es", "Mi familia", "Mis amistades", "Mi novia/o", "Los bibliotecarios", "Booktuber/Bookstagrammer", "Ninguna, es iniciativa propia", "Otro"]
    },
    {
        id: 38,
        "seccion": 3,
        "abr": "s3-p17",
        "texto": "De las siguientes afirmaciones sobre el uso de plataformas de streaming (Netflix, Prime, etc.) señala con cuál te identificas más:",
        "opciones": ["Te impiden mejorar tu hábito lector.", "Cada día te hacen leer más y mejor", "No te influyen como lector o lectora"]
    },
    {
        id: 39,
        "seccion": 3,
        "abr": "s3-p18",
        "texto": "De las siguientes afirmaciones sobre el uso de redes sociales en general, señala con cuál te identificas más:",
        "opciones": ["Te impiden mejorar tu hábito lector.", "Cada día te hacen leer más y mejor", "No te influyen como lector o lectora"]
    },
    {
        id: 40,
        "seccion": 3,
        "abr": "s3-p19",
        "texto": "¿Te pasa que la lectura de un libro te provoca interés por una película, serie o exposición basada en ese libro o relacionada con este?",
        "opciones": ["Nunca","Casi nunca","Algunas veces","Frecuentemente","Siempre"]
    },
    {
        id: 41,
        "seccion": 3,
        "abr": "s3-p20",
        "texto": "¿Te pasa que una película o serie o exposición basada en un libro despierte tu interés por leer ese libro? ",
        "opciones": ["Nunca","Casi nunca","Algunas veces","Frecuentemente","Siempre"]
    },
    {
        id: 42,
        "seccion": 3,
        "abr": "s3-p21",
        "texto": "Cuando lees libros en físico por tu cuenta, ¿cómo los consigues generalmente?:",
        "opciones": ["Sueles pedirlos prestados en bibliotecas.","Sueles pedirlos prestados a los amigos.", "Suelen estar en la biblioteca personal.", "Suelen estar en la biblioteca familiar.", "Te los han regalado.","Haces trueques", "Los has obtenido en ferias del libro", "Otra"]
    },
    {
        id: 43,
        "seccion": 3,
        "abr": "s3-p22",
        "texto": "Cuando lees libros en digital por tu cuenta, ¿cómo los consigues generalmente?:",
        "opciones": ["Recursos pagos (Google Books, Kindle Store u otros).",
                     "Recursos de libre acceso (El libro total, Libro al Viento u otros).",
                     "Bibliotecas digitales con afiliación (Biblored, Bibliotecas Universitarias, BLAA u otros). ",
                     "Otros"]
    },
    {
        id: 44,
        "seccion": 3,
        "abr": "s3-p23",
        "texto": "¿Qué tanto dependes de la IAG (Chat GPT, Deep Seek, etc.) para el desarrollo de tus actividades académicas?",
        "opciones": ["Nada","Poco","Medianamente","Mucho"]
    },
    {
        id: 45,
        "seccion": 3,
        "abr": "s3-p24",
        "texto": "¿Qué tan seguido acudes a la Biblioteca Central de la UPN para hacer préstamos de libros?",
        "opciones": ["Nunca","Casi nunca","Algunas veces","Frecuentemente","Siempre"]
    },
    {
        id: 46,
        "seccion": 3,
        "abr": "s3-p25",
        "texto": "Qué tan seguido acudes a Bibliotecas Públicas para hacer préstamos de libros?",
        "opciones": ["Nunca","Casi nunca","Algunas veces","Frecuentemente","Siempre"]
    },
    {
        id: 47,
        "seccion": 4,
        "abr": "s4-p1",
        "texto": "De los siguientes géneros textuales enumera de 1 a 5 según la frecuencia de lectura",
        "opciones": ["Textos narrativos (literatura, crónica, ensayo literario, novela, libro-álbum…). ",
                     "Textos periodísticos (noticias, artículos de opinión, crónicas). ",
                     "Textos técnicos e instruccionales (que enseñan a hacer cosas). ",
                     "Textos jurídicos y/o administrativos (ejercicio de la ciudadanía y los derechos)",
                     "Textos dramatúrgicos (teatro). ",
                     "Textos poéticos (poemas, haikus, caligramas).",
                     "Textos epistolares (cartas, correos, mensajes de textos). ",
                     "Textos (auto)biográficos o íntimos (Diarios, Memorias). ",
                     "Textos propios de tu área.",
                     "Otros"]
    },
    # {
    #     id: 48,
    #     "seccion": 4,
    #     "abr": "s4-p2",
    #     "texto": "",
    #     "opciones": []
    # },
    # {
    #     id: 49,
    #     "seccion": 4,
    #     "abr": "s4-p3",
    #     "texto": "",
    #     "opciones": []
    # },
    # {
    #     id: 50,
    #     "seccion": 4,
    #     "abr": "s4-p4",
    #     "texto": "",
    #     "opciones": []
    # },
    # {
    #     id: 51,
    #     "seccion": 4,
    #     "abr": "s4-p5",
    #     "texto": "",
    #     "opciones": []
    # },
    # {
    #     id: 52,
    #     "seccion": 4,
    #     "abr": "s4-p6",
    #     "texto": "",
    #     "opciones": []
    # },
    # {
    #     id: 53,
    #     "seccion": 4,
    #     "abr": "s4-p7",
    #     "texto": "",
    #     "opciones": []
    # },
    # {
    #     id: 54,
    #     "seccion": 4,
    #     "abr": "s4-p8",
    #     "texto": "",
    #     "opciones": []
    # },
    # {
    #     id: 55,
    #     "seccion": 4,
    #     "abr": "s4-p9",
    #     "texto": "",
    #     "opciones": []
    # },
    #     {
    #     id: 56,
    #     "seccion": 4,
    #     "abr": "s4-p10",
    #     "texto": "",
    #     "opciones": []
    # },
]

def dar_abrs():
    lista_abr = [pregunta["abr"] for pregunta in Preguntas]
    return lista_abr

def dar_listado_preguntas()->list:
    return [pregunta for pregunta in Preguntas]

def dar_pregunta(abr: str)->str:
    for pregunta in Preguntas:
        if pregunta["abr"] == abr:
            return pregunta
    return None

def respuestas_aleatorias():
    respuestas = []
    for pregunta in Preguntas:
        if pregunta["seccion"] == 2 or pregunta["seccion"] == 3:
            respuesta = np.random.choice(pregunta["opciones"])
        elif pregunta["seccion"] == 4:
            respuesta = np.random.choice(pregunta["opciones"], size=5, replace=False).tolist()
        respuestas.append(respuesta)

    return pd.DataFrame([respuestas], columns=dar_abrs())
