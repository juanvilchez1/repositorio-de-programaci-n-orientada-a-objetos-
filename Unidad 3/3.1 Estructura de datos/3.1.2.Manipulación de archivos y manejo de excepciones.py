import os

class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio:.2f}"

    def get_id_producto(self):
        return self.id_producto

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def set_precio(self, precio):
        self.precio = precio


class Inventario:
    def __init__(self, archivo="inventario.txt"):
        self.productos = []
        self.archivo = archivo
        self.cargar_inventario()

    def cargar_inventario(self):
        try:
            if os.path.exists(self.archivo):
                with open(self.archivo, 'r') as file:
                    for linea in file:
                        datos = linea.strip().split(',')
                        if len(datos) == 4:
                            id_producto, nombre, cantidad, precio = datos
                            producto = Producto(id_producto, nombre, int(cantidad), float(precio))
                            self.productos.append(producto)
                print("Inventario cargado exitosamente.")
            else:
                print(f"Archivo {self.archivo} no encontrado. Se creará un nuevo archivo.")
                self.guardar_inventario()
        except FileNotFoundError:
            print("Error: El archivo no se encontró.")
        except PermissionError:
            print("Error: No tienes permiso para leer el archivo.")
        except Exception as e:
            print(f"Error al cargar el inventario: {e}")

    def guardar_inventario(self):
        try:
            with open(self.archivo, 'w') as file:
                for producto in self.productos:
                    file.write(f"{producto.get_id_producto()},{producto.get_nombre()},{producto.get_cantidad()},{producto.get_precio():.2f}\n")
            print("Inventario guardado exitosamente.")
        except PermissionError:
            print("Error: No tienes permiso para escribir en el archivo.")
        except Exception as e:
            print(f"Error al guardar el inventario: {e}")

    def añadir_producto(self, producto):
        for p in self.productos:
            if p.get_id_producto() == producto.get_id_producto():
                print("Error: El ID del producto ya existe.")
                return
        self.productos.append(producto)
        self.guardar_inventario()
        print("Producto añadido exitosamente.")

    def eliminar_producto(self, id_producto):
        for p in self.productos:
            if p.get_id_producto() == id_producto:
                self.productos.remove(p)
                self.guardar_inventario()
                print("Producto eliminado exitosamente.")
                return
        print("Error: Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        for p in self.productos:
            if p.get_id_producto() == id_producto:
                if cantidad is not None:
                    p.set_cantidad(cantidad)
                if precio is not None:
                    p.set_precio(precio)
                self.guardar_inventario()
                print("Producto actualizado exitosamente.")
                return
        print("Error: Producto no encontrado.")

    def buscar_producto_por_nombre(self, nombre):
        resultados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        if resultados:
            print("Productos encontrados:")
            for p in resultados:
                print(p)
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_todos_los_productos(self):
        if self.productos:
            print("Inventario:")
            for p in self.productos:
                print(p)
        else:
            print("El inventario está vacío.")


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
