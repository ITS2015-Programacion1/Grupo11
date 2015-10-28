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
        self.figura = pilas.fisica.Rectangulo(self.x, self.y)
        self.saltando=False
        
    def actualizar(self):
        if pilas.control.izquierda:
            self.x -= 5
            self.espejado = True
            
        if pilas.control.derecha:
            self.x += 5
            self.espejado = False
        if pilas.control.arriba:           
            if not self.saltando:
                self.hacer("Subir")

kuro=Kuro(pilas)

pilas.ejecutar()