# ===============================
# SISTEMA DE GESTIÓN DE INVENTARIOS
# Autor: Estudiante
# Descripción: Sistema simple en consola para gestionar productos
# ===============================

# ----------- Clase Producto -----------
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self._id = id_producto
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio

    # Getters
    def get_id(self):
        return self._id

    def get_nombre(self):
        return self._nombre

    def get_cantidad(self):
        return self._cantidad

    def get_precio(self):
        return self._precio

    # Setters
    def set_nombre(self, nombre):
        self._nombre = nombre

    def set_cantidad(self, cantidad):
        self._cantidad = cantidad

    def set_precio(self, precio):
        self._precio = precio

    def __str__(self):
        return f"ID: {self._id} | Nombre: {self._nombre} | Cantidad: {self._cantidad} | Precio: ${self._precio:.2f}"


# ----------- Clase Inventario -----------
class Inventario:
    def __init__(self):
        self.productos = []

    # Buscar producto por ID
    def _buscar_por_id(self, id_producto):
        for producto in self.productos:
            if producto.get_id() == id_producto:
                return producto
        return None

    # Añadir producto
    def agregar_producto(self, producto):
        if self._buscar_por_id(producto.get_id()) is not None:
            print("⚠️ Ya existe un producto con ese ID")
            return
        self.productos.append(producto)
        print("✅ Producto agregado correctamente")

    # Eliminar producto
    def eliminar_producto(self, id_producto):
        producto = self._buscar_por_id(id_producto)
        if producto:
            self.productos.remove(producto)
            print("🗑️ Producto eliminado")
        else:
            print("❌ Producto no encontrado")

    # Actualizar producto
    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        producto = self._buscar_por_id(id_producto)
        if producto:
            if cantidad is not None:
                producto.set_cantidad(cantidad)
            if precio is not None:
                producto.set_precio(precio)
            print("🔄 Producto actualizado")
        else:
            print("❌ Producto no encontrado")

    # Buscar por nombre
    def buscar_por_nombre(self, nombre):
        resultados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        if resultados:
            print("🔎 Resultados encontrados:")
            for p in resultados:
                print(p)
        else:
            print("No hay coincidencias")

    # Mostrar todos
    def mostrar_inventario(self):
        if not self.productos:
            print("Inventario vacío")
            return
        print("\n📦 LISTA DE PRODUCTOS:")
        for producto in self.productos:
            print(producto)


# ----------- Interfaz de Consola -----------

def menu():
    inventario = Inventario()

    while True:
        print("""
===== MENÚ INVENTARIO =====
1. Agregar producto
2. Eliminar producto
3. Actualizar producto
4. Buscar por nombre
5. Mostrar inventario
6. Salir
""")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            try:
                id_p = int(input("ID: "))
                nombre = input("Nombre: ")
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))
                inventario.agregar_producto(Producto(id_p, nombre, cantidad, precio))
            except ValueError:
                print("⚠️ Datos inválidos")

        elif opcion == "2":
            id_p = int(input("ID del producto a eliminar: "))
            inventario.eliminar_producto(id_p)

        elif opcion == "3":
            id_p = int(input("ID del producto: "))
            cantidad = input("Nueva cantidad (Enter para omitir): ")
            precio = input("Nuevo precio (Enter para omitir): ")

            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None

            inventario.actualizar_producto(id_p, cantidad, precio)

        elif opcion == "4":
            nombre = input("Nombre a buscar: ")
            inventario.buscar_por_nombre(nombre)

        elif opcion == "5":
            inventario.mostrar_inventario()

        elif opcion == "6":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida")


# Punto de entrada
if __name__ == "__main__":
    menu()
