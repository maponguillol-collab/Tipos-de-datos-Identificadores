import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import datetime

class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")
        self.root.geometry("800x500") # Tamaño inicial de la ventana

        # Lista para almacenar los eventos
        self.eventos = []

        # --- Estructura de la interfaz con Frames ---
        # Frame principal para la vista de eventos
        self.frame_vista = ttk.Frame(root, padding="10")
        self.frame_vista.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Frame para la entrada de datos
        self.frame_entrada = ttk.LabelFrame(root, text="Agregar Nuevo Evento", padding="10")
        self.frame_entrada.grid(row=0, column=1, sticky=(tk.W, tk.E, tk.N, tk.S), padx=10)

        # Frame para los botones de acción
        self.frame_acciones = ttk.Frame(root, padding="10")
        self.frame_acciones.grid(row=1, column=1, sticky=(tk.W, tk.E, tk.N, tk.S), padx=10)

        # Configurar el grid para que se expanda
        self.root.columnconfigure(0, weight=3)
        self.root.columnconfigure(1, weight=1)
        self.root.rowconfigure(0, weight=1)

        # --- Componentes de la Vista de Eventos ---
        self.label_vista = ttk.Label(self.frame_vista, text="Eventos Programados:")
        self.label_vista.grid(row=0, column=0, sticky=tk.W, pady=5)

        self.tree = ttk.Treeview(self.frame_vista, columns=("Fecha", "Hora", "Descripción"), show="headings")
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")

        # Configurar el ancho de las columnas
        self.tree.column("Fecha", width=100, anchor=tk.CENTER)
        self.tree.column("Hora", width=80, anchor=tk.CENTER)
        self.tree.column("Descripción", width=250)

        self.tree.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Scrollbar para el Treeview
        self.scrollbar = ttk.Scrollbar(self.frame_vista, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=self.scrollbar.set)
        self.scrollbar.grid(row=1, column=1, sticky=(tk.N, tk.S))

        self.frame_vista.columnconfigure(0, weight=1)
        self.frame_vista.rowconfigure(1, weight=1)

        # --- Componentes de Entrada de Datos ---
        # Fecha
        self.label_fecha = ttk.Label(self.frame_entrada, text="Fecha (YYYY-MM-DD):")
        self.label_fecha.grid(row=0, column=0, sticky=tk.W, pady=5)
        self.entry_fecha = ttk.Entry(self.frame_entrada, width=20)
        self.entry_fecha.grid(row=0, column=1, sticky=(tk.W, tk.E))

        # Hora
        self.label_hora = ttk.Label(self.frame_entrada, text="Hora (HH:MM):")
        self.label_hora.grid(row=1, column=0, sticky=tk.W, pady=5)
        self.entry_hora = ttk.Entry(self.frame_entrada, width=20)
        self.entry_hora.grid(row=1, column=1, sticky=(tk.W, tk.E))

        # Descripción
        self.label_descripcion = ttk.Label(self.frame_entrada, text="Descripción:")
        self.label_descripcion.grid(row=2, column=0, sticky=tk.W, pady=5)
        self.entry_descripcion = ttk.Entry(self.frame_entrada, width=40)
        self.entry_descripcion.grid(row=2, column=1, sticky=(tk.W, tk.E), columnspan=2)

        self.frame_entrada.columnconfigure(1, weight=1)

        # --- Componentes de Acciones ---
        self.btn_agregar = ttk.Button(self.frame_acciones, text="Agregar Evento", command=self.agregar_evento)
        self.btn_agregar.grid(row=0, column=0, pady=5, padx=5, sticky=(tk.W, tk.E))

        self.btn_eliminar = ttk.Button(self.frame_acciones, text="Eliminar Seleccionado", command=self.eliminar_evento)
        self.btn_eliminar.grid(row=1, column=0, pady=5, padx=5, sticky=(tk.W, tk.E))

        self.btn_salir = ttk.Button(self.frame_acciones, text="Salir", command=self.salir_app)
        self.btn_salir.grid(row=2, column=0, pady=5, padx=5, sticky=(tk.W, tk.E))

        # Cargar eventos iniciales si los hubiera (opcional)
        self.cargar_eventos()

    def agregar_evento(self):
        fecha_str = self.entry_fecha.get()
        hora_str = self.entry_hora.get()
        descripcion = self.entry_descripcion.get()

        # --- Validación de datos ---
        if not fecha_str or not hora_str or not descripcion:
            messagebox.showwarning("Advertencia", "Por favor, complete todos los campos.")
            return

        try:
            # Validar formato de fecha
            fecha_obj = datetime.datetime.strptime(fecha_str, "%Y-%m-%d").date()
        except ValueError:
            messagebox.showerror("Error de Formato", "El formato de fecha debe ser YYYY-MM-DD.")
            return

        try:
            # Validar formato de hora
            hora_obj = datetime.datetime.strptime(hora_str, "%H:%M").time()
        except ValueError:
            messagebox.showerror("Error de Formato", "El formato de hora debe ser HH:MM.")
            return

        # Crear el evento como un diccionario
        nuevo_evento = {
            "fecha": fecha_obj,
            "hora": hora_obj,
            "descripcion": descripcion
        }
        self.eventos.append(nuevo_evento)
        self.actualizar_vista_eventos()

        # Limpiar los campos de entrada
        self.entry_fecha.delete(0, tk.END)
        self.entry_hora.delete(0, tk.END)
        self.entry_descripcion.delete(0, tk.END)

        messagebox.showinfo("Éxito", "Evento agregado correctamente.")

    def actualizar_vista_eventos(self):
        # Limpiar la vista actual
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Ordenar eventos por fecha y hora
        self.eventos.sort(key=lambda x: (x["fecha"], x["hora"]))

        # Insertar eventos en el Treeview
        for i, evento in enumerate(self.eventos):
            fecha_formateada = evento["fecha"].strftime("%Y-%m-%d")
            hora_formateada = evento["hora"].strftime("%H:%M")
            self.tree.insert("", tk.END, values=(fecha_formateada, hora_formateada, evento["descripcion"]), iid=i)

    def eliminar_evento(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Advertencia", "Por favor, seleccione un evento para eliminar.")
            return

        # Obtener el índice del evento seleccionado
        item_iid = selected_item[0]
        indice_a_eliminar = int(item_iid)

        # Opcional: Preguntar confirmación
        if messagebox.askyesno("Confirmar Eliminación", "¿Está seguro de que desea eliminar este evento?"):
            if 0 <= indice_a_eliminar < len(self.eventos):
                del self.eventos[indice_a_eliminar]
                self.actualizar_vista_eventos()
                messagebox.showinfo("Éxito", "Evento eliminado correctamente.")
            else:
                messagebox.showerror("Error", "No se pudo encontrar el evento para eliminar.")

    def cargar_eventos(self):
        # Aquí podrías cargar eventos desde un archivo (ej. CSV, JSON) si tuvieras persistencia
        # Por ahora, solo aseguramos que la vista esté vacía al inicio
        self.actualizar_vista_eventos()

    def salir_app(self):
        if messagebox.askokcancel("Salir", "¿Desea salir de la aplicación?"):
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()