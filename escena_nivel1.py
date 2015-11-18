#! /usr/bin/env python
# -*- coding: utf-8 -*-
import pilasengine
from Kuro import KuroPP
import random
from time import time   

class Nivel1(pilasengine.escenas.Escena):
    def iniciar(self):
        mapa=self.pilas.actores.MapaTiled("data/Mapa/pacmanfinal.tmx")
        self.kuro=self.pilas.actores.KuroPP(x=-1539,y=170)
        self.pilas.fisica.eliminar_paredes()
        self.pilas.fisica.eliminar_suelo()
        self.pilas.fisica.eliminar_techo()
        self.pilas.fisica.gravedad_y=-20
        self.lastChange = time()
               

        #self.pilas.colisiones.agregar(self.sensor_Kuro, self.medio, self.pasar_medio)


    def pasar_medio(self):
        print "Pasa por el medio: ".format(self.pilas.fisica.gravedad_y)
        self.kuro.rotacion = 180
        self.pilas.fisica.gravedad_y *= -1
        
    def actualizar(self):
        pos = self.kuro.y ** 2        
        now = time()
        if pos<1 and  now - self.lastChange > 2:
            self.lastChange = now            
            self.pasar_medio()

        #self.sensor_Kuro.x=self.kuro.x
        #self.sensor_Kuro.y=self.kuro.y