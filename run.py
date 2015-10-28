#! /usr/bin/env python
# -*- coding: utf-8 -*-
import pilasengine
import random
from compo import Subir

pilas = pilasengine.iniciar()

pilas.comportamientos.vincular(Subir)

class Kuro(pilasengine.actores.Actor):
    def iniciar(self):
        self.imagen = "data/Kuro/mario.png"
        self.figura = pilas.fisica.Rectangulo(self.x, self.y, 20, 33)
        self.figura.sin_rotacion = True
        self.figura.escala_de_gravedad = 6
        self.saltando=False
        self.sensor_pies = pilas.fisica.Rectangulo(self.x, self.y, 5, 5, sensor=True, dinamica=False)

    def actualizar(self):
        self.x = self.figura.x
        self.y = self.figura.y
        if pilas.control.izquierda:
            self.figura.x -= 5
            self.espejado = True
        if pilas.control.derecha:
            self.figura.x += 5
            self.espejado = False
        if self.esta_pisando_el_suelo():
            if self.pilas.control.arriba:
                self.figura.impulsar(0, 5)

        self.sensor_pies.x = self.x
        self.sensor_pies.y = self.y - 20

    def esta_pisando_el_suelo(self):
        return len(self.sensor_pies.figuras_en_contacto) > 0
"""        if pilas.control.arriba:
            if not self.saltando:
                self.figura.y+=5
                #self.hacer("Subir")
"""

pilas.actores.vincular(Kuro)

kuro=Kuro(pilas)

mapa=pilas.actores.MapaTiled("plataformas.tmx")


pilas.ejecutar()

