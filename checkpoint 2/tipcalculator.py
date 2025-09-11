def main():
    dolares = dollars_to_float(input("¿Cuánto costó la comida? "))
    porcentaje = percent_to_float(input("¿Qué porcentaje quieres dejar de propina? "))
    propina = dolares * porcentaje
    print(f"Deja ${propina:.2f}")

def dollars_to_float(d):
    d = d.replace("$", "")
    return float(d)

def percent_to_float(p):
    p = p.replace("%", "")
    return float(p) / 100

main()
