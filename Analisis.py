#Importo las librerias que voy a utilizar
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import tkinter as tk
import csv
import random
import math
import pandas as pd
import os
import tkinter as tk

#Crear la base de datos
class Panaderia: # clase
    def __init__(self, archivo='panaderia.csv'): # metodo
        self.archivo = archivo 
        self.campos = ['Nombre','Pan Frances','Pan Queso', 'Pancacho', 'Complejidad Pan Frances', 'Complejidad Pan Queso', 'Complejidad Pancacho', 'Eficiencia', 'Estado']#Base de datos con laa columnas cambie croasaint por pancacho por que es lo mismo.
        if not os.path.isfile(self.archivo): #si la base de datos no existe la crea y si existe la deja quieta
            ## https://www-geeksforgeeks-org.translate.goog/python-os-path-isfile-method/?_x_tr_sl=en&_x_tr_tl=es&_x_tr_hl=es&_x_tr_pto=tc
            with open(self.archivo, 'w', newline='') as f: #lo que hace es que abre el archivo si existe se sobreescribe y si no crea el archivo La w es para sobreescribier tambien hay otras letras
                writer = csv.DictWriter(f, fieldnames=self.campos)
                writer.writeheader() # estas dos ultimas para agregarlas como diccionarios

#Registro
    def registro(self, nombre, pan_frances, pan_queso, pancacho):
        pan_frances = int(pan_frances)
        pan_queso = int(pan_queso)
        pancacho = int(pancacho)
        nombre = str(nombre)#  lo comvertimos a tipo texto
        Com_Pf = round(random.uniform(1, 1.5), 2)  # Usamos uniform para decimales
        Com_Pq = round(random.uniform(1, 1.5), 2)
        Com_Pc = round(random.uniform(1, 1.5), 2)
        ## PARA HACER LA EFICIENCIA LA VOY A HACER EN DOS VARIABLES EL NUMERADOR Y EL DENOMINADOR YA QUE LA FORMULA ES UNA DIVISIÓN
        numerador = (pan_frances*Com_Pf)+(pan_queso*Com_Pq)+(pancacho*Com_Pc)
        denominador = (Com_Pf+Com_Pq+Com_Pc)
        eficiencia = (numerador/denominador)
        if eficiencia >= 300:
            estado = "Cumple"
        else:
            estado = "No cumple"
        with open(self.archivo, 'a', newline='') as f:
         ## https://stackoverflow.com/questions/2918362/writing-string-to-a-file-on-a-new-line-every-time
         writer = csv.DictWriter(f, fieldnames=self.campos)
         writer.writerow({
            'Nombre': nombre,
            'Pan Frances': pan_frances,
            'Pan Queso': pan_queso,
            'Pancacho': pancacho,
            'Complejidad Pan Frances': Com_Pf,
            'Complejidad Pan Queso': Com_Pq,
            'Complejidad Pancacho': Com_Pc,
            'Eficiencia': eficiencia,
            'Estado': estado
        })
        return True
    def reporte_general(self):
        # 1 Reporte general de nombre eficiencia y estado 
        df = pd.read_csv(self.archivo)
        # Agrego una verificacion por si no hay datos
        if df.size == 0:
        ## https://www.geeksforgeeks.org/python-pandas-df-size-df-shape-and-df-ndim/
            return
        else:
            reporte_g = df[['Nombre', 'Eficiencia', 'Estado']]
        # 2 Estadisticas relevantes (Utilizo describe)
        estadisticas_descriptivas = df[['Nombre', 'Eficiencia', 'Estado']].describe()
        # 3 Promedio de eficacia
        lista_eficiencia = df['Eficiencia'].tolist() # Convertimos a lista para sacar el promedio
        promedio_ef = sum(lista_eficiencia)/len(lista_eficiencia) 
        promedio_ef_melo = round(promedio_ef, 2)
    ##GRAFICOS
    #Torta
    def grafico_torta (self):
        df = pd.read_csv(self.archivo)
        conteo_estados = df['Estado'].value_counts()
        plt.figure()
        plt.title('Grafica trabajadores que cumplieron')
        plt.pie(conteo_estados, labels=conteo_estados.index, colors=['#FFEC5C', '#146152'])
        plt.show()
    def matriz (self):
        df = pd.read_csv(self.archivo)
        productos = df[['Pan Frances', 'Pan Queso', 'Pancacho']]  
        matriz_corr = productos.corr()
        plt.figure()
        sns.heatmap(matriz_corr, annot=True, cmap='coolwarm', fmt=".2f")
        ## https://seaborn.pydata.org/generated/seaborn.heatmap.html
        plt.title('Matriz de Correlacion')
        plt.show()
    def reporte_individual(self, nom_panadero):
      df = pd.read_csv(self.archivo)      
      panadero = df[df['Nombre'].str.lower() == nom_panadero.lower()] #toma nombre llo convierte a minuscula y luego todo nom_panadero 
      ## https://stackoverflow.com/questions/19726029/how-can-i-make-pandas-dataframe-column-headers-all-lowercase
      if panadero.empty:
        ##https://stackoverflow.com/questions/42750551/converting-strings-to-a-lower-case-in-pandas
          return 
      eficiencia = panadero['Eficiencia'].values[0]
      estado = panadero['Estado'].values[0]
      panes_panadero = {'Pan Frances': int(panadero['Pan Frances'].values[0]),'Pan Queso': int(panadero['Pan Queso'].values[0]),'Pancacho': int(panadero['Pancacho'].values[0])} # diccionarios que toman el primer valor de cada pan
      complejida_panadero = {'Pan Frances': float(panadero['Complejidad Pan Frances'].values[0]),'Pan Queso': float(panadero['Complejidad Pan Quezo'].values[0]),'Pancacho': float(panadero['Complejidad Pancacho'].values[0])}
      eficiencia_final = {}
      for pan in panes_panadero:
          cantidad = panes_panadero[pan]
          complejidad = complejida_panadero[pan]
          eficiencia_final[pan] = cantidad * complejidad
      return eficiencia, estado, panes_panadero, complejida_panadero, eficiencia_final # regreso los valores
    def Grafi_produccion(self, panes_panadero):
        tiposde_pan = ['Pan Frances', 'Pan Queso', 'Pancacho'] # creo una lista
        cantidades = list(panes_panadero.values()) # crea una lista donde las keys son los tipos de panes
        ##https://stackoverflow.com/questions/16228248/how-can-i-get-list-of-values-from-dict
        plt.figure()
        plt.bar(tiposde_pan, cantidades, color='#B4CF66')
        plt.title('Producción por pan')
        plt.xlabel('Tipo de pan')
        plt.ylabel('Cantidad producida')
        plt.show()
    def Grafi_complejidad(self, complejida_panadero):
        tiposde_pan = ['Pan Frances', 'Pan Queso', 'Pancacho']
        niveles = list(complejida_panadero.values())
        plt.bar(tiposde_pan, niveles, color='skyblue')
        ##https://stackoverflow.com/questions/16228248/how-can-i-get-list-of-values-from-dict
        plt.title(' Complejidad')
        plt.xlabel('Tipo de pan')
        plt.ylabel('Nivel de complejidad')
        plt.show()
    def Grafi_eficiencia(self, eficiencia_final):
        tiposde_pan = ['Pan Frances', 'Pan Queso', 'Pancacho']
        valor_efici = list(eficiencia_final.values())
        plt.bar(tiposde_pan, valor_efici, color='green')
        plt.title('Por eficiencia')
        plt.xlabel('Tipo de pan')
        plt.ylabel('Valor eficiencia (producción × complejidad)')
        plt.show()
    


    

   


