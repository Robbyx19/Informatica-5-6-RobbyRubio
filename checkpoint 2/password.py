def main():
    password = input("Crea una contraseña: ")
    print("Contraseña guardada. Pulsa Enter para continuar.")
    input()  # solo pausa
    check_password(password)

def check_password(password):
    intento = input("Adivina la contraseña: ")
    if intento == password:
        print("¡Acertaste la contraseña!")
    else:
        print("Contraseña incorrecta.")
    print("El programa terminó.")

main()
