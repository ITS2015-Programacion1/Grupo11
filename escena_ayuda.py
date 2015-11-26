#! /usr/bin/env python
# -*- coding: utf-8 -*-
import pilasengine
from Kuro import KuroPP
from escena_nivel1 import Nivel1
from time import time


class Ayuda(pilasengine.escenas.Escena):
    def iniciar(self):
        mapa=self.pilas.actores.MapaTiled('data/Mapa/Ayuda/ayuda.tmx')
        self.kuro=self.pilas.actores.KuroPP(x=-720,y=33)
        self.pilas.fisica.eliminar_paredes()
        self.pilas.fisica.eliminar_suelo()
        self.pilas.fisica.eliminar_techo()
        self.pilas.fisica.gravedad_y=-15
        self.lastChange = time()
        self.a=0
        self.texto=self.pilas.actores.Texto("Kuro puede mover hacia la izquierda, \nderecha y hacia arriba,\n estos movimientos se pueden realizar\n con las flechas del teclado.\n cuando llegues al final \ncomenzara el nivel 1.",y=150,)
    def pasar_medio(self):
        self.pilas.fisica.gravedad_y *= -1

    def actualizar(self):
        self.a+=1
        if self.a==300:
            self.texto.eliminar()
            texto2=self.pilas.actores.Texto("Kuro puede cambiar su gravedad pasando \npor el medio, pero necesitara un impulso",y=150,)

        if self.kuro.x >= 730:
            self.pilas.escenas.Nivel1()

        pos = self.kuro.y ** 2
        now = time()
        if pos<100 and now - self.lastChange > 2:
            self.kuro.rotacion=[self.kuro.rotacion+180], .7 
            self.lastChange = now
            self.pasar_medio()