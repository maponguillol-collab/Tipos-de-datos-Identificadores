class ArchivoLog:
    """
    Clase que demuestra el uso de un constructor (__init__)
    y un destructor (__del__) en Python.
    """

    def __init__(self, nombre_archivo):
        """
        Constructor:
        Se ejecuta automáticamente cuando se crea una instancia
        de la clase. Inicializa los atributos del objeto y abre
        un archivo para escritura.
        """
        self.nombre_archivo = nombre_archivo
        self.archivo = open(self.nombre_archivo, "w")
        self.archivo.write("Archivo de log iniciado.\n")
        print("Constructor (__init__) ejecutado: archivo abierto.")

    def escribir(self, mensaje):
        """
        Método para escribir mensajes en el archivo.
        """
        self.archivo.write(mensaje + "\n")

    def __del__(self):
        """
        Destructor:
        Se ejecuta automáticamente cuando el objeto es eliminado
        o cuando ya no existen referencias a él. Se utiliza para
        cerrar el archivo y liberar recursos.
        """
        if not self.archivo.closed:
            self.archivo.write("Archivo de log cerrado.\n")
            self.archivo.close()
            print("Destructor (__del__) ejecutado: archivo cerrado.")


# Programa principal
if __name__ == "__main__":
    log = ArchivoLog("registro.txt")
    log.escribir("Primer mensaje de prueba.")
    log.escribir("Segundo mensaje de prueba.")

    # Eliminamos el objeto manualmente
    del log

    print("Fin del programa.")
