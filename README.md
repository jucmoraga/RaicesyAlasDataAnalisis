# Proyecto Raices y Alas - Universidad Pedagógica Nacional

## Descripción:
En el presente repositorio se encuentra el código del modelo estadístico para el análisis de los resultados del proyecto de investigación Raíces y Alas.

### Descripción de Archivos: 

- **Respuestas (carpeta):** contiene el archivo .txt con los resultados de la aplicación de encuestas el cual se descarga directamente del formulario (Google Forms) utilizado para sistematizar la aplicación de encuestas.
- **main.py:** Modulo principal desde el cual se ejecuta el modelo.
- **muestra.py:** Configuración para inicializar la muestra como un dataframe (pandas) tomando los datos de la carpeta de respuestas, y calculando datos muestrales. 
- **procesador.py** Modulo en Python con uso de las librerías pandas, numpy, matplotlib y scipy. Contiene los procedimientos necesarios para procesar el dataframe de la muestra, realizar calculos para perfilar estadísticamente los resultados y crear imágenes descriptivas de los resultados analizados.  
- **reporteador.py** Modulo que crea dos archivos de salida en formato .html los cuales incluyen: La muestra cruda (tabla) llamada **reporte_anexos.html** y la muestra analizada llamada **reporte_resultados.html** (estos archivos también se encuentran en el repositorio)
- **resultados.py** Modulo de Python que contiene toda la configuración para el procesamiento de los resultados (este modulo es importado por el procesador para realizar su trabajo) contiene información sobre: Las preguntas que contiene la encuesta, las opciones válidas de respuesta por cada pregunta, las preguntas que tienen la opción de ser abiertas y en general toda la información paramétrica necesaria para que el procesador pueda valida la calidad del dataframe que está analizando.