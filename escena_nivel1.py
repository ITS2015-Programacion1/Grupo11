#! /usr/bin/env python
# -*- coding: utf-8 -*-
import pilasengine
from Kuro import KuroPP
#from enemigos import Nuevoe
import random
from time import time   

class Nivel1(pilasengine.escenas.Escena):
    def iniciar(self):
        mapa=self.pilas.actores.MapaTiled("data/Mapa/Nivel1/pacmanfinal.tmx")
        self.kuro=self.pilas.actores.KuroPP(x=-1539,y=170)
        self.pilas.fisica.eliminar_paredes()
        self.pilas.fisica.eliminar_suelo()
        self.pilas.fisica.eliminar_techo()
        self.pilas.fisica.gravedad_y=-20
        self.lastChange = time()
        #Nuevoe.crear

    def pasar_medio(self):
        self.pilas.fisica.gravedad_y *= -1
        
    def actualizar(self):
        print str(self.kuro.y ** 2)
        pos = self.kuro.y ** 2
        now = time()
        if pos<100 and now - self.lastChange > 2:
            self.kuro.rotacion=[self.kuro.rotacion+180], .7 
            self.lastChange = now
            self.pasar_medio()