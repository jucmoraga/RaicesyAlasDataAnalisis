import pandas as pd
import math

class Muestra():
    def __init__(self):
        self.data= pd.read_csv('respuestas/resultados_041025.txt', delimiter=',')
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