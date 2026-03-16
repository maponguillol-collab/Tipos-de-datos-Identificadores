import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class AplicacionGUI:
    def __init__(self, ventana_principal):
        """
        Inicializa la aplicación GUI.

        Args:
            ventana_principal (tk.Tk): La ventana principal de la aplicación.
        """
        self.ventana_principal = ventana_principal
        self.ventana_principal.title("Gestor de Tareas Sencillo")
        self.ventana_principal.geometry("400x350") # Tamaño inicial de la ventana

        self.datos_agregados = [] # Lista para almacenar los datos

        self.crear_widgets()

    def crear_widgets(self):
        """
        Crea y organiza todos los widgets (componentes) de la interfaz gráfica.
        """
        # --- Frame para la entrada de datos ---
        frame_entrada = tk.Frame(self.ventana_principal, padx=10, pady=10)
        frame_entrada.pack(pady=10, fill=tk.X)

        # Etiqueta para el campo de texto
        tk.Label(frame_entrada, text="Nueva Tarea:").pack(side=tk.LEFT)

        # Campo de texto para ingresar la tarea
        self.campo_texto_tarea = tk.Entry(frame_entrada, width=30)
        self.campo_texto_tarea.pack(side=tk.LEFT, padx=5)
        self.campo_texto_tarea.bind("<Return>", lambda event=None: self.agregar_tarea()) # Permite agregar con Enter

        # Botón para agregar la tarea
        self.boton_agregar = tk.Button(frame_entrada, text="Agregar", command=self.agregar_tarea)
        self.boton_agregar.pack(side=tk.LEFT)

        # --- Frame para mostrar los datos ---
        frame_datos = tk.Frame(self.ventana_principal, padx=10, pady=10)
        frame_datos.pack(pady=10, fill=tk.BOTH, expand=True)

        # Etiqueta para la lista/tabla
        tk.Label(frame_datos, text="Tareas Pendientes:").pack(anchor=tk.W)

        # Configuración del Treeview (tabla) para mostrar datos
        self.tree = ttk.Treeview(frame_datos, columns=("Tarea"), show="headings")
        self.tree.heading("Tarea", text="Tarea")
        self.tree.column("Tarea", width=350, anchor=tk.W)
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Scrollbar para el Treeview
        scrollbar = tk.Scrollbar(frame_datos, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # --- Frame para los botones de acción ---
        frame_botones_accion = tk.Frame(self.ventana_principal, padx=10, pady=10)
        frame_botones_accion.pack(pady=10)

        # Botón para limpiar la entrada de texto
        self.boton_limpiar_entrada = tk.Button(frame_botones_accion, text="Limpiar Entrada", command=self.limpiar_entrada)
        self.boton_limpiar_entrada.pack(side=tk.LEFT, padx=5)

        # Botón para limpiar todos los datos
        self.boton_limpiar_todo = tk.Button(frame_botones_accion, text="Limpiar Todo", command=self.limpiar_todo)
        self.boton_limpiar_todo.pack(side=tk.LEFT, padx=5)

    def agregar_tarea(self):
        """
        Obtiene el texto del campo de entrada, lo agrega a la lista de datos
        y lo muestra en la tabla. Limpia el campo de entrada después de agregar.
        """
        tarea = self.campo_texto_tarea.get().strip() # Obtiene el texto y elimina espacios en blanco

        if tarea: # Solo agrega si el campo no está vacío
            self.datos_agregados.append(tarea)
            self.actualizar_tabla()
            self.campo_texto_tarea.delete(0, tk.END) # Limpia el campo de texto
        else:
            messagebox.showwarning("Advertencia", "Por favor, ingrese una tarea.")

    def actualizar_tabla(self):
        """
        Limpia el contenido actual de la tabla y lo rellena con los datos
        de la lista self.datos_agregados.
        """
        # Limpiar filas existentes en el Treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Insertar nuevos datos
        for dato in self.datos_agregados:
            self.tree.insert("", tk.END, values=(dato,))

    def limpiar_entrada(self):
        """
        Limpia el contenido del campo de texto de entrada.
        """
        self.campo_texto_tarea.delete(0, tk.END)

    def limpiar_todo(self):
        """
        Limpia la lista de datos y actualiza la tabla para que quede vacía.
        """
        if not self.datos_agregados:
            messagebox.showinfo("Información", "No hay tareas para limpiar.")
            return

        respuesta = messagebox.askyesno("Confirmar Limpieza", "¿Está seguro de que desea eliminar todas las tareas?")
        if respuesta:
            self.datos_agregados = []
            self.actualizar_tabla()
            self.limpiar_entrada() # Asegurarse de que el campo de texto también esté vacío


# --- Bloque principal para ejecutar la aplicación ---
if __name__ == "__main__":
    root = tk.Tk()
    app = AplicacionGUI(root)
    root.mainloop()