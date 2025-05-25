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

#Crear la base de datos
class Panaderia:
    def __init__(self, archivo='panaderia.csv'):
        self.archivo = archivo
        self.campos = ['Nombre','Pan Frances','Pan Queso', 'Pancacho']
        if not os.path.isfile(self.archivo):
            with open(self.archivo, 'w', newline='') as f: #lo que hace es que abre el archivo si existe se sobreescribe y si no crea el archivo La w es para sobreescribier tambien hay otras letras
                writer = csv.DictWriter(f, fieldnames=self.campos)
                writer.writeheader()

#Registro
   



#Reporte general


#Reporte individual


#Salir
