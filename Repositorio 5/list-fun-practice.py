def get_user_list():
    user_list = []
    print("Ingresa valores numéricos para agregarlos a una lista. Ingresa 0 para terminar.")

    while True:
        try:
            value = int(input("Ingresa un número: "))
            if value == 0:
                break
            user_list.append(value)

            print("\nLista en orden de adición:", user_list)

            sorted_list = sorted(user_list)
            print("Lista ordenada de menor a mayor:", sorted_list)

        except ValueError:
            print("Entrada no válida. Por favor, ingresa un número entero.")

    return user_list

def length(my_list):
    return len(my_list)

def mean(my_list):
    if not my_list:
        return 0
    return sum(my_list) / len(my_list)

def range_of_list(my_list):
    if not my_list:
        return 0
    return max(my_list) - min(my_list)

def main():
    my_numbers = get_user_list()
    print("\n--------------------------------------------------")
    print("Lista final para los cálculos:", my_numbers)

    print(f"Longitud de la lista: {length(my_numbers)}")
    print(f"Media aritmética de la lista: {mean(my_numbers)}")
    print(f"Rango de la lista (diferencia entre el valor más grande y el más pequeño): {range_of_list(my_numbers)}")

if __name__ == "__main__":
    main()