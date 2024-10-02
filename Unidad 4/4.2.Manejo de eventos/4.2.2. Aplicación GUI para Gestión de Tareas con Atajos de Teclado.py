import tkinter as tk
from tkinter import messagebox, ttk

class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas")
        self.root.geometry("500x450")

        # Configuración de fuente y estilos
        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Arial", 12, "bold"))
        style.configure("Treeview", font=("Arial", 10))

        # Frame para la entrada y botón de añadir tarea
        add_frame = tk.Frame(root)
        add_frame.pack(pady=10)

        # Campo de entrada para añadir nueva tarea
        self.new_task_entry = tk.Entry(add_frame, width=40, font=("Arial", 12))
        self.new_task_entry.grid(row=0, column=0)

        # Botón para añadir tarea
        self.add_task_button = tk.Button(add_frame, text="Añadir Tarea", command=self.add_task)
        self.add_task_button.grid(row=0, column=1, padx=10)

        # Frame para los botones de manejo de tareas
        button_frame = tk.Frame(root)
        button_frame.pack(pady=10)

        # Botón para marcar tarea como completada
        self.mark_task_button = tk.Button(button_frame, text="Marcar como Completada", command=self.mark_task)
        self.mark_task_button.grid(row=0, column=0, padx=10)

        # Botón para desmarcar tarea completada
        self.unmark_task_button = tk.Button(button_frame, text="Desmarcar Tarea", command=self.unmark_task)
        self.unmark_task_button.grid(row=0, column=1, padx=10)

        # Botón para eliminar tarea
        self.delete_task_button = tk.Button(button_frame, text="Eliminar Tarea", command=self.delete_task)
        self.delete_task_button.grid(row=0, column=2, padx=10)

        # Lista de tareas con un componente Treeview
        self.tasks_frame = ttk.Frame(root)
        self.tasks_frame.pack(fill=tk.BOTH, expand=True)

        self.tasks_list = ttk.Treeview(self.tasks_frame, columns=("Tarea"), show="headings", height=15)
        self.tasks_list.heading("Tarea", text="Descripción")
        self.tasks_list.pack(fill=tk.BOTH, expand=True, pady=10)

        # Configurar atajos de teclado para acciones
        root.bind('<Escape>', lambda e: root.quit())  # Tecla 'Escape' para salir
        root.bind('<Return>', lambda e: self.mark_task() if self.tasks_list.selection() else self.add_task())  # 'Enter' para añadir o marcar tarea
        root.bind('c', lambda e: self.mark_task())  # Tecla 'C' para marcar como completada
        root.bind('u', lambda e: self.unmark_task())  # Tecla 'U' para desmarcar tarea
        root.bind('d', lambda e: self.delete_task())  # Tecla 'D' para eliminar
        root.bind('<Delete>', self.delete_task)  # Tecla 'Delete' para eliminar tarea

    def add_task(self, event=None):
        """Añadir una nueva tarea a la lista."""
        task = self.new_task_entry.get()
        if task:
            self.tasks_list.insert('', tk.END, values=(task,))
            self.new_task_entry.delete(0, tk.END)  # Limpiar el campo de entrada
        else:
            messagebox.showwarning("Advertencia", "La tarea no puede estar vacía.")

    def mark_task(self):
        """Marcar la tarea seleccionada como completada."""
        selected_item = self.tasks_list.selection()
        if selected_item:
            self.tasks_list.item(selected_item, tags=('completed',))
            self.tasks_list.tag_configure('completed', background='light green')  # Cambiar color a verde claro
        else:
            messagebox.showinfo("Información", "Por favor, seleccione una tarea para marcar como completada.")

    def unmark_task(self):
        """Desmarcar la tarea seleccionada."""
        selected_item = self.tasks_list.selection()
        if selected_item:
            self.tasks_list.item(selected_item, tags=('uncompleted',))
            self.tasks_list.tag_configure('uncompleted', background='white')  # Volver a color blanco
        else:
            messagebox.showinfo("Información", "Por favor, seleccione una tarea para desmarcar.")

    def delete_task(self, event=None):
        """Eliminar la tarea seleccionada."""
        selected_item = self.tasks_list.selection()
        if selected_item:
            self.tasks_list.delete(selected_item)
        else:
            messagebox.showinfo("Información", "Por favor, seleccione una tarea para eliminar.")


# Ejecutar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()
