class Person:
    def __init__(self, name, age):
        """Constructor para la clase Person.
        Inicializa los atributos 'name' y 'age'."""
        self.name = name
        self.age = age
        print(f"Persona creada: {self.name}, {self.age} años.")

    def __del__(self):
        """Destructor para la clase Person.
        Imprime un mensaje indicando que la persona está siendo eliminada."""
        print(f"Persona eliminada: {self.name}, {self.age} años.")

# Demostración de uso
person = Person("Alice", 30)
del person  # Aquí se llama al destructor y se limpia el objeto


class Car:
    def __init__(self, make, model, year):
        """Constructor para la clase Car.
        Inicializa los atributos 'make', 'model' y 'year'."""
        self.make = make
        self.model = model
        self.year = year
        print(f"Coche creado: {self.year} {self.make} {self.model}.")

    def __del__(self):
        """Destructor para la clase Car.
        Imprime un mensaje indicando que el coche está siendo eliminado."""
        print(f"Coche eliminado: {self.year} {self.make} {self.model}.")

# Demostración de uso
car = Car("Toyota", "Corolla", 2020)
del car  # Aquí se llama al destructor y se limpia el objeto
