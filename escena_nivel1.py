#! /usr/bin/env python
# -*- coding: utf-8 -*-
import pilasengine
from Kuro import KuroPP
from enemigos import Nuevoe
import random
from time import time   

class Nivel1(pilasengine.escenas.Escena):
    def crear_enemigo(self):
        for i in range (3):
            self.e=[]
            self.plataformas1=[[-1488.8,-1288.8,145.1],[-1208.8,-1068.8,80.9],[-978.8,-838.8,81.1],[-788.8,-619,113.1],[-569,-369,177],[-308.6,-178.6,81],[-151.2,18.8,145.1],[77.1,277.1,80.9],[77.1,277.1,209],[331.1,501.4,145],[589.6,749.6,209],[809.6,1039.6,113],[1101.1,1301.1,209]]
            self.enemigo = self.pilas.actores.Nuevoe()
            self.e.append(self.enemigo)
            self.x= self.plataformas1[i][0]
            self.y= self.plataformas1[i][2]

    def iniciar(self):
        mapa=self.pilas.actores.MapaTiled("data/Mapa/Nivel1/pacmanfinal.tmx")
        self.kuro=self.pilas.actores.KuroPP(x=-1539,y=170)
        self.pilas.fisica.eliminar_paredes()
        self.pilas.fisica.eliminar_suelo()
        self.pilas.fisica.eliminar_techo()
        self.pilas.fisica.gravedad_y=-20
        self.lastChange = time()
        nuevo=self.pilas.actores.Nuevoe()
        nuevo.crear()
        #self.e=[]
        #self.plataformas1=[[-1488.8,-1288.8,145.1],[-1208.8,-1068.8,80.9],[-978.8,-838.8,81.1],[-788.8,-619,113.1],[-569,-369,177],[-308.6,-178.6,81],[-151.2,18.8,145.1],[77.1,277.1,80.9],[77.1,277.1,209],[331.1,501.4,145],[589.6,749.6,209],[809.6,1039.6,113],[1101.1,1301.1,209]]
        #self.crear_enemigo()

    def pasar_medio(self):
        self.pilas.fisica.gravedad_y *= -1
        
    def actualizar(self):
        print str(self.kuro.y ** 2)
        pos = self.kuro.y ** 2
        now = time()
        if pos<100 and now - self.lastChange > 2:
            print "aca cambia"
            self.kuro.rotacion=[self.kuro.rotacion+180], .7 
            self.lastChange = now
            self.pasar_medio()
        if pos>60000 and now - self.lastChange > 2:
            print "aca cambia"
            self.kuro.rotacion+=180
            self.lastChange=now
            self.pasar_medio
            self.kuro.y=self.kuro.y*-1