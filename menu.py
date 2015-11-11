# coding: utf-8
import pilasengine
from escena_nivel1 import Nivel1
from Kuro import KuroPP
import sys


pilas = pilasengine.iniciar()
pilas.fondos.Espacio()
pilas.escenas.vincular(Nivel1)
pilas.actores.vincular(KuroPP)
def iniciar_juego():
    
    menu.eliminar
    pilas.escenas.Nivel1()

def ayuda():
    print "(Escribir controles, de que se va a tratar, etc)"

def niveles():
    print "NIVELES"

def salir():
    sys.exit(0)

menu = pilas.actores.Menu(
            [
                ('iniciar juego', iniciar_juego),
                ('ayuda', ayuda),
                ('niveles', niveles),
                ('salir', salir),
            ])

pilas.ejecutar()