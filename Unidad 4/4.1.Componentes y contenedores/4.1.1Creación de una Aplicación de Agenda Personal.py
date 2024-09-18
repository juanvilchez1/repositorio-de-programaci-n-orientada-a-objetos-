import tkinter as tk
from tkinter import ttk, messagebox, Menu, scrolledtext

# Funciones para eventos
def accion_boton():
    messagebox.showinfo("Acción", "¡Has presionado el botón!")

def seleccion_radio():
    messagebox.showinfo("Selección", f"Has seleccionado: {opcion_seleccionada.get()}")

def seleccion_combobox(event):
    seleccion = lista_desplegable.get()
    messagebox.showinfo("Combobox", f"Seleccionaste: {seleccion}")

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Ejemplo Simplificado GUI")
ventana.geometry("600x400")

# Panel de Entrada
panel_entrada = tk.LabelFrame(ventana, text="Panel de Entrada", padx=10, pady=10)
panel_entrada.pack(padx=10, pady=10, fill=tk.X)

# Etiqueta y Campo de texto
etiqueta = tk.Label(panel_entrada, text="Ingresa algo aquí:")
etiqueta.pack(anchor='w')
campo_texto = tk.Entry(panel_entrada)
campo_texto.pack(fill=tk.X, padx=5, pady=5)

# Lista desplegable (Combobox)
opciones = ["Primera", "Segunda", "Tercera"]
lista_desplegable = ttk.Combobox(panel_entrada, values=opciones)
lista_desplegable.current(0)
lista_desplegable.bind("<<ComboboxSelected>>", seleccion_combobox)
lista_desplegable.pack(fill=tk.X, padx=5, pady=5)

# Panel de Botones
panel_botones = tk.LabelFrame(ventana, text="Botones", padx=10, pady=10)
panel_botones.pack(padx=10, pady=10, fill=tk.X)

# Botón
boton = tk.Button(panel_botones, text="Haz clic aquí", command=accion_boton)
boton.pack(padx=5, pady=5)

# Botones de opción (RadioButtons)
opcion_seleccionada = tk.StringVar()
opcion_seleccionada.set("Primera")  # Opción predeterminada
radio1 = tk.Radiobutton(panel_botones, text="Primera", variable=opcion_seleccionada, value="Primera", command=seleccion_radio)
radio2 = tk.Radiobutton(panel_botones, text="Segunda", variable=opcion_seleccionada, value="Segunda", command=seleccion_radio)
radio3 = tk.Radiobutton(panel_botones, text="Tercera", variable=opcion_seleccionada, value="Tercera", command=seleccion_radio)
radio1.pack(side=tk.LEFT, padx=5)
radio2.pack(side=tk.LEFT, padx=5)
radio3.pack(side=tk.LEFT, padx=5)

# Área de texto con scroll
area_texto = scrolledtext.ScrolledText(ventana, wrap=tk.WORD, width=40, height=10)
area_texto.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Menú
barra_menu = Menu(ventana)
menu_archivo = Menu(barra_menu, tearoff=0)
menu_archivo.add_command(label="Opción 1", command=accion_boton)
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command=ventana.quit)
barra_menu.add_cascade(label="Archivo", menu=menu_archivo)
ventana.config(menu=barra_menu)

ventana.mainloop()


