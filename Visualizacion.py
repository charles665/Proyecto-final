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
from tkinter import messagebox

## Van las funciones
gestor = Analisis.Panaderia()

#Espacio para las funciones
def mostrar_registro():
 subventana = tk.Toplevel()
 subventana.title("Registro")
 subventana.geometry("500x300")
 subventana.configure(bg='#146152')
 #frame para el formulario

 #formulario
 tk.Label(subventana, text="Nombre", bg="#B4CF66").grid(row=0, column=0, padx=10, pady=5)
 entry_nombre = tk.Entry(subventana)
 entry_nombre.grid(row=0, column=1, padx=10, pady=5)
    
 tk.Label(subventana, text="Pan Frances", bg="#B4CF66").grid(row=1, column=0, padx=10, pady=5)
 entry_pan_frances = tk.Entry(subventana)
 entry_pan_frances.grid(row=1, column=1, padx=10, pady=5)
    
 tk.Label(subventana, text="Pan Queso", bg="#B4CF66").grid(row=2, column=0, padx=10, pady=5)
 entry_pan_queso = tk.Entry(subventana)
 entry_pan_queso.grid(row=2, column=1, padx=10, pady=5)
    
 tk.Label(subventana, text="Pancacho", bg="#B4CF66").grid(row=3, column=0, padx=10, pady=5)
 entry_pancacho = tk.Entry(subventana)
 entry_pancacho.grid(row=3, column=1, padx=10, pady=5)
 def registrar ():
  nombre = entry_nombre.get().strip()
  pan_frances = entry_pan_frances.get().strip()
  pan_queso = entry_pan_queso.get().strip()
  pancacho = entry_pancacho.get().strip()
  if not all([nombre, pan_frances, pan_queso, pancacho]):
        messagebox.showwarning("Campos vacíos", "Por favor completa todos los campos.")
        return
  if not nombre.replace(" ", "").isalpha():
     messagebox.showwarning("Campos vacíos", "Por favor completa todos los campos.")
     return
  try:
    all([int(pan_frances), float(pan_queso), float(pancacho)])
  except ValueError:
      messagebox.showerror("Error", "Pan frances, Pan queso  y pancacho deben ser numeros ya que corresponden a la cantidad elaborada.")
      return
 boton5 = tk.Button(subventana, text="Registrar", font=("Arial", 10), fg="white", bg="#FF5A33", width=12, command=registrar)
 boton5.grid(row=4, column=0, padx=18, pady=10)

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