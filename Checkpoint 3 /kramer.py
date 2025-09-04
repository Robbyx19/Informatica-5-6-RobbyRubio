def main():
    total = 0  # Total money collected

    while True:
        greeting = input("Greeting: ").strip().lower()

        if greeting.startswith("hello"):
            cambio  = 0
        elif greeting.startswith("h"):
            cambio  = 20
        else:
            cambio = 100

        total += cambio 
        print(f"recibes : ${cambio }")
        print(f"Total de totales: ${total}\n")

        if cambio == 100:
            break

if __name__ == "__main__":
    main()
