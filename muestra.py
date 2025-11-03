import pandas as pd
import math
from resultados import Preguntas

class Muestra():
    def __init__(self):
        self.data= pd.read_csv('respuestas/resultados_281025.csv', delimiter=',')
        self.resultados = []
        self.informacion_poblacional = []
        self.informacion_muestral = []
        self.margen_error = self.calculo_margen()

    def calculo_margen(self):
        z = 1.96           # 95% de confianza
        s = 0.25           # desviación muestral
        n = self.data.shape[0]            # tamaño de la muestra
        N = 8564          # tamaño de la población
        margen_error = z * math.sqrt(s/n) * math.sqrt((N - n) / (N - 1))
        return margen_error * 100
    
    def limpiar(self):
        self.data.iloc[:,3] = self.data.iloc[:,3].replace(
            "Cuarto a sexto semestre", 
            "Cuarto a octavo semestre"
        )
        for i in range (0, len(self.data)):
            if self.data.iloc[i,5] not in ["Masculino", "Femenino"]:
                self.data.iloc[i,5] = "Otro"
        self.consolidar_seccion_4()
    
    def consolidar_seccion_4(self):
        preguntas_seccion_4 = [p for p in Preguntas if p["seccion"] == 4]
        columnas = self.data.columns.tolist()
        for pregunta in preguntas_seccion_4:
            opciones = pregunta["opciones"]
            if opciones is None or len(opciones) == 0:
                continue
            columnas_consolidar = []
            for columna in columnas:
                if pregunta["texto"] in columna:
                    for opcion in opciones:
                        if opcion in columna:
                            columnas_consolidar.append([opcion,columna])
            
            nueva_columna = []
            for i in range(0, len(self.data)):
                respuestas_usuario = {}
                for opcion, columna in columnas_consolidar:
                    respuestas_usuario[opcion] = self.data.iloc[i][columna]
                nueva_columna.append(respuestas_usuario)
            nombre_nueva_columna = pregunta["texto"] + " - Consolidado"
            self.data[nombre_nueva_columna] = nueva_columna
            self.data.drop(columns=[columna for _, columna in columnas_consolidar], inplace=True)

