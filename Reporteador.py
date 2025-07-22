from resultados import Preguntas, dar_texto


def reporte_anexos(df):
    # Generar la tabla HTML
    tabla_html = df.to_html(index=False)

    # Crear el reporte HTML con la gráfica y la tabla
    reporte_html = f"""
    <html>
    <head><title>Cuaderno de Trabajo</title></head>
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

def reporte_resultados(resultados):

    resultados_seccion2 = [resultado for resultado in resultados if resultado["seccion"] == 2]

    reporte_html = f"""
    <html>
    <head><title>Reporte Resultados PRYA.</title>
    </head>
    <body style="font-family: Arial, sans-serif; line-height: 1.6;">
        <div style="text-align: center;">
        <h1 style='color: MidnightBlue;'>Universidad Pedagógica Nacional</h1>
        <h2>Proyecto Raices y Alas. Reporte de resultados.</h2>
        <h3>Sección 2: Preguntas de tipo SI/NO</h3>
        """
    for resultado in resultados_seccion2:
        reporte_html += f"""
        <img style="display: block;">{resultado["grafica"]}</img>
        """

    reporte_html += """
        <h3>Sección 3: Preguntas de múltiple opción con única respuesta</h3>
        """
    
    reporte_html += """
        </div>
    </body>
    </html>
    """

    with open('reporte_resultados.html', 'w', encoding='utf-8') as f:
        f.write(reporte_html)    