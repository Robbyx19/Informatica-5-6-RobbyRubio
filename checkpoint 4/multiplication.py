numero = input("escribe un numero positivo chavalon: ")
numero = int(numero)
i = int

if numero > 0:
    print("Tablin de tablines de el ", numero)

    for   i in range(1, 11):
        resultado = numero * i
        print(numero, "x", i, "=", resultado)
else:
    print("no te hagas el numero no es positivo.") 