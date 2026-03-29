import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas")
        self.root.geometry("400x450")

        # --- Variables ---
        self.tasks = [] # Lista para almacenar las tareas como diccionarios
        self.task_font = ("Arial", 12)
        self.completed_font = ("Arial", 12, "overstrike") # Fuente para tareas completadas

        # --- Widgets ---

        # Frame para la entrada y botón de añadir
        self.input_frame = tk.Frame(root, pady=10)
        self.input_frame.pack(fill=tk.X)

        self.task_entry = tk.Entry(self.input_frame, font=self.task_font, width=30)
        self.task_entry.pack(side=tk.LEFT, padx=10)
        self.task_entry.bind("<Return>", self.add_task_event) # Bind Enter key

        self.add_button = tk.Button(self.input_frame, text="Añadir Tarea", command=self.add_task, bg="#4CAF50", fg="white")
        self.add_button.pack(side=tk.LEFT, padx=5)

        # Frame para la lista de tareas
        self.list_frame = tk.Frame(root, pady=10)
        self.list_frame.pack(fill=tk.BOTH, expand=True)

        self.task_listbox = tk.Listbox(self.list_frame, font=self.task_font, selectmode=tk.SINGLE, height=15, border=0, highlightthickness=0, selectbackground="#a6a6a6", selectforeground="white")
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=5)
        self.task_listbox.bind("<Double-Button-1>", self.toggle_complete_event) # Double click to toggle completion

        # Scrollbar para la Listbox
        self.scrollbar = tk.Scrollbar(self.list_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y, padx=(0, 10), pady=5)
        self.task_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_listbox.yview)

        # Frame para los botones de acción
        self.button_frame = tk.Frame(root, pady=10)
        self.button_frame.pack(fill=tk.X)

        self.complete_button = tk.Button(self.button_frame, text="Marcar como Completada", command=self.toggle_complete, bg="#2196F3", fg="white")
        self.complete_button.pack(side=tk.LEFT, padx=5)

        self.delete_button = tk.Button(self.button_frame, text="Eliminar Tarea", command=self.delete_task, bg="#f44336", fg="white")
        self.delete_button.pack(side=tk.LEFT, padx=5)

        # --- Cargar tareas iniciales (si las hubiera) ---
        self.load_tasks()

    def add_task(self):
        task_text = self.task_entry.get().strip()
        if task_text:
            self.tasks.append({"text": task_text, "completed": False})
            self.update_listbox()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Entrada Vacía", "Por favor, introduce una tarea.")

    def add_task_event(self, event):
        self.add_task()

    def update_listbox(self):
        self.task_listbox.delete(0, tk.END) # Limpiar la lista actual
        for i, task in enumerate(self.tasks):
            display_text = task["text"]
            if task["completed"]:
                # Mostrar texto tachado si está completada
                self.task_listbox.insert(tk.END, display_text)
                self.task_listbox.itemconfig(i, {'fg': 'gray', 'font': self.completed_font})
            else:
                self.task_listbox.insert(tk.END, display_text)
                self.task_listbox.itemconfig(i, {'fg': 'black', 'font': self.task_font})

    def get_selected_task_index(self):
        selected_indices = self.task_listbox.curselection()
        if not selected_indices:
            messagebox.showwarning("Ninguna Tarea Seleccionada", "Por favor, selecciona una tarea.")
            return None
        return selected_indices[0]

    def toggle_complete(self):
        index = self.get_selected_task_index()
        if index is not None:
            self.tasks[index]["completed"] = not self.tasks[index]["completed"]
            self.update_listbox()

    def toggle_complete_event(self, event):
        # Obtener el índice de la tarea sobre la que se hizo doble clic
        widget = event.widget
        x = event.x
        y = event.y
        index = widget.nearest(y)
        if 0 <= index < len(self.tasks):
            self.tasks[index]["completed"] = not self.tasks[index]["completed"]
            self.update_listbox()

    def delete_task(self):
        index = self.get_selected_task_index()
        if index is not None:
            del self.tasks[index]
            self.update_listbox()

    def load_tasks(self):
        # Aquí podrías implementar la carga de tareas desde un archivo (ej. JSON, TXT)
        # Por ahora, la lista estará vacía al inicio.
        pass

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()