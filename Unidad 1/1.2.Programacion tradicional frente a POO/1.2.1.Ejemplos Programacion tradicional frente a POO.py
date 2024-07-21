#Programación Tradicional:

def ingresar_temperaturas():
    temperaturas = []
    dias_semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']

    for dia in dias_semana:
        temp = float(input(f"Ingresa la temperatura del {dia}: "))
        temperaturas.append(temp)

    return temperaturas


def calcular_promedio_semanal(temperaturas):
    total = 0
    for temp in temperaturas:
        total += temp

    promedio = total / len(temperaturas)
    return promedio


def main():
    print("Calculadora de promedio semanal de temperaturas")
    temperaturas = ingresar_temperaturas()
    promedio = calcular_promedio_semanal(temperaturas)
    print(f"El promedio semanal de las temperaturas es: {promedio:.2f}°C")


if __name__ == "__main__":
    main()



#Programación Orientada a Objetos (POO):
class ClimaDiario:
    def __init__(self):
        self.temperaturas = []

    def ingresar_temperaturas(self):
        dias_semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']

        for dia in dias_semana:
            temp = float(input(f"Ingresa la temperatura del {dia}: "))
            self.temperaturas.append(temp)

    def calcular_promedio_semanal(self):
        total = sum(self.temperaturas)
        promedio = total / len(self.temperaturas)
        return promedio


def main():
    print("Calculadora de promedio semanal de temperaturas")
    clima = ClimaDiario()
    clima.ingresar_temperaturas()
    promedio = clima.calcular_promedio_semanal()
    print(f"El promedio semanal de las temperaturas es: {promedio:.2f}°C")


if __name__ == "__main__":
    main()

