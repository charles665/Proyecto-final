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
from Analisis import Panaderia
from tkinter import ttk

conexion = Panaderia("panaderia.csv")


#Funciones 
def mostrar_Registro(frame_registro):##Aqui debemos poner el frame para organizar lo que va dentro 
  #formulario
  tk.Label(frame_registro, text="Nombre", bg="#B4CF66").grid(row=0, column=0, padx=10, pady=5)# etiqueta
  entry_nombre = tk.Entry(frame_registro)#cuadro de texto
  entry_nombre.grid(row=0, column=1, padx=10, pady=5)
  ## https://hektorprofe.github.io/python/interfaces-graficas-con-tkinter/widget-label-etiqueta-de-texto/

  tk.Label(frame_registro, text="Pan Frances", bg="#B4CF66").grid(row=1, column=0, padx=10, pady=5)
  entry_pan_frances = tk.Entry(frame_registro)
  entry_pan_frances.grid(row=1, column=1, padx=10, pady=5)
    
  tk.Label(frame_registro, text="Pan Queso", bg="#B4CF66").grid(row=2, column=0, padx=10, pady=5)
  entry_pan_queso = tk.Entry(frame_registro)
  entry_pan_queso.grid(row=2, column=1, padx=10, pady=5)
    
  tk.Label(frame_registro, text="Pancacho", bg="#B4CF66").grid(row=3, column=0, padx=10, pady=5)
  entry_pancacho = tk.Entry(frame_registro)
  entry_pancacho.grid(row=3, column=1, padx=10, pady=5)
  def registrar():
     nombre = entry_nombre.get().strip() # enviamos a la base de datos
     pan_frances = entry_pan_frances.get().strip()
     pan_queso = entry_pan_queso.get().strip()
     pancacho = entry_pancacho.get().strip()
     if not all([nombre, pan_frances, pan_queso, pancacho]): # verica que esten llenos
        messagebox.showwarning("Campos vacíos", "Completa todos los campos")
        return
     if pan_queso > 500:
        messagebox.showwarning("Limite", "Solo se permiten valores menores o iguales a 500 en pan queso")
        return
     if pancacho > 500:
        messagebox.showwarning("Limite", "Solo se permiten valores menores o iguales a 500 en pancacho")# mensaje de error
        return
     if pan_frances> 500:
        messagebox.showwarning("Limite", "Solo se permiten valores menores o iguales a 500 en pan frances")
        return
     if not nombre.replace(" ", "").isalpha():# verifica que sea solo letras y permite los espacios
     ##https://www.w3schools.com/python/ref_string_isalpha.asp
        messagebox.showwarning("Campos vacíos", "Digita solo letras en el nombre") 
        return
     try:
        all([int(pan_frances), int(pan_queso), int(pancacho)]) # Verifica que los panes sean numeros enteros
     except ValueError:
      messagebox.showerror("Error", "Pan frances, Pan queso  y pancacho deben ser numeros ya que corresponden a la cantidad elaborada.")
      return
     resultado = conexion.registro(nombre, pan_frances, pan_queso, pancacho)
     messagebox.showinfo("Exito", "Registro guardado")
  boton5 = tk.Button(frame_registro, text="Registrar", font=("Arial", 10), fg="white", bg="#FF5A33", width=12, command=registrar)
  boton5.grid(row=4, column=0, padx=18, pady=10)

def mostrar_reporte_general(frame_reporte):
  def reporteG():
        df = pd.read_csv("panaderia.csv")
        if df.empty:##Revisamos que no este vacio
            messagebox.showinfo("Sin datos", "Registra como minimo un usuario")
            return
        texto.delete("1.0", tk.END)##Borra el contenido de widwet
        ##https://stackoverflow.com/questions/27966626/how-to-clear-delete-the-contents-of-a-tkinter-text-widget
        texto.insert(tk.END, df[['Nombre', 'Eficiencia', 'Estado']].to_string(index=False))#muestra contenido
        conexion.grafico_torta()#muestra la torta en una subventana
        conexion.matriz()
        ##https://diveintopython.org/es/learn/functions/import-functions
  tk.Label(frame_reporte, text="Reporte General", font=("Arial", 14), bg="#F9F9F9").pack(pady=10)
  texto = tk.Text(frame_reporte, width=80, height=15)
  texto.pack()
  boton = tk.Button(frame_reporte, text="Ver Reporte", command=reporteG, bg="#44803F", fg="white")
  boton.pack(pady=10)
def mostrar_reporteT(frame_individual):
    def reporteI():
       df = pd.read_csv("panaderia.csv")
       nombre = entry_nombre.get().strip()##obtenemos nombre
       if not nombre:#si esta vacio
            messagebox.showwarning("Campo vacío", "Ingresa un nombre.")
            return
       resultado = conexion.reporte_individual(nombre)
       if resultado is None:# si no encuentra ese nombre
           messagebox.showinfo("No encontrado", "No se encontró ese nombre.")
           return
       eficiencia, estado, panes, complejidades, eficiencia_final = resultado
       texto.delete("1.0", tk.END)
       texto.insert(tk.END, f"Nombre: {nombre}\neficiencia: {eficiencia,2}\nestado: {estado}\n")# muestra en el widget
       conexion.Grafi_produccion(panes)
       conexion.Grafi_complejidad(complejidades)
       conexion.Grafi_eficiencia(eficiencia_final)
    tk.Label(frame_individual, text="Nombre del panadero", bg="#44803F").pack(pady=5)
    entry_nombre = tk.Entry(frame_individual)
    entry_nombre.pack(pady=5)

    tk.Button(frame_individual, text="Ver Reporte", command=reporteI, bg="#FFEC5C", fg="white").pack(pady=5)

    texto = tk.Text(frame_individual, width=70, height=10)
    texto.pack(pady=10)

#Ventana principal
ventana = tk.Tk()#inicio la ventana
ventana.title("Pagina de proyectos")#El titulo
ventana.geometry('800x500')#Tamaño
ventana.configure(bg='#FFEC5C')  # Cambiamos el fondo con color
## https://www.geeksforgeeks.org/how-to-change-a-tkinter-window-background-color/

# La partecita de arriba donde estan las pestañas
notebook = ttk.Notebook(ventana)
notebook.pack(expand=True, fill="both")
## https://programacionpython80889555.wordpress.com/2020/03/10/anadiendo-pestanas-a-ventana-tkinter-con-ttk-notebook/

#   creamos las pestañas
pestaña_registro = tk.Frame(notebook, bg="#D0F4DE")
pestaña_general = tk.Frame(notebook, bg="#F9F9F9")
pestaña_reporte = tk.Frame(notebook, bg="white")

# unimos las unciones a cada pestaña para que al abrirlas sea lo que nos muestre
mostrar_Registro(pestaña_registro)
mostrar_reporte_general(pestaña_general)
mostrar_reporteT(pestaña_reporte)

# Agregar las pestaña la ventana principal
notebook.add(pestaña_registro, text="Registro")
notebook.add(pestaña_general, text="Reporte General")
notebook.add(pestaña_reporte, text="Reporte por trabajador")


ventana.mainloop()
