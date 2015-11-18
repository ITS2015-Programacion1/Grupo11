#! /usr/bin/env python
# -*- coding: utf-8 -*-
import pilasengine
from Kuro import KuroPP
import random

class Nivel1(pilasengine.escenas.Escena):
    def iniciar(self):
        mapa=self.pilas.actores.MapaTiled("data/Mapa/pacmanfinal.tmx")
        kuro=self.pilas.actores.KuroPP(x=-1273,y=100)
        medio=self.pilas.fisica.Rectangulo(0, 0, 1500, 1, sensor=True, dinamica=False)