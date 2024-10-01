import tkinter as tk
from tkinter import ttk, messagebox

class TaskApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Tareas")
        self.root.geometry("500x450")  # Dimensiones ajustadas para una mejor visualización

        # Campo de entrada para agregar nuevas tareas
        self.task_entry = tk.Entry(self.root, width=50)
        self.task_entry.pack(pady=15)
        self.task_entry.focus()  # Coloca el cursor en el campo de entrada

        # Botón para añadir tarea
        self.add_button = tk.Button(self.root, text="Añadir Tarea", command=self.add_task)
        self.add_button.pack(pady=5)

        # Lista para mostrar las tareas
        self.task_list = tk.Listbox(self.root, selectmode=tk.SINGLE, height=10, font=("Arial", 12))
        self.task_list.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

        # Asociar eventos a la lista de tareas
        self.task_list.bind("<Double-1>", self.mark_as_completed)
        self.task_list.bind("<Delete>", self.delete_task)  # Presionar Supr para eliminar una tarea

        # Botones adicionales para gestionar las tareas
        self.complete_button = tk.Button(self.root, text="Marcar como Completada", command=self.mark_as_completed)
        self.complete_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.delete_button = tk.Button(self.root, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.pack(side=tk.RIGHT, padx=10, pady=10)

        # Asignar eventos de teclado
        self.root.bind("<Return>", lambda event: self.add_task())  # Enter para agregar una tarea
        self.root.bind("<Escape>", lambda event: self.root.quit())  # Escape para cerrar la aplicación

    def add_task(self):
        # Añadir una nueva tarea a la lista
        task = self.task_entry.get()
        if task:
            self.task_list.insert(tk.END, task)  # Inserta la tarea al final de la lista
            self.task_entry.delete(0, tk.END)  # Borra el contenido del campo de entrada
        else:
            messagebox.showwarning("Advertencia", "Por favor, ingresa una tarea.")

    def mark_as_completed(self, event=None):
        # Marca una tarea como completada visualmente
        selected_task_index = self.task_list.curselection()
        if selected_task_index:
            current_text = self.task_list.get(selected_task_index)
            self.task_list.delete(selected_task_index)
            self.task_list.insert(selected_task_index, f"✔️ {current_text}")  # Añadir marca de completado
        else:
            messagebox.showinfo("Información", "Selecciona una tarea para marcar como completada.")

    def delete_task(self, event=None):
        # Elimina una tarea seleccionada
        selected_task_index = self.task_list.curselection()
        if selected_task_index:
            self.task_list.delete(selected_task_index)
        else:
            messagebox.showinfo("Información", "Selecciona una tarea para eliminar.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskApp(root)
    root.mainloop()

