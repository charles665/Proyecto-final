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
        plt.pie(conteo_estados, labels=conteo_estados.index, colors=['#FF5A33', '#44803F'])
        plt.show()
    def matriz (self):
        df = pd.read_csv(self.archivo)
        productos = df[['Pan Frances', 'Pan Queso', 'Pancacho']]  
        matriz_corr = productos.corr()
        plt.figure()
        sns.heatmap(matriz_corr, annot=True, cmap='coolwarm', fmt=".2f")
        plt.title('Matriz de Correlacion')
        plt.show()
    def reporte_individual(self, nom_panadero):
        df = pd.read_csv(self.archivo)      
        panadero = df[df['Nombre'].str.lower() == nom_panadero.lower()]#ignora mayuscalus y minusculas
        ##https://stackoverflow.com/questions/42750551/converting-strings-to-a-lower-case-in-pandas
        if panadero.empty:
            return
        eficiencia = panadero['Eficiencia'].values[0]# toma el primer valor de la columna eficiencia
        estado = panadero['Estado'].values[0] # toma el primer valor de estado
        panes_panadero = {'Pan Frances': int(panadero['Pan Frances']),'Pan Queso': int(operario['Pan Queso']),'Pancacho': int(operario['Pancacho'])} # Lista con los panes producidos por el panadero
        complejida_panadero = {'Pan Frances': float(panadero['Complejidad Pan Frances']),'Pan Queso': float(operario['Complejidad Pan Queso']),'Pancacho': float(operario['Complejidad Pancacho'])}
        eficiencia_final = {}
        i=0
        for i in panes_panadero: 
         cantidad = panes_panadero[i]
         complejidad = complejida_panadero[i]
         resultado = cantidad * complejidad
         eficiencia_final[i] = resultado
    def Grafi_produccion(self, panes_panadero):
        tiposde_pan = ['Pan Frances', 'Pan Queso', 'Pancacho']
        cantidades = list(panes_panadero.values())
        plt.figure()
        plt.bar(tiposde_pan, cantidades, color='orange')
        plt.title('Producción por pan')
        plt.xlabel('Tipo de pan')
        plt.ylabel('Cantidad producida')
        plt.show()
    def Grafi_complejidad(self, complejida_panadero):
        tiposde_pan = ['Pan Frances', 'Pan Queso', 'Pancacho']
        niveles = list(complejida_panadero.values())
        plt.bar(tiposde_pan, niveles, color='skyblue')
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
    


    

   


