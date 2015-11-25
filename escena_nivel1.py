#! /usr/bin/env python
# -*- coding: utf-8 -*-
import pilasengine
from Kuro import KuroPP
from enemigos import Nuevoe
import random
from escena_ganar import Ganar
from time import time   

class Nivel1(pilasengine.escenas.Escena):
    def perder(self):
        self.kuro.x=-1539
        self.kuro.y=170

    def iniciar(self):
        mapa=self.pilas.actores.MapaTiled("data/Mapa/Nivel1/pacmanfinal.tmx")
        self.kuro=self.pilas.actores.KuroPP(x=-1539,y=170)
        self.pilas.fisica.eliminar_paredes()
        self.pilas.fisica.eliminar_suelo()
        self.pilas.fisica.eliminar_techo()
        self.pilas.fisica.gravedad_y=-20
        self.lastChange = time()
        self.le=[]
        self.plataformas=[[-1488,-1288,145],[-1208,-1068,80],[-978,-838,81],[-788,-619,113],[-569,-369,177],[-308,-178,81],[-151,18,145],[77,277,81],[77,277,209],[331,501,145],[589,749,209],[809,1039,113],[1101,1301,209]]
 
        self.enemigo1=self.pilas.actores.Nuevoe()
        self.plataforma1=self.plataformas[random.randint(0,12)]
        self.le.append(self.enemigo1)
        self.enemigo1.y=self.plataforma1[2]
        self.enemigo1.x=self.plataforma1[0]
        self.direccion1=-1

        self.enemigo2=self.pilas.actores.Nuevoe()
        self.plataforma2=self.plataformas[random.randint(0,12)]
        self.le.append(self.enemigo2)
        self.enemigo2.y=self.plataforma2[2]
        self.enemigo2.x=self.plataforma2[0]
        self.direccion2=-1

        self.enemigo3=self.pilas.actores.Nuevoe()
        self.plataforma3=self.plataformas[random.randint(0,12)]
        self.le.append(self.enemigo3)
        self.enemigo3.y=self.plataforma3[2]
        self.enemigo3.x=self.plataforma3[0]
        self.direccion3=-1

        self.enemigo4=self.pilas.actores.Nuevoe()
        self.plataforma4=self.plataformas[random.randint(0,12)]
        self.le.append(self.enemigo4)
        self.enemigo4.y=self.plataforma4[2]
        self.enemigo4.x=self.plataforma4[0]
        self.direccion4=-1

        self.enemigo5=self.pilas.actores.Nuevoe()
        self.plataforma5=self.plataformas[random.randint(0,12)]
        self.le.append(self.enemigo5)
        self.enemigo5.y=self.plataforma5[2]
        self.enemigo5.x=self.plataforma5[0]
        self.direccion5=-1

        self.pilas.colisiones.agregar(self.le, self.kuro, self.perder)

    def pasar_medio(self):
        self.pilas.fisica.gravedad_y *= -1
        
    def actualizar(self):
        pos = self.kuro.y ** 2
        now = time()
        if pos<100 and now - self.lastChange > 2:
            self.kuro.rotacion=[self.kuro.rotacion+180], .7 
            self.lastChange = now
            self.pasar_medio()
        if pos>60000 and now - self.lastChange > 2:
            self.kuro.rotacion+=180
            self.lastChange=now
            self.pasar_medio
            self.kuro.y=self.kuro.y*-1

        if self.enemigo1.x<=self.plataforma1[0]:
            self.direccion1=1
        if self.enemigo1.x>=self.plataforma1[1]:
            self.direccion1=-1
        self.enemigo1.x+=self.direccion1*2.5

        if self.enemigo2.x<=self.plataforma2[0]:
            self.direccion2=1
        if self.enemigo1.x>=self.plataforma1[1]:
            self.direccion2=-1
        self.enemigo2.x+=self.direccion2*2.5

        if self.enemigo3.x<=self.plataforma3[0]:
            self.direccion3=1
        if self.enemigo1.x>=self.plataforma1[1]:
            self.direccion3=-1
        self.enemigo3.x+=self.direccion3*2.5

        if self.enemigo4.x<=self.plataforma4[0]:
            self.direccion4=1
        if self.enemigo1.x>=self.plataforma1[1]:
            self.direccion4=-1
        self.enemigo4.x+=self.direccion4*2.5

        if self.enemigo5.x<=self.plataforma5[0]:
            self.direccion5=1
        if self.enemigo1.x>=self.plataforma1[1]:
            self.direccion5=-1
        self.enemigo5.x+=self.direccion5*2.5

        if self.kuro.x>=1530:
            self.pilas.escenas.Ganar()
