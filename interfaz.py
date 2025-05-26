import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

#Funciones 
def mostrar_Registro(frame_registro):
  #formulario
  tk.Label(frame_registro, text="Nombre", bg="#B4CF66").grid(row=0, column=0, padx=10, pady=5)# etiqueta
  entry_nombre = tk.Entry(frame_registro)#cuadro de texto
  entry_nombre.grid(row=0, column=1, padx=10, pady=5)

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
     if not nombre.replace(" ", "").isalpha():# verifica que sea solo letras y permite los espacios
     ##
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

def funcion_reporte_general(padre):
    pass
def funcion_reporte_individual(padre):
    pass

#Ventana principal
ventana = tk.Tk()#inicio la ventana
ventana.title("Pagina de proyectos")#El titulo
ventana.geometry('800x500')#Tamaño
ventana.configure(bg='#FFEC5C')  # Cambiamos el fondo con color

# Crear el contenedor de pestañas
notebook = ttk.Notebook(ventana)
notebook.pack(expand=True, fill="both")

# Crear las pestañas
pestana_registro = tk.Frame(notebook, bg="#D0F4DE")
pestana_general = tk.Frame(notebook, bg="#F9F9F9")
pestana_individual = tk.Frame(notebook, bg="#FFCAD4")

# Agregar funciones a cada pestaña
mostrar_Registro(pestana_registro)
funcion_reporte_general(pestana_general)
funcion_reporte_individual(pestana_individual)

# Añadir las pestañas al notebook
notebook.add(pestana_registro, text="Registro")
notebook.add(pestana_general, text="Reporte General")
notebook.add(pestana_individual, text="Reporte Individual")

ventana.mainloop()
