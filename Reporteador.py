import matplotlib.pyplot as plt
import base64
from io import BytesIO


def reporte_anexos(df):
    # Crear la gráfica
    # plt.bar(df['Nombre'], df['Edad'])
    # plt.title('Edades de las Personas')
    # plt.xlabel('Nombre')
    # plt.ylabel('Edad')

    # # Guardar la gráfica en un buffer en memoria
    # buffer = BytesIO()
    # plt.savefig(buffer, format='png')
    # plt.close()
    # buffer.seek(0)

    # # Codificar la imagen en base64 para insertarla en HTML
    # imagen_base64 = base64.b64encode(buffer.read()).decode('utf-8')
    # img_html = f'<img src="data:image/png;base64,{imagen_base64}" alt="Gráfica de Edades"/>'

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