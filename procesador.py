from resultados import dar_listado_preguntas
import matplotlib.pyplot as plt
import pandas as pd
import base64
from io import BytesIO

def procesar_datos(df, resultados: list):
    preguntas = dar_listado_preguntas()
    for pregunta in preguntas:
        nuevaPregunta = {
            "abr": pregunta,
            "grafica": generar_grafica(df, pregunta, pregunta["seccion"]),
            "seccion": pregunta["seccion"],
        }
        resultados.append(nuevaPregunta)


def generar_grafica(df, pregunta, seccion)->str:
    grafica = ""
    if seccion == 2:
        grafica = generar_torta(df, pregunta)
    elif seccion == 3:
        grafica = generar_barra_horizontal(df, pregunta)
    elif seccion == 4:
        grafica = generar_distribucion_horizontal(df, pregunta)
    elif seccion == 5:
        grafica = generar_grafico_barras(df, pregunta)
    return grafica


def generar_torta(df,pregunta)-> str:
    opciones = pregunta["opciones"]
    resultados = df[pregunta["abr"]].value_counts()
    resultados = resultados.reindex(opciones, fill_value=0)
    colores = [plt.cm.Set1(1), plt.cm.Set1(0)]
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.pie(
            resultados,
            labels=resultados.index,
            autopct='%1.1f%%',
            startangle=0,
            colors=colores
            )
    ax.set_title(pregunta["texto"],wrap=True, fontsize=11)
    imagen_codificada = codificar_imagen(fig)
    plt.close(fig)
    return imagen_codificada

def generar_barra_horizontal(df, pregunta)->str:
    opciones = pregunta["opciones"]
    resultados = df[pregunta["abr"]].value_counts()
    resultados = resultados.reindex(opciones, fill_value=0)
    
    fig, ax = plt.subplots(figsize=(10, 6))
    suma = 0
    for opcion in opciones:
        conteo = resultados[opcion]
        if conteo == 0:
            conteo = ""
        ax.barh( 0, 
                resultados[opcion], 
                left=suma, 
                label=opcion,
                height=1,
                color = plt.cm.Paired(opciones.index(opcion))
                )
        ax.text(x=suma + resultados[opcion] / 2,
                y = 0,
                s = conteo,
                va= 'center',
                ha = 'center')
        suma += resultados[opcion]
    
    ax.set_ylim(-1, 1)
    ax.set_yticks([])
    ax.set_title(pregunta["texto"], wrap=True, fontsize=11)
    ax.legend(loc = 'upper center',
              bbox_to_anchor=(0.5, -0.15))
    fig.subplots_adjust(bottom=0.5) 
    imagen_codificada = codificar_imagen(fig)
    plt.close(fig)
    return imagen_codificada

def generar_distribucion_horizontal(df, pregunta)->str:
    opciones = pregunta["opciones"]
    resultados = df[pregunta["abr"]].apply(pd.Series)
    columnas = ["Preferencia 1", "Preferencia 2", "Preferencia 3", "Preferencia 4", "Preferencia 5"]
    resultados.columns = columnas

    fig, ax = plt.subplots(figsize=(10, 6)) 

    for columna in columnas:
        suma = 0
        conteos = resultados[columna].value_counts()
        for opcion in opciones:
            conteo = conteos[opcion] if opcion in conteos else 0
            conteo_label = conteo if conteo != 0 else ""
            label = opcion if columna == "Preferencia 1" else None
            ax.barh(
                    columna, 
                    conteo, 
                    left=suma, 
                    label=label,
                    color=plt.cm.tab20(opciones.index(opcion)))
            ax.text(x=suma + conteo / 2,
                y = columna,
                s = conteo_label,
                va= 'center',
                ha = 'center')
            suma += conteo
            
    ax.set_title(pregunta["texto"], wrap=True, fontsize=11)
    ax.legend(loc = 'upper center',bbox_to_anchor=(0.5, -0.15))
    fig.subplots_adjust(bottom=0.6) 
    imagen_codificada = codificar_imagen(fig)
    plt.close(fig)
    return imagen_codificada

def generar_grafico_barras(df, pregunta)-> str:
    fig, ax = plt.subplots(figsize=(10, 6))
    opciones = pregunta["opciones"]
    resultados = df[pregunta["abr"]]
    conteos = []

    for opcion in opciones:
        conteo = 0
        for resultado in resultados:
            if isinstance(resultado, list) and opcion in resultado:
                conteo += 1
        conteos.append(conteo)


    for i, opcion in enumerate(opciones):
        conteo = conteos[i]
        if conteo > 0:    
            ax.bar(opcion, 
                   conteo, 
                   color=plt.cm.tab20.colors[i], label=opcion)
            ax.text(x=opcion,
                    y = conteo, 
                    s=conteo, 
                    va='bottom', 
                    ha='center', 
                    fontsize=9)
    
    ax.set_title(pregunta["texto"], wrap=True, fontsize=11)
    ax.set_xticks([])
    maximo = max(conteos)
    ax.set_ylim(0, maximo + 5)
    ax.legend(loc = 'upper center',
              bbox_to_anchor=(0.5, -0.15),
              ncol=2) 
    fig.subplots_adjust(bottom=0.4)  
    imagen_codificada = codificar_imagen(fig)
    plt.close(fig)
    return imagen_codificada

def codificar_imagen(img: plt.Figure) -> str:
    buffer = BytesIO()
    img.savefig(buffer, format='png')
    buffer.seek(0)
    imagen_base64 = base64.b64encode(buffer.read()).decode('utf-8')
    img_html = f'<img src="data:image/png;base64,{imagen_base64}"/>'
    return img_html


