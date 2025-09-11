num1 = float(input("Primer número: "))
operador = input("Operador (+, -, * o /): ")
num2 = float(input("Segundo número: "))

if operador == "+":
    resultado = num1 + num2
elif operador == "-":
    resultado = num1 - num2
elif operador == "*":
    resultado = num1 * num2
elif operador == "/":
    resultado = num1 / num2

print(round(resultado, 1))
