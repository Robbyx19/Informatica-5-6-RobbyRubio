#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# LEGO EV3 – Introducción con Python
# Necesita: ev3dev2

from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C, SpeedPercent, MoveTank
from ev3dev2.sound import Sound
from time import sleep

def main():
    # Motores
    tank = MoveTank(OUTPUT_B, OUTPUT_C)

    # Altavoz
    sound = Sound()

    # Introducción
    sound.speak("Hola, soy tu robot EV3. ¡Vamos a empezar!")
    sleep(1)

    # Avanzar
    sound.speak("Avanzando")
    tank.on(SpeedPercent(40), SpeedPercent(40))
    sleep(2)

    # Girar
    sound.speak("Girando a la izquierda")
    tank.on(SpeedPercent(-30), SpeedPercent(30))
    sleep(1)

    # Parar
    tank.off()
    sound.speak("Programa de introducción finalizado")

if __name__ == "__main__":
    main()
