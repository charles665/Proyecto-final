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
        Com_Pf = round(random.randint(1, 1,5),2) # generamos el numero aleatorio entre 1 y 1,5
        Com_Pq = round(random.randint(1, 1,5),2)
        Com_Pc = round(random.randint(1, 1,5),2)
        while True: # bucle infinito
            try:# validaciones
                pan_frances = int(pan_frances) #convertimos a entero
                if pan_frances >500: # verificacamos que sea mayor que 500
                    messagebox.showerror("Error", "El numero debe ser menor o igual a 500") # mensaje de error si es mayor que 500
                else:
                    messagebox.showinfo("Exito", "Numero registrado") # si hizo las cosas bien
                    break # sale del bucle
            except ValueError:
                messagebox.showerror("Error", "El valor debe ser un numero") # no es numero
        while True: 
            try:
                pan_quezo = int(pan_quezo) 
                if pan_quezo >500:
                    messagebox.showerror("Error", "El numero debe ser menor o igual a 500") 
                else:
                    messagebox.showinfo("Exito", "Numero registrado") 
                    break 
            except ValueError:
                messagebox.showerror("Error", "El numero debe ser entero")
        while True: 
            try:
                pancacho = int(pancacho) 
                if pancacho >500:
                    messagebox.showerror("Error", "El numero debe ser menor o igual a 500") 
                else:
                    messagebox.showinfo("Exito", "Numero registrado") 
                    break 
            except ValueError:
                messagebox.showerror("Error", "El numero debe ser entero")
        ## PARA HACER LA EFICIENCIA LA VOY A HACER EN DOS VARIABLES EL NUMERADOR Y EL DENOMINADOR YA QUE LA FORMULA ES UNA DIVISIÓN
        numerador = (pan_frances*Com_Pf)+(pan_quezo*Com_Pq)+(pancacho*Com_Pc)
        denominador = (Com_Pf+Com_Pq+Com_Pc)
        eficiencia = (numerador/denominador)
        if eficiencia >= 300:
            estado = "Cumple"
        else:
            estado = "No cumple"
        with open(self.archivo, 'a', newline='')as f:  
            writer = csv.DictWriter(f, fieldnames=self.campos)
            writer.writeheader({
                'Nombre': nombre, 
                'Pan Frances': pan_frances, 
                'Pan Quezo': pan_quezo, 
                'Pancacho': pancacho,
                'Complejidad Pan Frances': Com_Pf, 
                'Complejidad Pan Quezo': Com_Pq, 
                'Complejidad Pancacho': Com_Pc, 
                'Eficiecncia': eficiencia, 
                'Estado': estado})
    
            



#Reporte general


#Reporte individual


#Salir
