
# 1
palabra = 'Hola'
nombre = 'Mundo'
frase = palabra + ' ' + nombre
print(frase)
palabra = 'Adiós'
print(frase)




 2#
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))
suma = num1 + num2
print(f"La suma de los números es: {suma}")


#  3
celsius = float(input("Ingresa la temperatura en grados Celsius: "))
fahrenheit = celsius * 9/5 + 32
print(f"{celsius} grados Celsius son {fahrenheit} grados Fahrenheit.")


# 4
numero = int(input("Ingresa un número: "))
if numero % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")


# 5 
palabra = input("Ingresa una palabra: ").lower()
vocales = "aeiou"
contador = 0
for letra in palabra:
    if letra in vocales:
        contador += 1
print(f"La palabra '{palabra}' tiene {contador} vocales.")
# 6
inicio = int(input("Ingresa el número de inicio del rango: "))
fin = int(input("Ingresa el número final del rango: "))
resultado = 1
for i in range(inicio, fin + 1):
    resultado *= i
print(f"La multiplicación de los números del {inicio} al {fin} es {resultado}.")
