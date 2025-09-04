while True:
    try:
        limite = int(input("Ingresa el número límite: "))
        paso = int(input("Ingresa el tamaño del paso: "))

        if limite <= 0 or paso <= 0:
            print("Por favor, ingresa números positivos mayores que cero.\n")
            continue

        print("\nNúmeros generados:")
        for numero in range(paso, limite + 1, paso):
            print(numero)
        break

    except:
        print("Entrada inválida. Por favor, ingresa solo números.\n")
