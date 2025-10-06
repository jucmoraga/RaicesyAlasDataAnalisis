from resultados import Preguntas


def reporte_anexos(muestra):
    # Generar la tabla HTML
    tabla_html = muestra.data.to_html(index=False)

    # Crear el reporte HTML con la gráfica y la tabla
    reporte_html = f"""
    <html>
    <head>
        <title>Resultados Individuales</title>
    </head>
    <body>
        <h1>Proyecto Raices y Alas</h1>
        <h2>Anexos de resultados</h2>
        <h2>Anexo 1: Resultados Individuales</h2>
        {tabla_html}
    </body>
    </html>
    """

    with open('reporte_anexos.html', 'w', encoding='utf-8') as f:
        f.write(reporte_html)

def reporte_resultados(muestra):

    resultados_seccion2 = [resultado for resultado in muestra.resultados if resultado["seccion"] == 2]
    resultados_seccion3 = [resultado for resultado in muestra.resultados if resultado["seccion"] == 3]
    resultados_seccion4 = [resultado for resultado in muestra.resultados if resultado["seccion"] == 4]
    # resultados_seccion5 = [resultado for resultado in resultados if resultado["seccion"] == 5]
    # resultados_seccion6 = [resultado for resultado in resultados if resultado["seccion"] == 6]

    reporte_html = f"""
    <html>
    <head>
        <title>Reporte Resultados PRYA</title>
        <style>
            .descriptivo {{text-align: justify; width: 70%; margin-left:15%}}
            th{{text-align: center; border: 1px solid black;}}
            td{{text-align: center;border: 1px solid black;}}
            ul{{text-align: left; width: 70%; margin-left:15%}}
        </style>
    </head>
    <body style="font-family: Arial, sans-serif; line-height: 1.6;">
        <div style="text-align: center;">
        <h1 style='color: MidnightBlue;'>Universidad Pedagógica Nacional</h1>
        <h2>Proyecto Raices y Alas</h2>
        <h2>Reporte de resultados</h2>
        <p>Con encuestas realizadas hasta el 4 de octubre del 2025</p>
        <h3>Sección 1: Perfil poblacional y muestral</h3>
        <h4>Descripción de la población a estudiar</h4>
        <p class="descriptivo">
            La población a estudiar está conformada por estudiantes de pregrado de la Universidad Pedagógica Nacional,
            matriculados en los distintos programas académicos para el segundo semestre del año 2025. El tamaño de la población
            es de 8.564 estudiantes.
        </p>
        <p class="descriptivo">
            Para identificar las características demográficas de la población y cuidar la representatividad de la muestra,
            se han considerado las siguientes variables de control: género, facultad y semestre académico. 
        </p>
        {muestra.informacion_poblacional[0]}
        {muestra.informacion_poblacional[1]}
        {muestra.informacion_poblacional[2]}
        <h4>Descripción de la muestra obtenida</h4>
        <p class="descriptivo">
            La muestra obtenida está conformada por {len(muestra.data)} estudiantes. Teniendo en cuenta el tamaño de la población
            y el nivel de confianza del 95% definido por el equipo de investigación, el margen de error de la muestra es de
            {muestra.margen_error:.2f}%.
        </p>
        <p class="descriptivo">
            A continuación, se presentan las características demográficas de la muestra obtenida:
        </p>
        """
    for info in muestra.informacion_muestral:
        reporte_html += info

    reporte_html += "<h3>Sección 2: Preguntas de única respuesta: Si o No</h3>"
    
    for resultado in resultados_seccion2:
        reporte_html += f"""
        <img style="display: block;">{resultado["grafica"]}</img>
        """

    reporte_html += """
        <h3>Sección 3: Preguntas de múltiple opción con única respuesta</h3>
        """
    
    for resultado in resultados_seccion3:
        reporte_html += f"""
        <img style="display: block;">{resultado["grafica"]}</img>
        """
        if len(resultado["otras respuestas"]) > 0:
            otras_html = "<ul style='margin-bottom: 80px;'>"
            for resp in resultado["otras respuestas"]:
                otras_html += f"<li>{resp}</li>"
            otras_html += "</ul>"
            reporte_html += f"""
            <p>Otras respuestas proporcionadas por los encuestados a la pregunta {resultado["texto"]}</p>
            {otras_html}
            """

    reporte_html += """
        <h3>Sección 4: Preguntas de enumeración de preferencia del 1 al 5</h3>
        <p>Siendo 5 el máximo nivel de preferencia y 1 el mínimo.</p>
        """

    for resultado in resultados_seccion4:
        reporte_html += f"""
        <img style="display: block;">{resultado["grafica"]}</img>
        """
    
    # reporte_html += """
    #     <h3>Sección 5: Preguntas con opciones multiples de respuesta</h3>
    #     """

    # for resultado in resultados_seccion5:
    #     reporte_html += f"""
    #     <img style="display: block;">{resultado["grafica"]}</img>
    #     """  

    # reporte_html += """
    #     <h3>Sección 6: Preguntas abiertas</h3>
    #     """

    # for resultado in resultados_seccion6:
    #     reporte_html += f"""
    #     <img style="display: block;">{resultado["grafica"]}</img>
    #     """      

    reporte_html += """
        </div>
    </body>
    </html>
    """

    with open('reporte_resultados.html', 'w', encoding='utf-8') as f:
        f.write(reporte_html)    