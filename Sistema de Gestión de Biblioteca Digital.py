# Clase Libro: contiene atributos inmutables (autor y título) en una tupla, y otros atributos
class Libro:
    def __init__(self, isbn, titulo, autor, categoria):
        self.isbn = isbn
        self.informacion = (autor, titulo)  # Tupla para autor y título
        self.categoria = categoria

    def __str__(self):
        return f"ISBN: {self.isbn}, Título: {self.informacion[1]}, Autor: {self.informacion[0]}, Categoría: {self.categoria}"

# Clase Usuario: contiene la lista de libros actualmente prestados
class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []  # Lista de objetos Libro

    def __str__(self):
        return f"Usuario: {self.nombre}, ID: {self.id_usuario}"

    # Listar libros prestados
    def listar_libros_prestados(self):
        if not self.libros_prestados:
            return "No tiene libros prestados."
        return "\n".join(str(libro) for libro in self.libros_prestados)

# Clase Biblioteca: gestiona libros, usuarios y préstamos
class Biblioteca:
    def __init__(self):
        self.libros = {}  # Diccionario: ISBN -> Libro
        self.usuarios = set()  # Conjunto de IDs de usuarios
        self.usuario_objetos = {}  # ID_usuario -> Usuario objeto

    # Añadir un libro
    def agregar_libro(self, libro):
        if libro.isbn in self.libros:
            print(f"El libro con ISBN {libro.isbn} ya existe.")
        else:
            self.libros[libro.isbn] = libro
            print(f"Libro '{libro.informacion[1]}' agregado exitosamente.")

    # Quitar un libro
    def quitar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]
            print(f"Libro con ISBN {isbn} eliminado.")
        else:
            print(f"No se encontró ningún libro con ISBN {isbn}.")

    # Registrar un usuario
    def registrar_usuario(self, usuario):
        if usuario.id_usuario in self.usuarios:
            print(f"El usuario con ID {usuario.id_usuario} ya está registrado.")
        else:
            self.usuarios.add(usuario.id_usuario)
            self.usuario_objetos[usuario.id_usuario] = usuario
            print(f"Usuario '{usuario.nombre}' registrado exitosamente.")

    # Dar de baja un usuario
    def dar_baja_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            del self.usuario_objetos[id_usuario]
            self.usuarios.remove(id_usuario)
            print(f"Usuario con ID {id_usuario} dado de baja.")
        else:
            print(f"No se encontró usuario con ID {id_usuario}.")

    # Prestar libro a usuario
    def prestar_libro(self, isbn, id_usuario):
        if isbn not in self.libros:
            print(f"El libro con ISBN {isbn} no existe.")
            return
        if id_usuario not in self.usuarios:
            print(f"El usuario con ID {id_usuario} no está registrado.")
            return

        libro = self.libros[isbn]
        usuario = self.usuario_objetos[id_usuario]

        # Verificar si el libro ya está prestado
        for u in self.usuario_objetos.values():
            if libro in u.libros_prestados:
                print(f"El libro ya está prestado a otro usuario.")
                return

        usuario.libros_prestados.append(libro)
        print(f"Libro '{libro.informacion[1]}' prestado a {usuario.nombre}.")

    # Devolver libro
    def devolver_libro(self, isbn, id_usuario):
        if id_usuario not in self.usuarios:
            print(f"El usuario con ID {id_usuario} no está registrado.")
            return
        usuario = self.usuario_objetos[id_usuario]

        # Buscar el libro en los prestados del usuario
        for libro in usuario.libros_prestados:
            if libro.isbn == isbn:
                usuario.libros_prestados.remove(libro)
                print(f"Libro '{libro.informacion[1]}' devuelto por {usuario.nombre}.")
                return
        print(f"El usuario no tiene prestado ese libro.")

    # Buscar libros por título, autor o categoría
    def buscar_libros(self, criterio, valor):
        resultados = []
        for libro in self.libros.values():
            if criterio == 'titulo' and libro.informacion[1] == valor:
                resultados.append(libro)
            elif criterio == 'autor' and libro.informacion[0] == valor:
                resultados.append(libro)
            elif criterio == 'categoria' and libro.categoria == valor:
                resultados.append(libro)
        if resultados:
            return "\n".join(str(libro) for libro in resultados)
        else:
            return "No se encontraron libros con ese criterio."

    # Listar libros prestados a un usuario
    def listar_libros_usuario(self, id_usuario):
        if id_usuario not in self.usuarios:
            return "Usuario no registrado."
        usuario = self.usuario_objetos[id_usuario]
        return usuario.listar_libros_prestados()

# Ejemplo de uso:
if __name__ == "__main__":
    # Crear la biblioteca
    biblioteca = Biblioteca()

    # Crear algunos libros
    libro1 = Libro("1234567890", "Cien Años de Soledad", "Gabriel García Márquez", "Realismo mágico")
    libro2 = Libro("0987654321", "Don Quijote", "Miguel de Cervantes", "Clásico")
    libro3 = Libro("111222333", "El Alquimista", "Paulo Coelho", "Ficción")

    # Agregar libros a la biblioteca
    biblioteca.agregar_libro(libro1)
    biblioteca.agregar_libro(libro2)
    biblioteca.agregar_libro(libro3)

    # Registrar usuarios
    usuario1 = Usuario("Ana Pérez", "U001")
    usuario2 = Usuario("Luis Gómez", "U002")
    biblioteca.registrar_usuario(usuario1)
    biblioteca.registrar_usuario(usuario2)

    # Prestar libros
    biblioteca.prestar_libro("1234567890", "U001")
    biblioteca.prestar_libro("0987654321", "U002")

    # Listar libros prestados
    print("\nLibros prestados a Ana Pérez:")
    print(biblioteca.listar_libros_usuario("U001"))

    print("\nLibros prestados a Luis Gómez:")
    print(biblioteca.listar_libros_usuario("U002"))

    # Buscar libros por título
    print("\nBuscar libros por título 'El Alquimista':")
    print(biblioteca.buscar_libros("titulo", "El Alquimista"))

    # Devolver un libro
    biblioteca.devolver_libro("1234567890", "U001")
    print("\nDespués de devolver el libro:")
    print(biblioteca.listar_libros_usuario("U001"))