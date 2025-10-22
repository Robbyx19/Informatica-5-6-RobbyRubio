# 1
numero = int(input("Ingresa un número: "))

if numero > 0:
    print("El número es positivo.")
else:
    print("El número es negativo o cero.")

# 2
numero = int(input("Ingresa un número: "))

if numero % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")
# 3
edad = int(input("Ingresa tu edad: "))

if edad >= 18:
    print("Puedes votar.")
else:
    print("Aún no puedes votar.")
# 4
a = int(input("Ingresa el primer número: "))
b = int(input("Ingresa el segundo número: "))
c = int(input("Ingresa el tercer número: "))

if a > b and a > c:
    print("El primer número es el mayor.")
elif b > a and b > c:
    print("El segundo número es el mayor.")
else:
    print("El tercer número es el mayor.")
# 5
calificacion = float(input("Ingresa tu calificación: "))

if calificacion >= 70:
    print("Aprobado ✅")
else:
    print("Reprobado ❌")
# 6
usuario = input("Ingresa tu nombre de usuario: ")

if usuario == "admin":
    print("Bienvenido, administrador.")
else:
    print("Acceso denegado.")
# 7
mes = input("Ingresa el mes actual: ").lower()

if mes in ["diciembre", "enero", "febrero"]:
    print("Es invierno.")
elif mes in ["marzo", "abril", "mayo"]:
    print("Es primavera.")
elif mes in ["junio", "julio", "agosto"]:
    print("Es verano.")
elif mes in ["septiembre", "octubre", "noviembre"]:
    print("Es otoño.")
else:
    print("Mes no válido.")
# 8
numero = int(input("Ingresa un número: "))

if numero > 0:
    print("Es positivo.")
elif numero < 0:
    print("Es negativo.")
else:
    print("Es cero.")
# 9
edad = int(input("Ingresa tu edad: "))
tiene_ine = input("¿Tienes INE? (sí/no): ").lower()

if edad >= 18 and tiene_ine == "sí":
    print("Puedes entrar al evento.")
else:
    print("No cumples los requisitos.")
# 10
import snoop

snoop
def evaluar_numero():
    n = int(input("Ingresa un número: "))
    if n % 2 == 0:
        print("El número es par.")
    else:
        print("El número es impar.")

evaluar_numero()

