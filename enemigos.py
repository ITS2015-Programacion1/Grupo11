#! /usr/bin/env python
# -*- coding: utf-8 -*-
import pilasengine
import random

pilas = pilasengine.iniciar()
class Enemigo(pilasengine.actores.Actor):
    def iniciar(self):
        self.imagen = ""
        self.figura = pilas.fisica.Rectangulo(self.x, self.y, 20, 33)
        self.figura.sin_rotacion = True

    def actualizar(self):
        velocidad = 10
        self.x = self.figura.x
        self.y = self.figura.x      
        
        #pilas.utils.interpolar(enemigo, 'x', 0, 1)
        #pilas.utils.interpolar(enemigo, 'y', 0, 1)

