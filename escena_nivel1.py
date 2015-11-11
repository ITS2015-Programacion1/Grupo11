#! /usr/bin/env python
# -*- coding: utf-8 -*-
import pilasengine
from Kuro import KuroPP
import random

pilas = pilasengine.iniciar()

class nivel1(pilasengine.escenas.Escena):

    def iniciar(self):
        fondo=pilas.fondos.Pasto()
        mapa=pilas.actores.MapaTiled("data/Mapa/pacmanfinal.tmx")

    def ejecutar(self):
        pilas.actores.vincular(KuroPP)
        kuro=pilas.actores.KuroPP()

pilas.ejecutar()