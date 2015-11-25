#! /usr/bin/env python
# -*- coding: utf-8 -*-
import pilasengine
import random

pilas = pilasengine.iniciar()
class Nuevoe(pilasengine.actores.Actor):
    def iniciar(self):
        self.imagen = "pacman.jpeg"
        self.figura = pilas.fisica.Rectangulo(self.x, self.y, 20, 33)
        self.figura.sin_rotacion = True
        self.e=[]
        self.ecant=[]
        self.cant=3
        for a in range(cant):
            z=random.randint(1,13)
            self.ecant.append(z)

        self.plataformas1=[[-1488.8,-1288.8,145.1],[-1208.8,-1068.8,80.9],[-978.8,-838.8,81.1],[-788.8,-619,113.1],[-569,-369,177],[-308.6,-178.6,81],[-151.2,18.8,145.1],[77.1,277.1,80.9],[77.1,277.1,209],[331.1,501.4,145],[589.6,749.6,209],[809.6,1039.6,113],[1101.1,1301.1,209]]
    def crear(self):
        for i in range (cant):
            self.enemigo= self.pilas.actores.Nuevoe()
            self.e.append(self.enemigo)
            self.x= self.plataformas1[e.index(enemigo)][1]
            self.y= self.plataformas1[e.index(enemigo)][3]

    def actualizar(self):
        self.figura.x = self.x
        self.figura.y = self.x      
        if (self.x == self.plataformas1[e.index(enemigo)][1]):
            pilas.utils.interpolar(enemigo, 'x', self.plataformas1[e.index(enemigo)][2], 1)
        if (self.x == self.plataformas1[e.index(enemigo)][2]):
            pilas.utils.interpolar(enemigo, 'X',self.plataformas1[e.index(enemigo)][1] , 1)

    
