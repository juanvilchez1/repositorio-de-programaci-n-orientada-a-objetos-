class Personaje:
    # Constructor de la clase Personaje, inicializa los atributos del personaje
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = max(vida, 0)  # Asegura que la vida no sea negativa

    # Método para mostrar los atributos del personaje
    def atributos(self):
        print(self.nombre, ":", sep="")
        print("·Fuerza:", self.fuerza)
        print("·Inteligencia:", self.inteligencia)
        print("·Defensa:", self.defensa)
        print("·Vida:", self.vida)

    # Método para aumentar los atributos del personaje
    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza += fuerza
        self.inteligencia += inteligencia
        self.defensa += defensa

    # Método para verificar si el personaje está vivo
    def esta_vivo(self):
        return self.vida > 0

    # Método para hacer que el personaje muera
    def morir(self):
        self.vida = 0
        print(self.nombre, "ha muerto")

    # Método para calcular el daño hecho a un enemigo
    def dano(self, enemigo):
        return self.fuerza - enemigo.defensa

    # Método para atacar a un enemigo
    def atacar(self, enemigo):
        dano = self.dano(enemigo)
        enemigo.vida -= dano
        print(self.nombre, "ha realizado", dano, "puntos de daño a", enemigo.nombre)
        if enemigo.esta_vivo():
            print("Vida de", enemigo.nombre, "es", enemigo.vida)
        else:
            enemigo.morir()


# Clase Asesino que hereda de Personaje

class Asesino(Personaje):

    # Constructor de la clase Asesino, inicializa los atributos específicos del asesino
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, velocidad):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.velocidad = velocidad

    # Método para cambiar el ítem del asesino, modificando su velocidad
    def cambiar_item(self):
        opcion = int(input("Elige un item: (1) botas de pegaso, velocidad 2. (2) sandalias de hermes, velocidad 5: "))
        if opcion == 1:
            self.velocidad = 2
        elif opcion == 2:
            self.velocidad = 5
        else:
            print("Número de item incorrecto")

    # Método para mostrar los atributos del asesino, incluyendo la velocidad
    def atributos(self):
        super().atributos()
        print("·Velocidad:", self.velocidad)

    # Método para calcular el daño hecho a un enemigo, considerando la velocidad del asesino
    def dano(self, enemigo):
        return self.fuerza * self.velocidad - enemigo.defensa


# Clase Hechicero que hereda de Personaje
class Hechicero(Personaje):

    # Constructor de la clase Hechicero, inicializa los atributos específicos del hechicero
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, baculo):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.baculo = baculo

    # Método para mostrar los atributos del hechicero, incluyendo el báculo
    def atributos(self):
        super().atributos()
        print("·Báculo:", self.baculo)

    # Método para calcular el daño hecho a un enemigo, considerando la inteligencia del hechicero y el báculo
    def dano(self, enemigo):
        return self.inteligencia * self.baculo - enemigo.defensa


# Función para manejar el combate entre dos personajes
def combate(jugador_1, jugador_2):
    turno = 0
    while jugador_1.esta_vivo() and jugador_2.esta_vivo():
        print("\nTurno", turno)
        print(">>> Acción de ", jugador_1.nombre, ":", sep="")
        jugador_1.atacar(jugador_2)
        if not jugador_2.esta_vivo():
            break
        print(">>> Acción de ", jugador_2.nombre, ":", sep="")
        jugador_2.atacar(jugador_1)
        turno += 1

    if jugador_1.esta_vivo():
        print("\nHa ganado", jugador_1.nombre)
    elif jugador_2.esta_vivo():
        print("\nHa ganado", jugador_2.nombre)
    else:
        print("\nEmpate")


# Creación de instancias de los personajes Asesino y Hechicero
personaje_1 = Asesino("Batuzai", 20, 10, 4, 100, 5)
personaje_2 = Hechicero("Merlin", 5, 15, 4, 100, 4)

# Mostrar los atributos de los personajes
personaje_1.atributos()
personaje_2.atributos()

# Realizar el combate entre los personajes
combate(personaje_1, personaje_2)
