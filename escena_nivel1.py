#! /usr/bin/env python
# -*- coding: utf-8 -*-
import pilasengine
from Kuro import KuroPP
from enemigos import Nuevoe
import random
from escena_ganar import Ganar
from time import time   

class Nivel1(pilasengine.escenas.Escena):
    def iniciar(self):
        mapa=self.pilas.actores.MapaTiled("data/Mapa/Nivel1/pacmanfinal1.tmx")
        self.kuro=self.pilas.actores.KuroPP(x=-1539,y=170)
        self.pilas.fisica.eliminar_paredes()
        self.pilas.fisica.eliminar_suelo()
        self.pilas.fisica.eliminar_techo()
        self.pilas.fisica.gravedad_y=-20
        self.lastChange = time()
        self.le=[]
        self.plataformas=[[-1503,-1308,161],[-1222,-1075,96],[-992,-862,96],[-804,-634,145],[-575,-380,209],[-325,-186,97],[-161,-26,161],[22,227,224],[28,228,97],[282,452,160],[539,709,225],[764,1004,129],[1051,1256,193]]
        self.plataformas1=[[-1504,-1309,-145],[-1224,-1079,-97],[-999,-859,-97],[-799,-634,-145],[-575,-380,-209],[-320,-190,-97],[-164,-30,-161],[25,230,-209],[25,230,-97],[281,448,-160],[538,708,-224],[763,998,-112],[1056,1256,-177]]
        
        self.enemigo1=self.pilas.actores.Nuevoe()
        self.enemigo1.escala=0.4
        self.plataforma1=self.plataformas[random.randint(0,12)]
        self.le.append(self.enemigo1)
        self.enemigo1.y=self.plataforma1[2]
        self.enemigo1.x=self.plataforma1[0]
        self.enemigo1.radio_de_colision=30
        self.direccion1=-1

        self.enemigo2=self.pilas.actores.Nuevoe()
        self.enemigo2.escala=0.4
        self.plataforma2=self.plataformas[random.randint(0,12)]
        self.le.append(self.enemigo2)
        self.enemigo2.y=self.plataforma2[2]
        self.enemigo2.x=self.plataforma2[0]
        self.enemigo2.radio_de_colision=30  
        self.direccion2=-1

        self.enemigo3=self.pilas.actores.Nuevoe()
        self.enemigo3.escala=0.4
        self.plataforma3=self.plataformas[random.randint(0,12)]
        self.le.append(self.enemigo3)
        self.enemigo3.y=self.plataforma3[2]
        self.enemigo3.x=self.plataforma3[0]
        self.enemigo3.radio_de_colision=30 
        self.direccion3=-1

        self.enemigo4=self.pilas.actores.Nuevoe()
        self.enemigo4.escala=0.4
        self.plataforma4=self.plataformas[random.randint(0,12)]
        self.le.append(self.enemigo4)
        self.enemigo4.y=self.plataforma4[2]
        self.enemigo4.x=self.plataforma4[0]
        self.enemigo4.radio_de_colision=30 
        self.direccion4=-1

        self.enemigo5=self.pilas.actores.Nuevoe()
        self.enemigo5.escala=0.4
        self.plataforma5=self.plataformas[random.randint(0,12)]
        self.le.append(self.enemigo5)
        self.enemigo5.y=self.plataforma5[2]
        self.enemigo5.x=self.plataforma5[0]
        self.enemigo5.radio_de_colision=30
        self.direccion5=-1

        self.enemigop=self.pilas.actores.Nuevoe()
        self.enemigop.escala=0.4
        self.le.append(self.enemigop)
        self.enemigop.y=17
        self.enemigop.x=1400
        self.enemigop.radio_de_colision=30
        self.direccionp=-1

        self.enemigob=self.pilas.actores.Nuevoe()
        self.enemigob.escala=0.4
        self.le.append(self.enemigob)
        self.enemigob.y=-48
        self.enemigob.x=1400
        self.enemigob.radio_de_colision=30
        self.direccionb=-1


        self.enemigob1=self.pilas.actores.Nuevoe()
        self.enemigob1.escala=0.4
        self.plataformab1=self.plataformas1[random.randint(0,12)]
        self.le.append(self.enemigob1)
        self.enemigob1.y=self.plataformab1[2]
        self.enemigob1.x=self.plataformab1[0]
        self.enemigob1.radio_de_colision=30
        self.direccionb1=-1

        self.enemigob2=self.pilas.actores.Nuevoe()
        self.enemigob2.escala=0.4
        self.plataformab2=self.plataformas1[random.randint(0,12)]
        self.le.append(self.enemigob2)
        self.enemigob2.y=self.plataformab2[2]
        self.enemigob2.x=self.plataformab2[0]
        self.enemigob2.radio_de_colision=30
        self.direccionb2=-1

        self.enemigob3=self.pilas.actores.Nuevoe()
        self.enemigob3.escala=0.4
        self.plataformab3=self.plataformas1[random.randint(0,12)]
        self.le.append(self.enemigob3)
        self.enemigob3.y=self.plataformab3[2]
        self.enemigob3.x=self.plataformab3[0]
        self.enemigob3.radio_de_colision=30
        self.direccionb3=-1

        self.enemigob4=self.pilas.actores.Nuevoe()
        self.enemigob4.escala=0.4
        self.plataformab4=self.plataformas1[random.randint(0,12)]
        self.le.append(self.enemigob4)
        self.enemigob4.y=self.plataformab4[2]
        self.enemigob4.x=self.plataformab4[0]
        self.enemigob4.radio_de_colision=30
        self.direccionb4=-1

        self.enemigob5=self.pilas.actores.Nuevoe()
        self.enemigob5.escala=0.4
        self.plataformab5=self.plataformas1[random.randint(0,12)]
        self.le.append(self.enemigob5)
        self.enemigob5.y=self.plataformab5[2]
        self.enemigob5.x=self.plataformab5[0]
        self.enemigob5.radio_de_colision=30
        self.direccionb5=-1

        self.pilas.colisiones.agregar(self.le, self.kuro, self.kuro.perder)

    def pasar_medio(self):
        self.pilas.fisica.gravedad_y *= -1

    def actualizar(self):
        pos = self.kuro.y ** 2
        now = time()
        if pos<100 and now - self.lastChange > 2:
            self.kuro.rotacion=[self.kuro.rotacion+180], .7 
            self.lastChange = now
            self.pasar_medio()

        if self.enemigo1.x<=self.plataforma1[0]:
            self.direccion1=1
        if self.enemigo1.x>=self.plataforma1[1]:
            self.direccion1=-1
        self.enemigo1.x+=self.direccion1*2.5

        if self.enemigo2.x<=self.plataforma2[0]:
            self.direccion2=1
        if self.enemigo2.x>=self.plataforma2[1]:
            self.direccion2=-1
        self.enemigo2.x+=self.direccion2*2.5

        if self.enemigo3.x<=self.plataforma3[0]:
            self.direccion3=1
        if self.enemigo3.x>=self.plataforma3[1]:
            self.direccion3=-1
        self.enemigo3.x+=self.direccion3*2.5

        if self.enemigo4.x<=self.plataforma4[0]:
            self.direccion4=1
        if self.enemigo4.x>=self.plataforma4[1]:
            self.direccion4=-1
        self.enemigo4.x+=self.direccion4*2.5

        if self.enemigo5.x<=self.plataforma5[0]:
            self.direccion5=1
        if self.enemigo5.x>=self.plataforma5[1]:
            self.direccion5=-1
        self.enemigo5.x+=self.direccion5*2.5

        if self.enemigop.x>=1400:
            self.direccionp=-1
        if self.enemigop.x<=-1523:
            self.direccionp=1
        self.enemigop.x+=self.direccionp*8


        if self.enemigob.x>=1400:
            self.direccionb=-1
        if self.enemigob.x<=-1523:
            self.direccionb=1
        self.enemigob.x+=self.direccionb*8

        if self.enemigob1.x<=self.plataformab1[0]:
            self.direccionb1=1
        if self.enemigob1.x>=self.plataformab1[1]:
            self.direccionb1=-1
        self.enemigob1.x+=self.direccionb1*2.5

        if self.enemigob2.x<=self.plataformab2[0]:
            self.direccionb2=1
        if self.enemigob2.x>=self.plataformab2[1]:
            self.direccionb2=-1
        self.enemigob2.x+=self.direccionb2*2.5

        if self.enemigob3.x<=self.plataformab3[0]:
            self.direccionb3=1
        if self.enemigob3.x>=self.plataformab3[1]:
            self.direccionb3=-1
        self.enemigob3.x+=self.direccionb3*2.5

        if self.enemigob4.x<=self.plataformab4[0]:
            self.direccionb4=1
        if self.enemigob4.x>=self.plataformab4[1]:
            self.direccionb4=-1
        self.enemigob4.x+=self.direccionb4*2.5

        if self.enemigob5.x<=self.plataformab5[0]:
            self.direccionb5=1
        if self.enemigob5.x>=self.plataformab5[1]:
            self.direccionb5=-1
        self.enemigob5.x+=self.direccionb5*2.5

        if self.kuro.x>=1530:
            self.pilas.escenas.Ganar()