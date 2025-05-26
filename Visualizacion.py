#Importar las librerias necesarias
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import tkinter as tk
import csv
import random
import math
import pandas as pd
import os
import Analisis

## Van las funciones
gestor = Analisis.Panaderia()

#Espacio para las funciones
def mostrar_registro():
 pass

#Ventana principal
ventana = tk.Tk()#inicio la ventana
ventana.title("Pagina de proyectos")#El titulo
ventana.geometry('800x500')#Tamaño
ventana.configure(bg='#FFEC5C')  # Cambiamos el fondo con color
#Frame para los botones
frame_botones = tk.Frame(ventana, bg="#B4CF66", width=1000, height=150)
frame_botones.pack(side="bottom", pady=15)
#Botones
boton1 = tk.Button(frame_botones, text="Registrar", font=("Arial", 10), fg="white", bg="#FF5A33", width=12, command=mostrar_registro)
boton1.grid(row=0, column=0, padx=18, pady=10)

boton2 = tk.Button(frame_botones, text="Reporte general", font=("Arial", 10), fg="white", bg="#FF5A33", width=12, command=mostrar_registro)
boton2.grid(row=0, column=1, padx=18, pady=10)

boton3 = tk.Button(frame_botones, text="Reporte individual", font=("Arial", 10), fg="white", bg="#FF5A33", width=12, command=mostrar_registro)
boton3.grid(row=0, column=2, padx=18, pady=10)

boton4 = tk.Button(frame_botones, text="Salir", font=("Arial", 10), fg="white", bg="#FF5A33", width=12, command=mostrar_registro)
boton4.grid(row=0, column=3, padx=18, pady=10)

#Botones

#cierre de la ventana
ventana.mainloop()