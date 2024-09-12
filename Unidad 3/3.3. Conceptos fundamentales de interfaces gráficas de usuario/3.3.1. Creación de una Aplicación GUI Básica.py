
import tkinter as tk
from tkinter import messagebox

# Función para agregar elementos a la lista
def agregar_dato():
    dato = entry.get()
    if dato:
        lista.insert(tk.END, dato)  # Agrega el dato al final de la lista
        entry.delete(0, tk.END)  # Limpia el campo de texto
    else:
        messagebox.showwarning("Advertencia", "El campo de texto está vacío")

# Función para limpiar la lista
def limpiar_lista():
    lista.delete(0, tk.END)  # Borra todos los elementos de la lista

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Aplicación GUI Básica")

# Etiqueta
label = tk.Label(ventana, text="Ingrese un dato:")
label.pack(pady=10)

# Campo de texto
entry = tk.Entry(ventana, width=40)
entry.pack(pady=5)

# Botón "Agregar"
boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_dato)
boton_agregar.pack(pady=5)

# Lista para mostrar los datos agregados
lista = tk.Listbox(ventana, width=50, height=10)
lista.pack(pady=10)

# Botón "Limpiar"
boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_lista)
boton_limpiar.pack(pady=5)

# Ejecutar el bucle principal de la ventana
ventana.mainloop()
