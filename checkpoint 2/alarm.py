def revisar(sistema_activado, movimiento_detectado, puerta_abierta, despues_del_atardecer):
    if sistema_activado:
        if movimiento_detectado:
            return "¡Alarma: INTRUSO DETECTADO!"
        elif puerta_abierta:
            return "Alerta silenciosa: ¡La puerta está abierta!"
        else:
            return ""
    else:
        if despues_del_atardecer and movimiento_detectado:
            return "Bienvenido a casa. Encendiendo la luz."
        else:
            return ""

escenarios = [
    ("Escenario 1: Activado y movimiento", True, True, False, True),
    ("Escenario 2: Activado y puerta abierta", True, False, True, False),
    ("Escenario 3: Desactivado y prender luz", False, True, False, True),
    ("Escenario 4: Desactivado sin acción", False, False, False, True),
]

for nombre, sistema_activado, movimiento_detectado, puerta_abierta, despues_del_atardecer in escenarios:
    print(nombre)
    salida = revisar(sistema_activado, movimiento_detectado, puerta_abierta, despues_del_atardecer)
    if salida:
        print(salida)
    else:
        print("(sin salida)")
    print()
