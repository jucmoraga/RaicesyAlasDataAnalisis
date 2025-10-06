from procesador import datos_poblacionales, datos_muestrales, procesar_resultados
from reporteador import reporte_anexos, reporte_resultados
from muestra import Muestra

def main():
    print("Leyendo respuestas...")
    muestra = Muestra()
    print("Limpiando la muestra...")
    muestra.limpiar()
    print("Calculando información muestral...")
    datos_poblacionales(muestra)
    datos_muestrales(muestra)
    print("Procesando resultados...")
    procesar_resultados(muestra.data, muestra.resultados)
    print("Generando reporte para", len(muestra.resultados), "resultados obtenidos...")
    reporte_resultados(muestra)
    reporte_anexos(muestra)
    print("Proceso finalizado")


if __name__ == "__main__":
    main()