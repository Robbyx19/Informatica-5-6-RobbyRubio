# faces.py

def main():
    # Pedimos texto al usuario
    texto = input("Escribe algo: ")
    
    # Reemplazamos caritas
    texto = texto.replace(":)", "🙂")
    texto = texto.replace(":(", "🙁")
    
    # Mostramos el resultado
    print(texto)

# Llamamos a main cuando se ejecute el archivo
if __name__ == "__main__":
    main()
