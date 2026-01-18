"""
Programa: Gestión de Vehículos
Autor: [HYUNDAI]
Fecha: [18-1-2026]

Este programa demuestra el uso de:
- Clases y objetos
- Herencia
- Encapsulación
- Polimorfismo
"""

# ------------------------------
# Clase base
# ------------------------------
class Vehiculo:
    def __init__(self, marca, modelo):
        # Atributos encapsulados (privados)
        self.__marca = marca
        self.__modelo = modelo

    # Métodos getter (encapsulación)
    def get_marca(self):
        return self.__marca

    def get_modelo(self):
        return self.__modelo

    # Método que será sobrescrito (polimorfismo)
    def mostrar_info(self):
        return f"Vehículo marca {self.__marca}, modelo {self.__modelo}"


# ------------------------------
# Clase derivada (herencia)
# ------------------------------
class Auto(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        # Llamada al constructor de la clase base
        super().__init__(marca, modelo)
        self.puertas = puertas

    # Polimorfismo: sobrescritura del método
    def mostrar_info(self):
        return (f"Auto marca {self.get_marca()}, "
                f"modelo {self.get_modelo()}, "
                f"{self.puertas} puertas")


# ------------------------------
# Programa principal
# ------------------------------
if __name__ == "__main__":
    # Creación de objetos
    vehiculo1 = Vehiculo("Toyota", "Hilux")
    auto1 = Auto("Chevrolet", "Sail", 4)

    # Uso de métodos
    print(vehiculo1.mostrar_info())
    print(auto1.mostrar_info())
