#! /usr/bin/env python
# -*- coding: utf-8 -*-
import pilasengine
import random

pilas = pilasengine.iniciar()

class Kuro(pilasengine.actores.Actor):
    def iniciar(self):
        self.imagen = "mario.png"


kuro=Kuro(pilas)

pilas.ejecutar()