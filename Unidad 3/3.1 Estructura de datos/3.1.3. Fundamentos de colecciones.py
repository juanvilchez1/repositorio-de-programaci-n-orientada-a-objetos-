import json
import os

# Clase Producto
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def get_id_producto(self):
        return self.id_producto

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def get_precio(self):
        return self.precio

    def set_precio(self, precio):
        self.precio = precio

    def to_dict(self):
        return {
            "id_producto": self.id_producto,
            "nombre": self.nombre,
            "cantidad": self.cantidad,
            "precio": self.precio
        }

    @staticmethod
    def from_dict(data):
        return Producto(data["id_producto"], data["nombre"], data["cantidad"], data["precio"])

    def __str__(self):
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio:.2f}"


# Clase Inventario
class Inventario:
    def __init__(self, archivo="inventario.json"):
        self.productos = {}  # Usamos un diccionario para una búsqueda rápida por ID
        self.archivo = archivo
        self.cargar_inventario()

    def cargar_inventario(self):
        if os.path.exists(self.archivo):
            try:
                with open(self.archivo, 'r') as file:
                    data = json.load(file)
                    for id_producto, prod_data in data.items():
                        producto = Producto.from_dict(prod_data)
                        self.productos[id_producto] = producto
                print("Inventario cargado exitosamente.")
            except FileNotFoundError:
                print(f"Error: El archivo {self.archivo} no se encontró.")
            except json.JSONDecodeError:
                print("Error: No se pudo leer el archivo de inventario. Verifica su formato.")
            except Exception as e:
                print(f"Error al cargar el inventario: {e}")
        else:
            print(f"Archivo {self.archivo} no encontrado. Se creará un nuevo archivo.")
            self.guardar_inventario()

    def guardar_inventario(self):
        try:
            with open(self.archivo, 'w') as file:
                data = {id_producto: prod.to_dict() for id_producto, prod in self.productos.items()}
                json.dump(data, file, indent=4)
            print("Inventario guardado exitosamente.")
        except PermissionError:
            print("Error: No tienes permiso para escribir en el archivo.")
        except Exception as e:
            print(f"Error al guardar el inventario: {e}")

    def añadir_producto(self, producto):
        if producto.get_id_producto() in self.productos:
            print("Error: El ID del producto ya existe.")
        else:
            self.productos[producto.get_id_producto()] = producto
            self.guardar_inventario()
            print("Producto añadido exitosamente.")

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            self.guardar_inventario()
            print("Producto eliminado exitosamente.")
        else:
            print("Error: Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            producto = self.productos[id_producto]
            if cantidad is not None:
                producto.set_cantidad(cantidad)
            if precio is not None:
                producto.set_precio(precio)
            self.guardar_inventario()
            print("Producto actualizado exitosamente.")
        else:
            print("Error: Producto no encontrado.")

    def buscar_producto_por_nombre(self, nombre):
        resultados = [p for p in self.productos.values() if nombre.lower() in p.get_nombre().lower()]
        if resultados:
            print("Productos encontrados:")
            for p in resultados:
                print(p)
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_todos_los_productos(self):
        if self.productos:
            print("Inventario:")
            for p in self.productos.values():
                print(p)
        else:
            print("El inventario está vacío.")


# Interfaz de Usuario
def mostrar_menu():
    print("\n--- Menú de Gestión de Inventario ---")
    print("1. Añadir nuevo producto")
    print("2. Eliminar producto por ID")
    print("3. Actualizar cantidad o precio de un producto por ID")
    print("4. Buscar producto(s) por nombre")
    print("5. Mostrar todos los productos")
    print("6. Salir")


def obtener_entero(mensaje):
    while True:
        valor = input(mensaje)
        try:
            return int(valor)
        except ValueError:
            print("Por favor, ingresa un número entero válido.")


def obtener_flotante(mensaje):
    while True:
        valor = input(mensaje)
        try:
            return float(valor)
        except ValueError:
            print("Por favor, ingresa un número decimal válido.")


def main():
    inventario = Inventario()

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            id_producto = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            cantidad = obtener_entero("Cantidad del producto: ")
            precio = obtener_flotante("Precio del producto: ")
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.añadir_producto(producto)

        elif opcion == "2":
            id_producto = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            id_producto = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (dejar en blanco si no se desea cambiar): ")
            precio = input("Nuevo precio (dejar en blanco si no se desea cambiar): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id_producto, cantidad, precio)

        elif opcion == "4":
            nombre = input("Nombre del producto a buscar: ")
            inventario.buscar_producto_por_nombre(nombre)

        elif opcion == "5":
            inventario.mostrar_todos_los_productos()

        elif opcion == "6":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Inténtalo de nuevo.")


if __name__ == "__main__":
    main()

