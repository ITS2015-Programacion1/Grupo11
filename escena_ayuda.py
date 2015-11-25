#! /usr/bin/env python
# -*- coding: utf-8 -*-
import pilasengine
from Kuro import KuroPP

class Ayuda(pilasengine.escenas.Escena):
    def iniciar(self):
        mapa=self.pilas.actores.MapaTiled("data/Mapa/Ayuda/ayuda.tmx")
        self.kuro=self.pilas.actores.KuroPP(x=1500,y=16)
        self.kuro.aprender("LimitadoABordesDePantalla")
