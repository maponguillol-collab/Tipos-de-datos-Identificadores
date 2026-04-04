import tkinter as tk
from tkinter import messagebox

class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas")
        self.root.geometry("500x400")

        self.tasks = []

        # --- Widgets de la Interfaz Gráfica ---

        # Frame para entrada y botón de añadir
        self.input_frame = tk.Frame(root)
        self.input_frame.pack(pady=10)

        self.task_entry = tk.Entry(self.input_frame, width=40)
        self.task_entry.pack(side=tk.LEFT, padx=5)
        self.task_entry.bind("<Return>", self.add_task_event) # Atajo para añadir con Enter

        self.add_button = tk.Button(self.input_frame, text="Añadir Tarea", command=self.add_task)
        self.add_button.pack(side=tk.LEFT)

        # Frame para la lista de tareas
        self.list_frame = tk.Frame(root)
        self.list_frame.pack(pady=10, fill=tk.BOTH, expand=True)

        self.task_listbox = tk.Listbox(self.list_frame, width=50, height=10, selectmode=tk.SINGLE)
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.task_listbox.bind("<<ListboxSelect>>", self.on_task_select) # Para saber qué tarea está seleccionada

        # Scrollbar para la lista
        self.scrollbar = tk.Scrollbar(self.list_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.task_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_listbox.yview)

        # Frame para botones de acción
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=10)

        self.complete_button = tk.Button(self.button_frame, text="Marcar Completada", command=self.mark_complete)
        self.complete_button.pack(side=tk.LEFT, padx=5)

        self.delete_button = tk.Button(self.button_frame, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.pack(side=tk.LEFT, padx=5)

        # --- Atajos de Teclado ---
        self.root.bind("<KeyPress-c>", self.mark_complete_event) # Atajo para completar con 'C'
        self.root.bind("<KeyPress-d>", self.delete_task_event)   # Atajo para eliminar con 'D'
        self.root.bind("<Escape>", self.close_app_event)        # Atajo para cerrar con 'Escape'

        self.load_tasks() # Cargar tareas si las hubiera (en un futuro, desde archivo)

    # --- Funciones de Gestión de Tareas ---

    def add_task(self):
        task_description = self.task_entry.get().strip()
        if task_description:
            self.tasks.append({"description": task_description, "completed": False})
            self.update_task_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Entrada Vacía", "Por favor, introduce una descripción para la tarea.")

    def add_task_event(self, event):
        self.add_task()

    def mark_complete(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.tasks[selected_index]["completed"] = True
            self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Ninguna Tarea Seleccionada", "Por favor, selecciona una tarea para marcarla como completada.")

    def mark_complete_event(self, event):
        self.mark_complete()

    def delete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            del self.tasks[selected_index]
            self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Ninguna Tarea Seleccionada", "Por favor, selecciona una tarea para eliminarla.")

    def delete_task_event(self, event):
        self.delete_task()

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for i, task in enumerate(self.tasks):
            display_text = f"{i+1}. {task['description']}"
            self.task_listbox.insert(tk.END, display_text)
            if task["completed"]:
                self.task_listbox.itemconfig(tk.END, {'fg': 'gray', 'bg': '#f0f0f0'}) # Feedback visual
        self.task_listbox.selection_clear(0, tk.END) # Limpiar selección después de actualizar

    def on_task_select(self, event):
        # Podríamos usar esto para habilitar/deshabilitar botones si no hay nada seleccionado
        pass

    def close_app_event(self, event):
        self.root.destroy()

    def load_tasks(self):
        # En una aplicación real, aquí cargarías las tareas desde un archivo (JSON, DB, etc.)
        # Por ahora, la lista está vacía al inicio.
        pass

    def save_tasks(self):
        # En una aplicación real, aquí guardarías las tareas a un archivo.
        pass

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()