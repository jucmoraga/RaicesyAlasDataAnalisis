from reporteador import reporte_anexos, reporte_resultados
from GeneradorData import crear_dataframe
from procesador import procesar_datos

Resultados = []

print("Creando dataframe...")
dataFrame = crear_dataframe()
print("Procesando datos...")
procesar_datos(dataFrame, Resultados)
print("Generando reporte de anexos...")
reporte_anexos(dataFrame)
print("Generando reporte de resultados...")
reporte_resultados(Resultados)
# Verificar Sesgos
