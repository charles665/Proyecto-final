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
        self.campos = ['Nombre','Pan Frances','Pan Queso', 'Pancacho', 'Complejidad Pan Frances', 'Complejidad Pan Quezo', 'Complejidad Pancacho', 'Eficiencia', 'Estado']#Base de datos con laa columnas cambie croasaint por pancacho por que es lo mismo.
        if not os.path.isfile(self.archivo): #si la base de datos no existe la crea y si existe la deja quieta
            with open(self.archivo, 'w', newline='') as f: #lo que hace es que abre el archivo si existe se sobreescribe y si no crea el archivo La w es para sobreescribier tambien hay otras letras
                writer = csv.DictWriter(f, fieldnames=self.campos)
                writer.writeheader() # estas dos ultimas para agregarlas como diccionarios

#Registro
    def registro():
        nombre = str(nombre)#  lo comvertimos a tipo texto
        Com_Pf = round(random.uniform(1, 1.5), 2)  # Usamos uniform para decimales
        Com_Pq = round(random.uniform(1, 1.5), 2)
        Com_Pc = round(random.uniform(1, 1.5), 2)
        ## PARA HACER LA EFICIENCIA LA VOY A HACER EN DOS VARIABLES EL NUMERADOR Y EL DENOMINADOR YA QUE LA FORMULA ES UNA DIVISIÓN
        numerador = (pan_frances*Com_Pf)+(pan_quezo*Com_Pq)+(pancacho*Com_Pc)
        denominador = (Com_Pf+Com_Pq+Com_Pc)
        eficiencia = (numerador/denominador)
        if eficiencia >= 300:
            estado = "Cumple"
        else:
            estado = "No cumple"
        with open(self.archivo, 'a', newline='') as f:  
            writer = csv.DictWriter(f, fieldnames=self.campos)
            writer.writerow({  # Corregi writeheader por writerow
                'Nombre': nombre, 
                'Pan Frances': pan_frances, 
                'Pan Queso': pan_quezo,  
                'Pancacho': pancacho,
                'Complejidad Pan Frances': Com_Pf, 
                'Complejidad Pan Queso': Com_Pq, 
                'Complejidad Pancacho': Com_Pc, 
                'Eficiencia': eficiencia,  
                'Estado': estado})
        return True
    def reporte_general(self):
        # 1 Reporte general de nombre eficiencia y estado 
        df = pd.read_csv(self.archivo)
        # Agrego una verificacion por si no hay datos
        if df.size == 0:
            print ('El archivo esta vacio registre almenos 1 usuario')
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
        plt.pie(conteo_estados.index, colors=['#FF5A33', '#44803F'])
        plt.show()
    def matriz (self):
        df = pd.read_csv(self.archivo)
        productos = df[['Pan Frances', 'Pan Queso', 'Pancacho']]  
        matriz_corr = productos.corr()
        plt.figure()
        sns.heatmap(matriz_corr, annot=True, cmap='coolwarm', fmt=".2f")
        plt.title('Matriz de Correlacion')
        plt.show()
    def reporte_individual(self):
        pass