# 1
numeros = [5, 2, 9, 1, 7]

numeros.sort()       # Ordenar
numeros.append(10)   # Agregar
numeros.remove(2)    # Eliminar
print("Lista modificada:", numeros)
# 2
valores = [3, 8, 6, 2, 10]

print("Máximo:", max(valores))
print("Mínimo:", min(valores))
print("Suma total:", sum(valores))
print("Promedio:", sum(valores) / len(valores))
# 3
texto = "  hola mundo en python  "

print("Original:", texto)
print("Mayúsculas:", texto.upper())
print("Minúsculas:", texto.lower())
print("Sin espacios:", texto.strip())
print("Reemplazado:", texto.replace("python", "Futurecode"))
# 4
cadena = "Python"
# Las cadenas no se pueden modificar directamente
nueva_cadena = cadena.replace("P", "J")

print("Original:", cadena)
print("Modificada:", nueva_cadena)
# 5
nombre = "Robby"
edad = 19

print(f"Hola, mi nombre es {nombre} y tengo {edad} años.")
# 6 
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print("a == b:", a == b)  # Compara contenido
print("a is b:", a is b)  # Compara si son el mismo objeto
print("a is c:", a is c)  # True, apuntan al mismo objeto
# 7
lista1 = [10, 20, 30]
lista2 = lista1  # Ambas variables apuntan a la misma lista

lista2.append(40)
print("Lista1:", lista1)
print("Lista2:", lista2)
# 8
numeros = [1, 2, 3, 4, 5]
print("Original:", numeros)

for n in numeros[:]:  # Copia de la lista
    if n % 2 == 0:
        numeros.remove(n)

print("Sin números pares:", numeros)
# 9
frase1 = "Ella dijo: 'Hola a todos!'"
frase2 = 'El profesor respondió: "Buenos días."'

print(frase1)
print(frase2)
# 10    
def duplicar(lista):
    nueva = []
    for n in lista:
        nueva.append(n * 2)
    return nueva

numeros = [1, 2, 3]
resultado = duplicar(numeros)
print("Resultado:", resultado)
