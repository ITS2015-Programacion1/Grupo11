#! /usr/bin/env python
# -*- coding: utf-8 -*-
import pilasengine
from Kuro import KuroPP
import random

class Nivel1(pilasengine.escenas.Escena):

    def iniciar(self):
    	print 'Hola<'
        mapa=self.pilas.actores.MapaTiled("data/Mapa/pacmanfinal.tmx")        
        #pingu =self.pilas.actores.Pingu()
        kuro=self.pilas.actores.KuroPP()

    def ejecutar(self):
    	print 'Se ejecuto'
        