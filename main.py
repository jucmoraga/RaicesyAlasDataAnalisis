from procesador import procesar_datos, datos_poblacionales, datos_muestrales
from reporteador import reporte_anexos, reporte_resultados
from muestra import Muestra

def main():
    print("Leyendo respuestas...")
    muestra = Muestra()
    datos_poblacionales(muestra)
    datos_muestrales(muestra)
    print("Procesando datos...")
    resultados = []
    #procesar_datos(muestra.data, resultados)
    print("Generando reporte de resultados...")
    reporte_resultados(muestra)
    reporte_anexos(muestra)
    print("Proceso finalizado")


if __name__ == "__main__":
    main()