def calcular_area_rectangulo(base, altura):
    return base * altura

def imprimir_area_cuadrado(lado):
    area = calcular_area_rectangulo(lado)
    print("El área del cuadrado es:", area)

def main():
    base = 5
    altura = 10
    area_rectangulo = calcular_area_rectangulo(base, altura)  # Falta una coma
    print("El área del rectángulo es:", area_rectangulo)

    lado = "4"  # Debería ser un entero, no una cadena
    imprimir_area_cuadrado(lado)


main()
