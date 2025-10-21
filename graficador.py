import matplotlib.pyplot as plt
import base64
from io import BytesIO
from textwrap import fill

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

def generar_barras_acumuladas(resultado, pregunta)-> str:
    conteos = []
    opciones = pregunta["opciones"]
    fig, ax = plt.subplots(figsize=(10, 6))

    conteo_no_selecciona = int((~resultado.isin(pregunta["opciones"])).sum())
    conteos.append(conteo_no_selecciona)

    for opcion in opciones:
        conteo = int((resultado == opcion).sum())
        conteos.append(conteo)

    opciones = ["Ninguna", "I", "II", "III", "IV", "V"]

    acumulado = 0
    for i, opcion in enumerate(opciones):
        conteo = conteos[i]
        if conteo > 0:    
            ax.bar(opcion, 
                   conteo, 
                   color= "#8d0707", 
                   label=opcion,
                   bottom=acumulado)
            ax.text(x=opcion,
                    y = acumulado + (conteo/3), 
                    s=str(conteo) + (f" ({(conteo/len(resultado)*100):.1f}%)"), 
                    va='bottom', 
                    ha='center', 
                    fontsize=9,
                    color = 'white',
                    fontweight = 'bold')
        acumulado += conteo

    ax.set_title("Opción " + pregunta["texto"] + " De la categoría " + pregunta["categoría"], wrap=True, fontsize=11)
    ax.tick_params(axis='x')
    ax.set_xlabel('Nivel de Preferencia')
    ax.set_ylim(0, acumulado + 10)
    fig.subplots_adjust(bottom=0.4)  
    imagen_codificada = codificar_imagen(fig)
    plt.close(fig)
    return imagen_codificada


def generar_mapa_de_calor(resultado, pregunta)-> str:
    opciones = pregunta["opciones"]

    data = [[0]*5 for _ in range(len(opciones))]

    for resp in resultado:
        for opcion in opciones:
            if resp[opcion] == 1:
                data[opciones.index(opcion)][0] += 1
            elif resp[opcion] == 2:
                data[opciones.index(opcion)][1] += 1
            elif resp[opcion] == 3:
                data[opciones.index(opcion)][2] += 1
            elif resp[opcion] == 4:
                data[opciones.index(opcion)][3] += 1
            elif resp[opcion] == 5:
                data[opciones.index(opcion)][4] += 1


    fig, ax = plt.subplots(figsize=(11, 4))
    cax = ax.imshow(data, cmap='Wistia', aspect='auto')   # heatmap

    preferencias = [1, 2, 3, 4, 5]

    # ticks y etiquetas
    ax.set_xticks(range(len(preferencias))); ax.set_xticklabels(preferencias)
    
    ylabels = []
    for opcion in opciones:
        opcion_recortada = opcion.split('(')[0].strip()
        ylabels.append(opcion_recortada)


    ax.set_yticks(range(len(opciones))); ax.set_yticklabels(ylabels)

    # aumentar espacio a la izquierda para que las etiquetas del eje Y quepan
    fig.subplots_adjust(left=0.35, bottom=0.15, top=0.92, right=0.95)

    # aumentar padding entre tick labels y eje Y
    ax.tick_params(axis='y', which='major', pad=12)

    # anotaciones (valores dentro de cada celda)
    for i in range(len(data)):
        for j in range(len(data[i])):
            ax.text(j, i, str(data[i][j]), ha='center', va='center', color='black', fontsize=9)

    # barra de color y título
    fig.colorbar(cax, ax=ax, label='Valor')
    ax.set_title(pregunta["texto"], wrap=True, fontsize=11)
    imagen_codificada = codificar_imagen(fig)
    plt.close(fig)
    return imagen_codificada


def generar_grafico_barras(resultados, pregunta)-> str:
    fig, ax = plt.subplots(figsize=(10, 6))
    opciones = pregunta["opciones"]
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
                    s=str(conteo) + (f" ({(conteo/len(resultados)*100):.1f}%)"), 
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

def codificar_imagen(img: plt.Figure) -> str:
    buffer = BytesIO()
    img.savefig(buffer, format='png')
    buffer.seek(0)
    imagen_base64 = base64.b64encode(buffer.read()).decode('utf-8')
    img_html = f'<img src="data:image/png;base64,{imagen_base64}"/>'
    return img_html