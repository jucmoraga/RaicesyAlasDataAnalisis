from muestra import Muestra
from procesador import procesar_datos
from reporteador import reporte_anexos, reporte_resultados

def main():
    print("Creando la muestra...")
    muestra = Muestra()
    muestra.generar_datos_aleatorios()
    print("Procesando datos...")
    resultados = []
    procesar_datos(muestra.data, resultados)
    print("Generando reporte de resultados...")
    reporte_resultados(resultados)
    reporte_anexos(muestra.data)
    print("Proceso finalizado")


if __name__ == "__main__":
    main()