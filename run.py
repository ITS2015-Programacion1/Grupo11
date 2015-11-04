#! /usr/bin/env python
# -*- coding: utf-8 -*-
import pilasengine
import random

pilas = pilasengine.iniciar(ancho=3200,alto=480)

mapa=pilas.actores.MapaTiled("pacmanfinal.tmx")

class Kuro(pilasengine.actores.Actor):
    def iniciar(self):
        self.imagen = "data/Kuro/mario.png"
        self.figura = pilas.fisica.Rectangulo(self.x, self.y, 20, 33)
        self.figura.sin_rotacion = True
        self.figura.escala_de_gravedad = 2
        self.sensor_pies = pilas.fisica.Rectangulo(self.x, self.y, 17, 5, sensor=True, dinamica=False)

    def actualizar(self):
        velocidad = 10
        salto = 5
        self.x = self.figura.x
        self.y = self.figura.y
	pilas.camara.x = kuro.x        
        if pilas.control.izquierda:
            self.figura.x -= velocidad
            self.espejado = True

        if pilas.control.derecha:
            self.figura.x += velocidad
            self.espejado = False

        if self.esta_pisando_el_suelo():
            if self.pilas.control.arriba:
                self.figura.impulsar(0, salto)

        self.sensor_pies.x = self.x
        self.sensor_pies.y = self.y - 20

    def esta_pisando_el_suelo(self):
        return len(self.sensor_pies.figuras_en_contacto) > 0


def si_pasa_por_el_medio(hola):
    while True:
        print hola

medio = pilas.fisica.Rectangulo(0, 0, 636, 1, sensor=True, dinamica=True)

pilas.actores.vincular(Kuro)
kuro=Kuro(pilas)


pilas.ejecutar()

