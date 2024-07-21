# Este programa calcula el área de diferentes figuras geométricas: círculo, rectángulo y triángulo.
# El usuario puede elegir la figura y proporcionar las dimensiones necesarias.

import math


def calcular_area_circulo(radio):
    """
    Calcula el área de un círculo dado su radio.

    Parámetros:
    radio (float): El radio del círculo.

    Retorna:
    float: El área del círculo.
    """
    return math.pi * radio ** 2


def calcular_area_rectangulo(base, altura):
    """
    Calcula el área de un rectángulo dada su base y altura.

    Parámetros:
    base (float): La base del rectángulo.
    altura (float): La altura del rectángulo.

    Retorna:
    float: El área del rectángulo.
    """
    return base * altura


def calcular_area_triangulo(base, altura):
    """
    Calcula el área de un triángulo dada su base y altura.

    Parámetros:
    base (float): La base del triángulo.
    altura (float): La altura del triángulo.

    Retorna:
    float: El área del triángulo.
    """
    return (base * altura) / 2


def main():
    """
    Función principal que solicita al usuario elegir una figura y proporcionar las dimensiones necesarias
    para calcular y mostrar el área de la figura seleccionada.
    """
    print("Bienvenido al programa de cálculo de áreas")
    print("Por favor, elija una figura:")
    print("1. Círculo")
    print("2. Rectángulo")
    print("3. Triángulo")

    figura_elegida = input("Ingrese el número de la figura elegida: ")

    if figura_elegida == '1':
        radio = float(input("Ingrese el radio del círculo: "))
        area = calcular_area_circulo(radio)
        figura = "círculo"
    elif figura_elegida == '2':
        base = float(input("Ingrese la base del rectángulo: "))
        altura = float(input("Ingrese la altura del rectángulo: "))
        area = calcular_area_rectangulo(base, altura)
        figura = "rectángulo"
    elif figura_elegida == '3':
        base = float(input("Ingrese la base del triángulo: "))
        altura = float(input("Ingrese la altura del triángulo: "))
        area = calcular_area_triangulo(base, altura)
        figura = "triángulo"
    else:
        print("Opción no válida")
        return

    print(f"El área del {figura} es: {area:.2f}")


if __name__ == "__main__":
    main()
