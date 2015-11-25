#! /usr/bin/env python
# -*- coding: utf-8 -*-
import pilasengine
import random

class Nuevoe(pilasengine.actores.Actor):
    def iniciar(self):
        self.imagen = "pacman.jpeg"
        self.figura = self.pilas.fisica.Rectangulo(self.x, self.y, 20, 33)
        self.figura.sin_rotacion = True
        self.e=[]
        self.ecant=[]
        self.cant=3
        for a in range(self.cant):
            z=random.randint(1,13)
            self.ecant.append(z)
        self.plataformas1=[[-1488.8,-1288.8,145.1],[-1208.8,-1068.8,80.9],[-978.8,-838.8,81.1],[-788.8,-619,113.1],[-569,-369,177],[-308.6,-178.6,81],[-151.2,18.8,145.1],[77.1,277.1,80.9],[77.1,277.1,209],[331.1,501.4,145],[589.6,749.6,209],[809.6,1039.6,113],[1101.1,1301.1,209]]

    def crear(self):
        for i in range (2):
            self.enemigo= self.pilas.actores.Nuevoe()
            self.e.append(self.enemigo)
            self.x= self.plataformas1[self.ecant[i-1]][1]
            self.y= self.plataformas1[self.ecant[i-1]][2]
            self.enemigo.escala=0.5

    def actualizar(self):
        
        self.figura.x = self.x
        self.figura.y = self.y
        #if self.e:
        for i in range(3):
            if len(self.e)>0:
                a=self.ecant[self.e.index(self.enemigo)]
                if (self.x == self.plataformas1[i][0]):
                        #self.pilas.utils.interpolar(self.e[i-1],'x',self.plataformas1[a][1],1)
                    self.x=self.x+1
                #if len(self.e)>1:
                    #a=self.ecant[self.e.index(self.enemigo)]
                if (self.x == self.plataformas1[i][1]):
                    self.x=self.x-1
                
    #self.e.index(self.enemigo)