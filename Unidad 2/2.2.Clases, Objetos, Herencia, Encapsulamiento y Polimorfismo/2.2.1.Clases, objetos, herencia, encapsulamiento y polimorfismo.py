# Clase base
class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre  # Atributo público
        self._edad = edad  # Atributo protegido (indicado por un solo guión bajo)

    def hacer_sonido(self):
        raise NotImplementedError("Este método debe ser sobrescrito por las clases derivadas")

    def obtener_info(self):
        return f"Nombre: {self.nombre}, Edad: {self._edad}"

    # Método público para obtener la edad (encapsulación)
    def get_edad(self):
        return self._edad

    # Método público para establecer la edad (encapsulación)
    def set_edad(self, edad):
        if edad > 0:
            self._edad = edad
        else:
            print("La edad debe ser un valor positivo")


# Clase derivada
class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)
        self.raza = raza

    def hacer_sonido(self):
        return "Guau"

    def obtener_info(self):
        # Sobrescritura de método (polimorfismo)
        info_base = super().obtener_info()
        return f"{info_base}, Raza: {self.raza}"


# Clase derivada
class Gato(Animal):
    def __init__(self, nombre, edad, color):
        super().__init__(nombre, edad)
        self.color = color

    def hacer_sonido(self):
        return "Miau"

    def obtener_info(self):
        # Sobrescritura de método (polimorfismo)
        info_base = super().obtener_info()
        return f"{info_base}, Color: {self.color}"


# Función para demostrar polimorfismo
def imprimir_sonido(animal):
    print(f"{animal.nombre} dice: {animal.hacer_sonido()}")


# Crear instancias de las clases y demostrar funcionalidad
perro = Perro("Fido", 5, "Labrador")
gato = Gato("Misu", 3, "Blanco")

print(perro.obtener_info())  # Nombre: Fido, Edad: 5, Raza: Labrador
print(gato.obtener_info())   # Nombre: Misu, Edad: 3, Color: Blanco

# Demostración de encapsulación
print(perro.get_edad())  # 5
perro.set_edad(6)
print(perro.get_edad())  # 6

# Demostración de polimorfismo
imprimir_sonido(perro)  # Fido dice: Guau
imprimir_sonido(gato)   # Misu dice: Miau
