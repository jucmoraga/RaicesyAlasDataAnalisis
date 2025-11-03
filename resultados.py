import pandas as pd
import numpy as np

Preguntas = [
    {
        "seccion": 2,
        "texto": "¿Sueles leer afiches, murales, grafitis o anuncios en las paredes de la Universidad?",
        "opciones": ["Sí","No"]
    },
    {
        "seccion": 2,
        "texto": "¿Tienes una biblioteca personal o familiar en tu casa?",
        "opciones": ["Sí","No"]
    },
    {
        "seccion": 2,
        "texto": "Cuando eras pequeño/a ¿Recuerdas que alguien te leyera?",
        "opciones": ["Sí","No"]
    },
    {
        "seccion": 2,
        "texto": "¿Asistes a librerías de la ciudad para hacer compra de libros?",
        "opciones": ["Sí","No"]
    },
    {
        "seccion": 2,
        "texto": "En este año ¿Has leído en voz alta a alguna persona o grupo?",
        "opciones": ["Sí","No"]
    },
    {
        "seccion": 2,
        "texto": "¿Utilizas alguna red social para compartir tus opiniones de lo que lees o enterarte de novedades de lectura?",
        "opciones": ["Sí","No"]
    },
    {
        "seccion": 2,
        "texto": "¿Consideras que tus hábitos de lectura y escritura mejoraron al ingresar a la Universidad?",
        "opciones": ["Sí","No"]
    },
    {
        "seccion": 2,
        "texto": "¿Haces uso de la Inteligencia Artificial Generativa (de ahora en adelante IAG) (Chat GPT, Deep Seek, etc.) para apoyar la comprensión de textos académicos asignados en tus clases?",
        "opciones": ["Sí","No"]
    },
    {
        "seccion": 2,
        "texto": "¿Haces uso de la Inteligencia Artificial Generativa (de ahora en adelante IAG) (Chat GPT, Deep Seek, etc.) para apoyar la escritura de textos académicos asignados en tus clases?",
        "opciones": ["Sí","No"]
    },
    {
        "seccion": 2,
        "texto": "¿Consideras que el uso de la IAG afecta negativamente tu proceso de lectura y escritura?",
        "opciones": ["Sí","No"]
    },
    {
        "seccion": 3,
        "texto": "¿Qué tanto te gusta leer?",
        "opciones": ["Nada","Poco","Medianamente","Mucho"]
    },
    {
        "seccion": 3,
        "texto": "En qué tipo de soporte sueles leer con más frecuencia.",
        "opciones": ["Dispositivos electrónicos (pantallas).","Medios impresos (papel)."]	
    },
    {
        "seccion": 3,
        "texto": "Cuando lees en pantalla ¿Cuál es el principal dispositivo que usas?",
        "opciones": ["a. Computadora de escritorio.", 
                     "b. Computadora portátil/laptop.", 
                     "c. Tableta.",
                     "d. Kindle o similar.", 
                     "e. Smartphone.", 
                     "f. Otro."] 
    },
    {
        "seccion": 3,
        "texto": "Cuando escribes textos de manera autónoma o personal, lo haces de manera más frecuente en:",
        "opciones": ["En papel (cuaderno, libreta, hojas, etc.)", 
                     "En un archivo de Word", 
                     "En alguna aplicación del teléfono (ej. Notas)", 
                     "En un blog propio", 
                     "En Facebook",
                     "En Twitter o similar", 
                     "En Instagram", 
                     "Otro"]
    },
    {
        "seccion": 3,
        "texto": "Cuando escribes textos solicitados por tus profesores, lo haces de manera más frecuente en:",
        "opciones": ["En papel (cuaderno, libretas, hojas, etc.)", 
                     "En un archivo de Word.", 
                     "En una plataforma académica.", 
                     "En alguna aplicación del teléfono (ej. Notas).",  
                     "Otro"]
    },
    {
        "seccion": 3,
        "texto": "Consideras que después de la pandemia Covid-19",
        "opciones": ["Lees más.", "Lees menos.", "Lees igual que antes."]
    },
    {
        "seccion": 3,
        "texto": "¿Con qué frecuencia lees por tu cuenta y gusto de hacerlo?",
        "opciones": ["Nunca.",
                     "Casi nunca.", 
                     "Una vez al mes.", 
                     "Varias veces al mes.", 
                     "Una vez por semana.", 
                     "Varias veces a la semana.", 
                     "Diariamente."]
    },
    {
        "seccion": 3,
        "texto": "¿Con qué frecuencia escribes por tu cuenta y por gusto?",
        "opciones": ["Nunca.",
                     "Casi nunca.", 
                     "Una vez al mes.", 
                     "Varias veces al mes", 
                     "Una vez por semana.", 
                     "Varias veces a la semana.", 
                     "Diariamente."]
    },
    {
        "seccion": 3,
        "texto": "¿Con qué frecuencia tomas notas o haces resumen de los textos que lees?",
        "opciones": ["Nunca.", 
                     "Casi nunca.", 
                     "Algunas veces.", 
                     "Frecuentemente.", 
                     "Siempre."]
    },
    {
        "seccion": 3,
        "texto": "¿Has participado de alguna comunidad lectora (entendida como un grupo de personas que, de manera autónoma y libre, se reúnen a leer en tiempos y espacios compartidos)?",
        "opciones": ["Nunca he participado.",
                     "No participo ahora, pero sí he participado antes.",
                     "Actualmente participo."]
    },
    {
        "seccion": 3,
        "texto": "¿Cuánta afición y gusto por la lectura hay en tu familia?",
        "opciones": ["Hay bastantes lectores y a veces hablamos de libros.",
                     "Apenas hay lectores, y casi nunca se charla sobre lecturas y libros.",
                     "La lectura no es una afición predominante en mi familia."]
    },
    {
        "seccion": 3,
        "texto": "¿Cuánta afición y gusto por la lectura hay en tu grupo de amigas/os o compañeras/os?",
        "opciones": ["Hay bastantes lectores y a veces hablamos de libros.",
                     "Apenas hay lectores, y casi nunca se charla sobre lecturas y libros.",
                     "La lectura no es una afición predominante en mis grupos."]
    },
    {
        "seccion": 3,
        "texto": "Si te leyeron en la infancia ¿Quién que te leyó con mayor frecuencia?",
        "opciones": ["Maestras/os", 
                     "Mi mamá", 
                     "Mi papá", 
                     "Mis hermanos/as", 
                     "Otros familiares", 
                     "Amigos/as", 
                     "Nadie",
                     "Otro"]
    },
    {
        "seccion": 3,
        "texto": "Qué personas consideras han influido de manera más considerable en tus hábitos lectores.",
        "opciones": ["Mis profesoras/es", "Mi familia", "Mis amistades", "Mi novia/o", "Los bibliotecarios", "Booktuber/Bookstagrammer", "Ninguna, es iniciativa propia", "Otro"]
    },
    {
        "seccion": 3,
        "texto": "De las siguientes afirmaciones sobre el uso de plataformas de streaming (Netflix, Prime, etc.) señala con cuál te identificas más:",
        "opciones": ["No hago uso de ninguna plataforma.",
                     "Sí las uso y me han impedido mejorar mi hábito lector.",
                     "Cada día me hacen leer más y mejor.", 
                     "No me influyen como lector o lectora."]
    },
    {
        "seccion": 3,
        "texto": "De las siguientes afirmaciones sobre el uso de redes sociales en general, señala con cuál te identificas más:",
        "opciones": ["No hago uso de redes sociales.",
                     "Sí las uso y me impiden mejorar mi hábito lector.",
                     "Cada día me hacen leer más y mejor.",
                     "No me influyen como lector o lectora."]
    },
    {
        "seccion": 3,
        "texto": "¿Te pasa que la lectura de un libro te provoca interés por una película o serie basada en ese libro o relacionada con este?",
        "opciones": ["Nunca","Casi nunca","Algunas veces","Frecuentemente","Siempre"]
    },
    {
        "seccion": 3,
        "texto": "¿Te pasa que una película o serie basada en un libro despierte tu interés por leer ese libro?",
        "opciones": ["Nunca","Casi nunca","Algunas veces","Frecuentemente","Siempre"]
    },
    {
        "seccion": 3,
        "texto": "¿Qué tan seguido acudes a la Biblioteca Central de la UPN para hacer préstamos de libros?",
        "opciones": ["Nunca","Casi nunca","Algunas veces","Frecuentemente","Siempre"]
    },
    {
        "seccion": 3,
        "texto": "¿Qué tan seguido acudes a otras Bibliotecas para hacer préstamos de libros?",
        "opciones": ["Nunca","Casi nunca","Algunas veces","Frecuentemente","Siempre"]
    },
    {
        "seccion": 4,
        "texto": "De los siguientes géneros textuales enumera de 1 a 5 según la frecuencia de lectura:",
        "opciones": ["Textos narrativos (literatura, crónica, ensayo literario, novela, libro-álbum…).",
                     "Textos periodísticos (noticias, artículos de opinión, crónicas).",
                     "Textos técnicos e instruccionales (que enseñan a hacer cosas).",
                     "Textos jurídicos y/o administrativos (ejercicio de la ciudadanía y los derechos)",
                     "Textos dramatúrgicos (teatro).",
                     "Textos poéticos (poemas, haikus, caligramas).",
                     "Textos epistolares (cartas, correos, mensajes de textos).",
                     "Textos (auto)biográficos o íntimos (Diarios, Memorias).",
                     "Textos propios de tu área.",
                     "Otro"
                     ]
    },
    {
        "seccion": 4,
        "texto": "1.1. Si en la anterior pregunta indicaste 'Otros', por favor describe aquí a cuáles te refieres.",
        "opciones": []
    },
    {
        "seccion": 4,
        "texto": "De los siguientes temas, enumera de 1 a 5 según tu interés de lectura",
        "opciones": ["Temas pedagógicos (para el ejercicio de la docencia).",
                     "Temas de ciencia y teoría (para el desarrollo de la disciplina y la investigación).",
                     "Temas técnicos y tecnológicos (para el uso y desarrollo de este tipo de habilidades).",
                     "Temas de interés cultural (poesía, literatura, reseñas literarias, o de cine, teatro, etc.).",
                     "Temas de política y actualidad: coyuntura de país.",
                     "Temas (auto)biográficos.",
                     "Temas de autoayuda y espiritualidad.",
                     "Otros"]
    },
    {
        "seccion": 4,
        "texto": "2.1. Si en la anterior pregunta indicaste 'Otros', por favor describe aquí a cuáles te refieres.",
        "opciones": []
    },
    {
        "seccion": 4,
        "texto": "En las dos últimas semanas previas a esta encuesta, enumera las escrituras que con más frecuencia hiciste",
        "opciones": ["Escribí textos para un periódico.",
                     "Escribí textos para una revista.",
                     "Escribí en un blog personal.",
                     "Escribí en un foro de discusión.",
                     "Escribí publicaciones en redes sociales.",
                     "Escribí mensajes de chat.",
                     "Escribí textos de trabajo académico solicitados.",
                     "Escribí en mi diario personal.",
                     "Escribí textos literarios.",
                     "Otros ¿Cuáles?"]
    },
    {
        "seccion": 4,
        "texto": "3.1. Si en la anterior pregunta indicaste 'Otros', por favor describe aquí a cuáles te refieres.",
        "opciones": []
    },
    {
        "seccion": 4,
        "texto": "En las dos últimas semanas previas a esta encuesta, enumera las lecturas que con más frecuencia hiciste:",
        "opciones": ["Leí literatura.",
                     "Leí sobre mi disciplina y campo profesional.",
                     "Leí sobre ciencia y divulgación.",
                     "Leí tips y consejos prácticos sobre un tema particular.",
                     "Leí autoayuda.",
                     "Leí opiniones sobre temas de actualidad.",
                     "Leí noticias.",
                     "Leí reseñas culturales de música, cine, teatro o literatura.",
                     "Otro"
        ]
    },
    {
        "seccion": 4,
        "texto": "4.1. Si en la anterior pregunta indicaste 'Otros', por favor describe aquí a cuáles te refieres.",
        "opciones": []
    },
    {
        "seccion": 4,
        "texto": "¿Cuáles son tus géneros literarios favoritos?",
        "opciones": ["Poesía","Teatro", "Ensayo", "Novelas o cuentos de misterio y terror",
                     "Novelas o cuentos de dramas y romances","Novelas o cuentos de aventuras",
                     "Novelas o cuentos de ciencia ficción",
                     "Novelas o cuentos realistas","Novelas o cuentos policiacos",
                     "Novelas históricas", "Novelas testimonio",
                     "Libros-álbum", "Novela gráfica", "Ninguno","Otro"]
    },
    {
        "seccion": 4,
        "texto": "5.1. Si en la anterior pregunta indicaste 'Otros', por favor describe aquí a cuáles te refieres.",
        "opciones": []
    },
    {
        "seccion": 4,
        "texto": "Cuando usas el internet, lo haces principalmente para",
        "opciones": ["Ver películas, series y/o documentales.",
                     "Leer artículos de mi área profesional.",
                     "Leer y acceder a libros de mi área profesional.",
                     "Leer noticias y temas de actualidad.",
                     "Acceder a videoconferencias (clases, seminarios, talleres).",
                     "Ver fotografías o imágenes.",
                     "Escuchar música.",
                     "Visitar museos o bibliotecas virtuales.",
                     "Comunicarme e interactuar con otros en redes sociales.",
                     "Escuchar podcast.",
                     "Escuchar programas de radio.",
                     "Jugar en línea.",
                     "Otro "]
    },
    {
        "seccion": 4,
        "texto": "6.1. Si en la anterior pregunta indicaste 'Otros', por favor describe aquí a cuáles te refieres.",
        "opciones": []
    },
    {
        "seccion": 4,
        "texto": "¿Para cuáles de las siguientes actividades lees con mayor frecuencia en la UPN?",
        "opciones": ["Para las asignaturas de mi carrera.",
                     "Para mi Club, grupo o círculo de lectura.",
                     "Para mi trabajo en un semillero de investigación.",
                     "Para mi grupo de estudio.",
                     "Para realizar exposiciones en las asignaturas.",
                     "Para un curso extracurricular.",
                     "Para participar en eventos académicos (congreso, seminario, coloquio, simposio, etc.).",
                     "Para desarrollar mi proyecto de grado.",
                     "Otro "]
    },
    {
        "seccion": 4,
        "texto": "7.1. Si en la anterior pregunta indicaste 'Otros', por favor describe aquí a cuáles te refieres.",
        "opciones": []
    },
    {
        "seccion": 4,
        "texto": "¿Para cuáles de las siguientes actividades escribes con mayor frecuencia en la UPN?",
        "opciones": ["Para las asignaturas de mi carrera.",
                     "Para mi Club, grupo o círculo de lectura.",
                     "Para mi trabajo en un semillero de investigación.",
                     "Para mi grupo de estudio.",
                     "Para realizar exposiciones en las asignaturas.",
                     "Para un curso extracurricular.",
                     "Para participar en eventos académicos (congreso, seminario, coloquio, simposio, etc.).",
                     "Para desarrollar mi proyecto de grado.",
                     "Otro "]
    },
    {
        "seccion": 4,
        "texto": "8.1. Si en la anterior pregunta indicaste 'Otros', por favor describe aquí a cuáles te refieres.",
        "opciones": []
    },
    {
        "seccion": 4,
        "texto": "Los documentos que más leíste en el semestre pasado, para responder a tus compromisos académicos fueron",
        "opciones": ["Materiales elaborados por los docentes (talleres, guías, artículos).",
                     "Apuntes de clase propios.",
                     "Apuntes de clase de otro (s) compañero (s).",
                     "Resúmenes de libros o de artículos.",
                     "Artículos académicos y científicos.",
                     "Informes de investigación.",
                     "Libros de consulta general (enciclopedias y diccionarios).",
                     "Libros o capítulo de libros, propios de la carrera.",
                     "Literatura (Novelas, cuentos, poesía).",
                     "Blogs u otras páginas web especializados en tu área.",
                     "Otro "]
    },
    {
        "seccion": 4,
        "texto": "9.1. Si en la anterior pregunta indicaste 'Otros', por favor describe aquí a cuáles te refieres.",
        "opciones": []
    },
        {
        "seccion": 4,
        "texto": "Los tipos de documentos que más escribiste el semestre pasado, para responder a tus compromisos académicos fueron",
        "opciones": ["Apuntes de clase.",
                     "Resúmenes.",
                     "Artículos.",
                     "Informes.",
                     "Ensayos.",
                     "Reseñas.",
                     "Relatorías.",
                     "Memorias, protocolos, actas, diarios.",
                     "Textos literarios (Novelas, cuentos, poesía).",
                     "Comentarios o aportes para foros o grupos de discusión presenciales o en línea.",
                     "Otro"]
    },
    {
        "seccion": 4,
        "texto": "10.1. Si en la anterior pregunta indicaste 'Otros', por favor describe aquí a cuáles te refieres.",
        "opciones": []
    },
    {
        "seccion": 4,
        "texto": "Cuando escribes textos académicos ¿para qué te apoyas en la IAG?",
        "opciones": ["Generar textos.",
                     "Generar imágenes.",
                     "Sintetizar o resumir textos.",
                     "Generar presentaciones gráficas, mapas conceptuales, infografías, etc.",
                     "Gestionar información: buscar y contrastar información.",
                     "Apoyar la redacción de textos: indagar sobre el tema que se va a trabajar, pedir ideas, organizar el texto.",
                     "Hacer corrección de estilo (ortografía, gramática, coherencia, cohesión).",
                     "Pasar la bibliografía a normas APA.",
                     "Hacer traducciones de un idioma a otro.",
                     "Proporcionar retroalimentación.",
                     "Mejorar un texto elaborado por mí.",
                     "Otro."]
    }, 
    {
        "seccion": 4,
        "texto": "11.1. Si en la anterior pregunta indicaste 'Otros', por favor describe aquí a cuáles te refieres.",
        "opciones": []
    },
    {
        "seccion": 4,
        "texto": "¿Cuáles son los usos más frecuentes que le das a la IAG para tus actividades, en general?",
        "opciones": ["Resolver preguntas.",
                     "Pedir recomendaciones de libros.",
                     "Redactar de cartas, correos y otros documentos personales.",
                     "Redactar documentos jurídicos como derechos de petición, tutelas, etc.",
                     "Crear personajes e historias ficticias.",
                     "Generar imágenes.",
                     "Conversar sobre asuntos personales.",
                     "Apoyarse para realizar trabajos académicos.",
                     "Apoyarse para resolver tareas laborales.",
                     "Apoyarse para realizar planeaciones, materiales didácticos, etc.",
                     "Realizar contenido audiovisual.",
                     "Otro "]
    },
    {
        "seccion": 4,
        "texto": "12.1. Si en la anterior pregunta indicaste 'Otros', por favor describe aquí a cuáles te refieres.",
        "opciones": []
    },
    {
        "seccion": 5,
        "texto": "De las siguientes IAG ¿Cuáles conoces y utilizas para apoyar la lectura y escritura de textos?",
        "opciones": ["Chat GPT",
                     "Copilot",
                     "Bing",
                     "Claude",
                     "QuillBot",
                     "Gemini",
                     "Writier",
                     "Texta",
                     "Deep Seek",
                     "Merlín",
                     "Wordtune",
                     "Perplexity",
                     "Trinka",
                     "Ninguna",
                     "Otro:"
]       
    },
    {
        "seccion": 5,
        "texto": "¿En qué otros idiomas, diferentes al español, leíste textos el semestre pasado?",
        "opciones": ["Inglés",
                     "Francés",
                     "Portugués",
                     "Alemán",
                     "Italiano",
                     "Solo leí en español",
                     "Ninguno",
                     "Otro:"]       
    },
    {
        "seccion": 5,
        "texto": "¿En qué otros idiomas, diferentes al español, escribiste textos el semestre pasado?",
        "opciones": ["Inglés",
                     "Francés",
                     "Portugués",
                     "Alemán",
                     "Italiano",
                     "Solo escribí en español",
                     "Ninguno",
                     "Otro:"]             
    },
    {
        "seccion": 5,
        "texto": "Cuando lees libros en físico por tu cuenta, ¿cómo los consigues generalmente?",
        "opciones": ["Sueles pedirlos prestados en bibliotecas.",
                     "Sueles pedirlos prestados a los amigos.",
                     "Suelen estar en la biblioteca personal.",
                     "Suelen estar en la biblioteca familiar.",
                     "Te los han regalado.",
                     "Haces trueques.",
                     "Los has obtenido en ferias del libro.",
                     "Otro:"]
    },
    {
        "seccion": 5,
        "texto": "Cuando lees libros en modo digital y por tu cuenta, ¿cómo los consigues generalmente?",
        "opciones": ["Recursos pagos (Google Books, Kindle Store u otros).",
                     "Recursos de libre acceso (El libro total, Libro al Viento u otros).",
                     "Bibliotecas digitales con afiliación (Biblored, Bibliotecas Universitarias, BLAA u otros).",
                     "Los compro.",
                     "De una plataforma en línea los convierto a PDF",
                     "Otro:"]       
    },
    {
        "seccion": 5,
        "texto": "A cuál de las siguientes bibliotecas, asistes para hacer préstamos de libros:",
        "opciones": ["Biblioteca Central de la UPN",
                     "Bibliotecas Públicas",
                     "Otras Bibliotecas Universitarias",
                     "Bibliotecas Comunitarias",
                     "Ninguna",
                     "Otro:"]       
    },
    # {
    #     "id": 65,
    #     "seccion": 6,
    #     "abr": "s6-p1",
    #     "texto": "¿Cuántos libros físicos tienes en tu casa aproximadamente?"
    # },
    # {
    #     "id": 66,
    #     "seccion": 6,
    #     "abr": "s6-p2",
    #     "texto": "¿Cuántos libros digitales tienes aproximadamente?"
    # },
    # {
    #     "id": 67,
    #     "seccion": 6,
    #     "abr": "s6-p3",
    #     "texto": "¿Qué porcentaje de lo que lees, está en versión digital?"
    # },
    # {
    #     "id": 68,
    #     "seccion": 6,
    #     "abr": "s6-p4",
    #     "texto": " ¿Aproximadamente qué cantidad de horas al día empleas para leer?"
    # },
    # {
    #     "id": 69,
    #     "seccion": 6,
    #     "abr": "s6-p5",
    #     "texto": "¿Aproximadamente qué cantidad de horas a al día empleas para escribir?"
    # }
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

