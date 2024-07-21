import os


def mostrar_codigo(ruta_script):
    # Asegúrate de que la ruta al script es absoluta
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            print(f"\n--- Código de {ruta_script} ---\n")
            print(archivo.read())
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")


def mostrar_menu():
    # Define la ruta base donde se encuentra el dashboard.py
    ruta_base = os.path.dirname(__file__)

    opciones = {
        '1': "Unidad 1/1.1.Tecnicas de programacion/1.1.1.Ejemplos de Técnicas de Programación.py",
        '2': "Unidad 1/1.2.Programacion tradicional frente a POO/1.2.1.Ejemplos Programacion tradicional frente a POO.py",
        '3': "Unidad 1/1.3.Caracteristicas de la POO/1.3.1.Ejemplos Mundo Real POO.py",
        '4': "Unidad 2/2.3. Constructores y Destructores/2.3.1.Ejemplo Constructores y Destructores.py",
    }

        #agrega aquí el resto de las rutas de los scripts#

    while True:
        print("\nMenu Principal - Dashboard")
        # Imprime las opciones del menú
        for key in opciones:
            print(f"{key} - {opciones[key]}")
        print("0 - Salir")

        eleccion = input("Elige un script para ver su código o '0' para salir: ")
        if eleccion == '0':
            break
        elif eleccion in opciones:
            # Asegura que el path sea absoluto
            ruta_script = os.path.join(ruta_base, opciones[eleccion])
            mostrar_codigo(ruta_script)
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")


# Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()