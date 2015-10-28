# coding: utf-8
import pilasengine
import sys

pilas = pilasengine.iniciar()
pilas.fondos.Selva()

def niveles():
    print "NIVELES"

def iniciar_juego():
    pilas.fondos.Espacio()
    opciones = [
        ('Comenzar a jugar', self.comenzar),
        ('Ayuda',self.ayuda),
        ('Niveles',niveles),
        ('Salir', self.salir)]
    self.menu = pilas.actores.Menu(opciones)

def salir():
    sys.exit(0)

def ayuda():
    print "(Escribir controles, de que se va a tratar, etc)"

menu = pilas.actores.Menu(
            [
                ('iniciar juego', iniciar_juego),
                ('ayuda', ayuda),
                ('niveles', niveles),
                ('salir', salir),
            ])

pilas.ejecutar()