import json

class Producto:
    """
    Clase que representa un producto en el inventario.
    Atributos:
        id (int): Identificador único del producto.
        nombre (str): Nombre del producto.
        cantidad (int): Cantidad disponible del producto.
        precio (float): Precio del producto.
    """
    def __init__(self, id, nombre, cantidad, precio):
        """
        Inicializa una nueva instancia de la clase Producto.
        """
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Métodos getter
    def getId(self):
        return self.id

    def getNombre(self):
        return self.nombre

    def getCantidad(self):
        return self.cantidad

    def getPrecio(self):
        return self.precio

    # Métodos setter
    def setNombre(self, nombre):
        self.nombre = nombre

    def setCantidad(self, cantidad):
        self.cantidad = cantidad

    def setPrecio(self, precio):
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"

class Inventario:
    """
    Clase que gestiona el inventario de productos.
    Utiliza un diccionario para almacenar los productos, donde el ID del producto es la clave.
    """
    def __init__(self, archivo_inventario="inventario.json"):
        """
        Inicializa una nueva instancia de la clase Inventario.
        Carga el inventario desde un archivo si existe.
        """
        self.inventario = {}
        self.archivo_inventario = archivo_inventario
        self.cargar_inventario()

    def agregar_producto(self, producto):
        """
        Añade un nuevo producto al inventario.
        Args:
            producto (Producto): Objeto de la clase Producto a añadir.
        """
        if producto.getId() in self.inventario:
            print("Error: Ya existe un producto con este ID.")
            return
        self.inventario[producto.getId()] = producto
        self.guardar_inventario()
        print(f"Producto '{producto.getNombre()}' añadido al inventario.")

    def eliminar_producto(self, id):
        """
        Elimina un producto del inventario por su ID.
        Args:
            id (int): ID del producto a eliminar.
        """
        if id in self.inventario:
            del self.inventario[id]
            self.guardar_inventario()
            print(f"Producto con ID {id} eliminado del inventario.")
        else:
            print(f"No se encontró ningún producto con ID {id}.")

    def actualizar_producto(self, id, cantidad=None, precio=None):
        """
        Actualiza la cantidad y/o el precio de un producto en el inventario.
        Args:
            id (int): ID del producto a actualizar.
            cantidad (int, opcional): Nueva cantidad del producto.
            precio (float, opcional): Nuevo precio del producto.
        """
        if id in self.inventario:
            producto = self.inventario[id]
            if cantidad is not None:
                producto.setCantidad(cantidad)
            if precio is not None:
                producto.setPrecio(precio)
            self.guardar_inventario()
            print(f"Producto con ID {id} actualizado.")
        else:
            print(f"No se encontró ningún producto con ID {id}.")

    def buscar_producto(self, nombre):
        """
        Busca productos por nombre en el inventario.
        Args:
            nombre (str): Nombre del producto a buscar.
        Returns:
            list: Lista de productos que coinciden con el nombre buscado.
        """
        resultados = [producto for producto in self.inventario.values() if nombre.lower() in producto.getNombre().lower()]
        if resultados:
            print(f"Productos encontrados con el nombre '{nombre}':")
            for producto in resultados:
                print(producto)
        else:
            print(f"No se encontraron productos con el nombre '{nombre}'.")

    def mostrar_inventario(self):
        """
        Muestra todos los productos en el inventario.
        """
        if self.inventario:
            print("Inventario:")
            for producto in self.inventario.values():
                print(producto)
        else:
            print("El inventario está vacío.")

    def guardar_inventario(self):
        """
        Guarda el inventario en un archivo JSON.
        """
        inventario_serializable = {id: producto.__dict__ for id, producto in self.inventario.items()}
        try:
            with open(self.archivo_inventario, 'w') as archivo:
                json.dump(inventario_serializable, archivo, indent=4)
            print("Inventario guardado en archivo.")
        except Exception as e:
            print(f"Error al guardar el inventario: {e}")

    def cargar_inventario(self):
        """
        Carga el inventario desde un archivo JSON.
        """
        try:
            with open(self.archivo_inventario, 'r') as archivo:
                inventario_serializado = json.load(archivo)
                for id, producto_data in inventario_serializado.items():
                    # Convertir las claves de cadena a enteros si es necesario
                    id = int(id)
                    producto = Producto(id, producto_data['nombre'], producto_data['cantidad'], producto_data['precio'])
                    self.inventario[id] = producto
            print("Inventario cargado desde archivo.")
        except FileNotFoundError:
            print("Archivo de inventario no encontrado. Se creará uno nuevo.")
        except Exception as e:
            print(f"Error al cargar el inventario: {e}")

# Interfaz de usuario
def menu(inventario):
    """
    Muestra el menú de opciones al usuario y gestiona la interacción.
    Args:
        inventario (Inventario): Objeto de la clase Inventario a gestionar.
    """
    while True:
        print("\n--- Menú ---")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Mostrar inventario")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            id = int(input("ID del producto: "))
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad del producto: "))
            precio = float(input("Precio del producto: "))
            producto = Producto(id, nombre, cantidad, precio)
            inventario.agregar_producto(producto)

        elif opcion == '2':
            id = int(input("ID del producto a eliminar: "))
            inventario.eliminar_producto(id)

        elif opcion == '3':
            id = int(input("ID del producto a actualizar: "))
            cantidad = input("Nueva cantidad (dejar en blanco para no cambiar): ")
            precio = input("Nuevo precio (dejar en blanco para no cambiar): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id, cantidad, precio)

        elif opcion == '4':
            nombre = input("Nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)

        elif opcion == '5':
            inventario.mostrar_inventario()

        elif opcion == '6':
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

# Ejemplo de uso
if __name__ == "__main__":
    inventario = Inventario()
    menu(inventario)