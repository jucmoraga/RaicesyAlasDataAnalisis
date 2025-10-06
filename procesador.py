from resultados import dar_listado_preguntas
import matplotlib.pyplot as plt
import pandas as pd
import base64
from io import BytesIO
from scipy.stats import chisquare, chi2

def procesar_resultados(data, resultados: list):
    encabezados = data.columns.tolist()
    preguntas = dar_listado_preguntas()
    for pregunta in preguntas:
        Resultados_Pregunta = None
        indice = dar_indice(encabezados, pregunta["texto"])
        if not indice:
            print(pregunta["texto"], "no encontrada")
        Resultados_Pregunta = data.iloc[:, indice]
        resultado = {
            "texto": pregunta["texto"],
            "grafica": generar_grafica(Resultados_Pregunta, pregunta),
            "otras respuestas": dar_otras_respuestas(Resultados_Pregunta, pregunta["opciones"]),
            "seccion": pregunta["seccion"],
        }
        resultados.append(resultado)

def dar_otras_respuestas(resultado, opciones)-> list:
    otras = []
    for respuesta in resultado:
        if not respuesta in opciones and respuesta not in otras:
            otras.append(respuesta)
    return otras


def dar_indice(encabezados, pregunta):
    for encabezado in encabezados:
        if pregunta in encabezado:
            return encabezados.index(encabezado)
    return None

def generar_grafica(resultados, pregunta)->str:
    grafica = ""
    if pregunta["seccion"] == 2:
        grafica = generar_torta(resultados, pregunta)
    elif pregunta["seccion"] == 3:
        grafica = generar_barra_horizontal(resultados, pregunta)
    elif pregunta["seccion"] == 4:
        grafica = generar_grafico_barras(resultados, pregunta)
    # elif seccion == 5:
    #     grafica = generar_grafico_barras(df, pregunta)
    # elif seccion == 6:
    #     grafica = generar_histograma(df, pregunta)
    return grafica


def generar_torta(resultado, pregunta)-> str:
    opciones = pregunta["opciones"]
    conteo = resultado.value_counts()
    conteo = conteo.reindex(opciones, fill_value=0)

    if not conteo.sum() == len(resultado):
        print("La suma de los conteos no coincide con el tamaño de la muestra, para la pregunta", pregunta["texto"], "-", conteo.sum(), "vs", len(resultado))

    colores = [plt.cm.Set1(1), plt.cm.Set1(4)]
    fig, ax = plt.subplots(figsize=(10, 6))
    wedges, texts, autotexts = ax.pie(
            conteo,
            labels=conteo.index,
            autopct='%1.1f%%',
            startangle=0,
            colors=colores
            )

    for i, (wedge, autotext) in enumerate(zip(wedges, autotexts)):
        # Obtener la posición del texto del porcentaje
        x, y = autotext.get_position()
        # Agregar el conteo real debajo del porcentaje
        ax.annotate(f'{conteo.iloc[i]}', 
                   xy=(x, y-0.15), 
                   ha='center', 
                   va='center', 
                   fontsize=10)   

    ax.set_title(pregunta["texto"],wrap=True, fontsize=11)
    imagen_codificada = codificar_imagen(fig)
    plt.close(fig)
    return imagen_codificada

def generar_barra_horizontal(resultado, pregunta)->str:
    opciones = pregunta["opciones"]

    resultado = resultado.copy()
    mascara = ~resultado.isin(opciones)
    resultado.loc[mascara] = opciones[-1]
    
    conteos = resultado.value_counts()
    conteos = conteos.reindex(opciones, fill_value=0)

    if not conteos.sum() == len(resultado):
        print("La suma de los conteos no coincide con el tamaño de la muestra, para la pregunta", pregunta["texto"], "-", conteos.sum(), "vs", len(resultado))

    fig, ax = plt.subplots(figsize=(10, 4))
    suma = 0
    for opcion in opciones:
        conteo = conteos[opcion]
        if conteo == 0:
            continue
        ax.barh( 0, 
                conteo, 
                left=suma, 
                label=opcion,
                height=1,
                color = plt.cm.Paired(opciones.index(opcion))
                )
        ax.text(x=suma + conteos[opcion] / 2,
                y = 0,
                s = str(conteo) + (f" ({(conteo/len(resultado)*100):.1f}%)" if conteo/len(resultado) > 0.1 else ""),
                va= 'center',
                ha = 'center')
        suma += conteos[opcion]
    
    ax.set_ylim(-1, 1)
    ax.set_yticks([])
    ax.set_title(pregunta["texto"], wrap=True, fontsize=11)
    ax.legend(loc = 'upper center',
              bbox_to_anchor=(0.5, -0.15))
    fig.subplots_adjust(bottom=0.5) 
    imagen_codificada = codificar_imagen(fig)
    plt.close(fig)
    return imagen_codificada

def generar_grafico_barras(resultados, pregunta)-> str:
    fig, ax = plt.subplots(figsize=(10, 6))
    opciones = pregunta["opciones"]
    conteos = []

    if pregunta["seccion"] == 4:
        for opcion in opciones:
            conteo = int((resultados == opcion).sum())
            conteos.append(conteo)
    elif pregunta["seccion"] == 5:
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
    ax.set_ylim(0, maximo + 40)
    ax.legend(loc = 'upper center',
              bbox_to_anchor=(0.5, -0.15),
              ncol=2) 
    fig.subplots_adjust(bottom=0.4)  
    imagen_codificada = codificar_imagen(fig)
    plt.close(fig)
    return imagen_codificada

def generar_histograma(df, pregunta)-> str:
    fig, ax = plt.subplots(figsize=(10, 6))
    resultados = df[pregunta["abr"]]
    ax.hist(resultados, bins=20, color='blue', alpha=0.7)
    ax.set_title(pregunta["texto"], wrap=True, fontsize=11)
    ax.set_xlabel('Valores')
    ax.set_ylabel('Frecuencia')
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


opciones_facultades = [
    "Facultad de Bellas Artes",
    "Facultad de Ciencia y Tecnología",
    "Facultad de Educación",
    "Facultad de Educación Física",
    "Facultad de Humanidades"
]

opciones_semestre = [
    "Primer a tercer semestre",
    "Cuarto a octavo semestre",
    "Noveno semestre o superior"
]

opciones_genero = [
    "Masculino",
    "Femenino",
    "Otro",
]


def datos_poblacionales(muestra):
    conteos_facultades = [1322, 1751, 1884, 1601, 2006]
    titulo_facultades = "Distribución de la población total según facultad de estudios"
    grafica_facultades = grafica_poblacional(opciones_facultades, conteos_facultades, titulo_facultades)

    conteos_semestre = [3117, 3339, 2108]
    titulo_semestre = "Distribución de la población total según semestre académico"
    grafica_semestre = grafica_poblacional(opciones_semestre, conteos_semestre, titulo_semestre)

    conteos_genero = [3901, 4644, 19]
    titulo_genero = "Distribución de la población total según género"
    grafica_genero = grafica_poblacional(opciones_genero, conteos_genero, titulo_genero)

    muestra.informacion_poblacional.append(grafica_facultades)
    muestra.informacion_poblacional.append(grafica_semestre)
    muestra.informacion_poblacional.append(grafica_genero)

def grafica_poblacional(opciones, conteos, titulo, esperados=None)-> str:
    fig, ax = plt.subplots(figsize=(10, 6))

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
            x_coord = i
            if esperados:
                ax.hlines(y=esperados[i], xmin=x_coord - 0.3, xmax=x_coord + 0.3, colors='red', linewidth=2)

    ax.set_title(titulo, wrap=True, fontsize=11)
    ax.set_xticks([])
    maximo = max(conteos)
    ax.set_ylim(0, maximo + max(conteos)*0.1)
    ax.legend(loc = 'upper center',
              bbox_to_anchor=(0.5, -0.15),
              ncol=2) 
    fig.subplots_adjust(bottom=0.4)  
    imagen_codificada = codificar_imagen(fig)
    plt.close(fig)
    return imagen_codificada

def datos_muestrales(muestra):
    facultades = muestra.data.iloc[:,2]
    conteos_facultades = facultades.value_counts().reindex(opciones_facultades, fill_value=0).tolist()
    if not sum(conteos_facultades) == len(muestra.data):
        print("La suma de los conteos de facultades no coincide con el tamaño de la muestra.")
    titulo_facultades = "Distribución de la muestra según facultad de estudios"
    esperados_facultades = [round(len(muestra.data) * (1322/8564)),
                            round(len(muestra.data) * (1751/8564)),
                            round(len(muestra.data) * (1884/8564)),
                            round(len(muestra.data) * (1601/8564)),
                            round(len(muestra.data) * (2006/8564))]
    grafica_facultades = grafica_poblacional(opciones_facultades, conteos_facultades, titulo_facultades, esperados_facultades)
    tabla_facultades = tabla_datos_muestrales(opciones_facultades, conteos_facultades, esperados_facultades)

    muestra.informacion_muestral.append(grafica_facultades)
    muestra.informacion_muestral.append(tabla_facultades)

    semestres = muestra.data.iloc[:,3]
    conteos_semestre = semestres.value_counts().reindex(opciones_semestre, fill_value=0).tolist()
    if not sum(conteos_semestre) == len(muestra.data):
        print("La suma de los conteos de semestre no coincide con el tamaño de la muestra.")
    titulo_semestre = "Distribución de la muestra según semestre académico"
    esperados_semestre = [round(len(muestra.data) * (3117/8564)),
                          round(len(muestra.data) * (3339/8564)),
                          round(len(muestra.data) * (2108/8564))]

    grafica_semestre = grafica_poblacional(opciones_semestre, conteos_semestre, titulo_semestre, esperados_semestre)
    tabla_semestre = tabla_datos_muestrales(opciones_semestre, conteos_semestre, esperados_semestre)

    muestra.informacion_muestral.append(grafica_semestre)
    muestra.informacion_muestral.append(tabla_semestre)

    generos = muestra.data.iloc[:,5]
    conteos_genero = generos.value_counts().reindex(opciones_genero, fill_value=0).tolist()
    if not sum(conteos_genero) == len(muestra.data):
        print("La suma de los conteos de género no coincide con el tamaño de la muestra.")
    titulo_genero = "Distribución de la muestra según género"
    esperados_genero = [round(len(muestra.data) * (3901/8564)),
                        round(len(muestra.data) * (4644/8564)),
                        round(len(muestra.data) * (19/8564))]
    grafica_genero = grafica_poblacional(opciones_genero, conteos_genero, titulo_genero, esperados_genero)
    tabla_genero = tabla_datos_muestrales(opciones_genero[:2], conteos_genero[:2], esperados_genero[:2])

    muestra.informacion_muestral.append(grafica_genero)
    muestra.informacion_muestral.append(tabla_genero)

def tabla_datos_muestrales(opciones, conteo, esperados)-> str:
    if not sum(conteo) == sum(esperados):
        dif_esperados = sum(conteo) - sum(esperados)
        max_index = esperados.index(max(esperados))
        esperados[max_index] += dif_esperados

    chi_cuadrado, p_valor = chisquare(f_obs=conteo, f_exp=esperados)
    valor_critico = chi2.ppf(1 - 0.05, len(opciones) - 1)
    tabla_html = f"""
    <table style="width:70%; margin-left:15%;border: 1px solid black; border-collapse: collapse; align: center;">
        <tr>
            <th>Grupo poblacional</th>
            <th>Encuestados</th>
            <th>Número esperado</th>
            <th>Diferencia</th>
            <th>Chi-cuadrado</th>
            <th>Contribución al Chi-cuadrado</th>
        </tr>
    """
    for i in range(len(opciones)):
        chi_individual = (conteo[i] - esperados[i])**2 / esperados[i] if esperados[i] > 0 else 0
        tabla_html += f"""
        <tr>
            <td>{opciones[i]}</td>
            <td>{conteo[i]}</td>
            <td>{esperados[i]}</td>
            <td>{abs(conteo[i] - esperados[i])}</td>
            <td>{(chi_individual):.2f}</td>
            <td>{(chi_individual/chi_cuadrado*100 if chi_cuadrado > 0 else 0):.2f}%</td>
        </tr>
        """
    tabla_html += "</table>"

    resultado_prueba = "la muestra pasa la prueba de bondad de ajuste al 95% de confianza." if p_valor > 0.05 else "LA MUESTRA NO PASA LA PRUEBA DE BONDAD DE AJUSTE."

    tabla_html += f"""
    <p class="descriptivo">La muestra obtenida arroja un estadistico Chi-Cuadrado total de {chi_cuadrado:.2f}, frente a un valor crítico de {valor_critico:.2f} y un p-valor de {p_valor:.2f}.
      Lo que implica que {resultado_prueba}</p>
    """
    return tabla_html