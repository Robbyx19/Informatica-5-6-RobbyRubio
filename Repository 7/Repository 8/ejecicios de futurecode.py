# 1
a = int(input("Ingresa el primer número: "))
b = int(input("Ingresa el segundo número: "))

if a > b:
    print("El primer número es mayor.")
elif a < b:
    print("El segundo número es mayor.")
else:
    print("Ambos números son iguales.")
# 2
nombre1 = input("Ingresa el primer nombre: ")
nombre2 = input("Ingresa el segundo nombre: ")

if nombre1.lower() == nombre2.lower():
    print("Los nombres son iguales.")
else:
    print("Los nombres son diferentes.")
# 3
frutas = ["manzana", "plátano", "naranja"]
print("Lista de frutas:", frutas)

nueva_fruta = input("Agrega una fruta: ")
frutas.append(nueva_fruta)

print("Lista actualizada:", frutas)
# 4 
numeros = [10, 20, 30, 40, 50]

print("Primer número:", numeros[0])
print("Último número:", numeros[-1])
print("Tercer número:", numeros[2])
# 5
lista = list(range(1, 11))
print("Lista del 1 al 10:", lista)
# 6
animales = ["perro", "gato", "conejo", "pez"]
print("Número de animales:", len(animales))
# 7
colores = ["rojo", "verde", "azul", "amarillo"]

for color in colores:
    print("Color:", color)
# 8
materias = ["matemáticas", "historia", "biología", "física"]
buscar = input("¿Qué materia buscas?: ")

if buscar.lower() in materias:
    print("La materia está en la lista.")
else:
    print("No se encontró la materia.")

# 9
numeros = [1, 3, 5, 7, 9, 10, 13]

for n in numeros:
    if n == 10:
        print("¡Se encontró el número 10! Deteniendo el bucle...")
        break
    print("Número:", n)
# 10    
nombres = ["Ana", "Luis", "Karla", "José"]

for i in range(len(nombres)):
    print(f"Posición {i}: {nombres[i]}")

