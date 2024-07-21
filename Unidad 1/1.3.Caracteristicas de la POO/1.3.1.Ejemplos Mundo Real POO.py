from datetime import datetime


# Clase que representa una habitación del hotel
class Habitacion:
    def __init__(self, numero, tipo):
        self.numero = numero
        self.tipo = tipo
        self.disponible = True  # Indica si la habitación está disponible

    def __str__(self):
        return f"Habitación {self.numero} ({self.tipo}) - {'Disponible' if self.disponible else 'Ocupada'}"


# Clase que representa un cliente del hotel
class Cliente:
    def __init__(self, nombre, id_cliente):
        self.nombre = nombre
        self.id_cliente = id_cliente

    def __str__(self):
        return f"Cliente: {self.nombre} (ID: {self.id_cliente})"


# Clase que representa una reserva realizada por un cliente
class Reserva:
    def __init__(self, cliente, habitacion, fecha_inicio, fecha_fin):
        self.cliente = cliente
        self.habitacion = habitacion
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin

    def __str__(self):
        return (f"Reserva: {self.cliente.nombre} ha reservado la {self.habitacion} "
                f"desde {self.fecha_inicio.strftime('%Y-%m-%d')} hasta {self.fecha_fin.strftime('%Y-%m-%d')}")


# Clase que maneja la colección de habitaciones y reservas
class Hotel:
    def __init__(self, nombre):
        self.nombre = nombre
        self.habitaciones = []  # Lista de todas las habitaciones en el hotel
        self.reservas = []  # Lista de todas las reservas realizadas

    def agregar_habitacion(self, habitacion):
        self.habitaciones.append(habitacion)
        print(f"Habitación agregada: {habitacion}")

    def realizar_reserva(self, cliente, numero_habitacion, fecha_inicio, fecha_fin):
        habitacion = next((h for h in self.habitaciones if h.numero == numero_habitacion and h.disponible), None)

        if habitacion:
            nueva_reserva = Reserva(cliente, habitacion, fecha_inicio, fecha_fin)
            self.reservas.append(nueva_reserva)
            habitacion.disponible = False
            print(f"Reserva realizada: {nueva_reserva}")
        else:
            print(f"Reserva no disponible. Habitación no encontrada o no disponible.")

    def cancelar_reserva(self, cliente, numero_habitacion):
        reserva = next((r for r in self.reservas if r.cliente == cliente and r.habitacion.numero == numero_habitacion),
                       None)

        if reserva:
            reserva.habitacion.disponible = True
            self.reservas.remove(reserva)
            print(f"Reserva cancelada: {reserva}")
        else:
            print(f"Reserva no encontrada para cancelar.")

    def mostrar_habitaciones(self):
        print("Listado de habitaciones en el hotel:")
        for habitacion in self.habitaciones:
            print(habitacion)

    def mostrar_reservas(self):
        print("Listado de reservas realizadas:")
        for reserva in self.reservas:
            print(reserva)


# Ejemplo de uso del sistema de reservas de hotel

# Crear una instancia del hotel
hotel = Hotel("Hotel Paraíso")

# Agregar habitaciones al hotel
habitacion1 = Habitacion(101, "Simple")
habitacion2 = Habitacion(102, "Doble")
habitacion3 = Habitacion(103, "Suite")
hotel.agregar_habitacion(habitacion1)
hotel.agregar_habitacion(habitacion2)
hotel.agregar_habitacion(habitacion3)

# Crear clientes
cliente1 = Cliente("Juan Pérez", 1)
cliente2 = Cliente("María López", 2)

# Realizar reservas
fecha_inicio1 = datetime(2023, 6, 20)
fecha_fin1 = datetime(2023, 6, 25)
hotel.realizar_reserva(cliente1, 101, fecha_inicio1, fecha_fin1)

fecha_inicio2 = datetime(2023, 7, 1)
fecha_fin2 = datetime(2023, 7, 10)
hotel.realizar_reserva(cliente2, 102, fecha_inicio2, fecha_fin2)

# Mostrar habitaciones y reservas
hotel.mostrar_habitaciones()
hotel.mostrar_reservas()

# Cancelar una reserva
hotel.cancelar_reserva(cliente1, 101)

# Mostrar habitaciones y reservas después de la cancelación
hotel.mostrar_habitaciones()
hotel.mostrar_reservas()

