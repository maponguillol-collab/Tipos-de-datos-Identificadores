import os
import json

class Producto:
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"

class Inventario:
    def __init__(self, archivo_inventario="inventario.txt"):
        self.archivo_inventario = archivo_inventario
        self.inventario = {}
        self.cargar_inventario()

    def cargar_inventario(self):
        """
        Carga el inventario desde el archivo especificado.
        Si el archivo no existe, lo crea.
        """
        try:
            if os.path.exists(self.archivo_inventario):
                with open(self.archivo_inventario, 'r') as archivo:
                    datos = json.load(archivo)
                    self.inventario = {nombre: Producto(nombre, data['cantidad'], data['precio']) for nombre, data in datos.items()}
                print("Inventario cargado exitosamente desde el archivo.")
            else:
                print("Archivo de inventario no encontrado. Se creará uno nuevo.")
                self.guardar_inventario()  # Crea un archivo vacío para evitar errores futuros
        except FileNotFoundError:
            print(f"Error: El archivo {self.archivo_inventario} no fue encontrado.")
        except PermissionError:
            print(f"Error: Permiso denegado para acceder al archivo {self.archivo_inventario}.")
        except json.JSONDecodeError:
            print(f"Error: El archivo {self.archivo_inventario} está corrupto o vacío. Se iniciará un nuevo inventario.")
            self.inventario = {}
        except Exception as e:
            print(f"Error inesperado al cargar el inventario: {e}")

    def guardar_inventario(self):
        """
        Guarda el inventario actual en el archivo especificado.
        """
        try:
            datos = {nombre: {'cantidad': producto.cantidad, 'precio': producto.precio} for nombre, producto in self.inventario.items()}
            with open(self.archivo_inventario, 'w') as archivo:
                json.dump(datos, archivo, indent=4)
            print("Inventario guardado exitosamente en el archivo.")
        except PermissionError:
            print(f"Error: Permiso denegado para escribir en el archivo {self.archivo_inventario}.")
        except Exception as e:
            print(f"Error inesperado al guardar el inventario: {e}")

    def agregar_producto(self, nombre, cantidad, precio):
        """
        Agrega un nuevo producto al inventario o actualiza la cantidad si ya existe.
        """
        if nombre in self.inventario:
            print("El producto ya existe. Use actualizar_producto para modificar la cantidad o el precio.")
            return
        self.inventario[nombre] = Producto(nombre, cantidad, precio)
        self.guardar_inventario()
        print(f"Producto '{nombre}' agregado exitosamente al inventario.")

    def actualizar_producto(self, nombre, cantidad=None, precio=None):
        """
        Actualiza la cantidad y/o el precio de un producto existente en el inventario.
        """
        if nombre not in self.inventario:
            print("El producto no existe. Use agregar_producto para añadirlo al inventario.")
            return
        if cantidad is not None:
            self.inventario[nombre].cantidad = cantidad
        if precio is not None:
            self.inventario[nombre].precio = precio
        self.guardar_inventario()
        print(f"Producto '{nombre}' actualizado exitosamente.")

    def eliminar_producto(self, nombre):
        """
        Elimina un producto del inventario.
        """
        if nombre in self.inventario:
            del self.inventario[nombre]
            self.guardar_inventario()
            print(f"Producto '{nombre}' eliminado exitosamente del inventario.")
        else:
            print("El producto no existe en el inventario.")

    def listar_productos(self):
        """
        Lista todos los productos en el inventario.
        """
        if not self.inventario:
            print("El inventario está vacío.")
            return
        print("Inventario:")
        for producto in self.inventario.values():
            print(producto)

def menu():
    """
    Muestra el menú de opciones y gestiona la interacción del usuario.
    """
    inventario = Inventario()

    while True:
        print("\nOpciones:")
        print("1. Agregar producto")
        print("2. Actualizar producto")
        print("3. Eliminar producto")
        print("4. Listar productos")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            inventario.agregar_producto(nombre, cantidad, precio)
        elif opcion == '2':
            nombre = input("Nombre del producto a actualizar: ")
            cantidad = input("Nueva cantidad (dejar en blanco para no cambiar): ")
            precio = input("Nuevo precio (dejar en blanco para no cambiar): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(nombre, cantidad, precio)
        elif opcion == '3':
            nombre = input("Nombre del producto a eliminar: ")
            inventario.eliminar_producto(nombre)
        elif opcion == '4':
            inventario.listar_productos()
        elif opcion == '5':
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()