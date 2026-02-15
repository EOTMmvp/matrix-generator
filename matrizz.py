def crear_matriz(filas, columnas):
    matriz = []

    for i in range(filas):
        fila = []
        for j in range(columnas):
            while True:
                try:
                    valor = int(input(f"Elemento [{i}][{j}]: "))
                    fila.append(valor)
                    break
                except ValueError:
                    print("Error: Ingresa un número válido.")
        matriz.append(fila)

    return matriz


def mostrar_matriz(matriz):
    print("\nMatriz creada:")
    for fila in matriz:
        print(" | ".join(map(str, fila)))


def main():
    print("=== CREADOR DE MATRICES ===\n")

    try:
        filas = int(input("¿Cuántas filas quieres?: "))
        columnas = int(input("¿Cuántas columnas quieres?: "))

        matriz = crear_matriz(filas, columnas)
        mostrar_matriz(matriz)

    except ValueError:
        print("Debes ingresar números enteros válidos.")


if __name__ == "__main__":
    main()