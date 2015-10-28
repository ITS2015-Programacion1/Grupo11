#! /usr/bin/env python
# -*- coding: utf-8 -*-
import pilasengine
import random
from compo import Subir

pilas = pilasengine.iniciar()

pilas.comportamientos.vincular(Subir)

class Kuro(pilasengine.actores.Actor):
    def iniciar(self):
        self.imagen = "mario.png"
        self.figura = pilas.fisica.Rectangulo(self.x, self.y, 17)
        self.figura.sin_rotacion = True
        self.figura.escala_de_gravedad = 2
        self.saltando=False
    
    def actualizar(self):
        self.x = self.figura.x
        self.y = self.figura.y
        if pilas.control.izquierda:
            self.figura.x -= 5
            self.espejado = True
        if pilas.control.derecha:
            self.figura.x += 5
            self.espejado = False
        if pilas.control.arriba:
            if not self.saltando:
                self.figura.y+=5
                #self.hacer("Subir")

pilas.actores.vincular(Kuro)

kuro=Kuro(pilas)

caja=pilas.actores.Caja()
caja.aprender(pilas.habilidades.Arrastrable)

pilas.fisica.definir_gravedad(0,0)

fondo= pilas.fondos.Fondo("plataforma.png")

rectangulo=pilas.fisica.Rectangulo(-170.0,18.0,355,30,dinamica=False)
rectangulo=pilas.fisica.Rectangulo(264.0,15.8,100,30,dinamica=False)
rectangulo=pilas.fisica.Rectangulo(181.3,-108.7,325,25,dinamica=False)
rectangulo=pilas.fisica.Rectangulo(-4.0,137.2,155,25,dinamica=False)
rectangulo=pilas.fisica.Rectangulo(231.8,190.8,180,25,dinamica=False)



pilas.ejecutar()