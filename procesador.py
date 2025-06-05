#alimenta un listado que contiene para cada pregunta:
# codigo y  gráfica de resultados 

from preguntas import dar_abrs, dar_texto
import matplotlib.pyplot as plt
import base64
from io import BytesIO

def procesar_datos(df, resultados: list):
    preguntas = dar_abrs()
    for pregunta in preguntas:
        nuevaPregunta = {
            "abr": pregunta,
            "grafica": generar_grafica(df, pregunta),
        }
        resultados.append(nuevaPregunta)


def generar_grafica(df, pregunta):    

    plt.pie(df[pregunta].value_counts(), 
            labels=df[pregunta].value_counts().index, 
            autopct='%1.1f%%', 
            startangle=0,
            colors=plt.cm.Pastel2.colors)
    plt.title(dar_texto(pregunta),wrap=True, fontsize=14)
    # Guardar la gráfica en un buffer en memoria
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    plt.close()
    buffer.seek(0)

    # Codificar la imagen en base64 para insertarla en HTML
    imagen_base64 = base64.b64encode(buffer.read()).decode('utf-8')
    img_html = f'<img src="data:image/png;base64,{imagen_base64}" alt="Gráfica de Edades"/>'
    return img_html
