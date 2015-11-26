#! /usr/bin/env python
# -*- coding: utf-8 -*-
import pilasengine

class Ganar(pilasengine.escenas.Escena):
    def iniciar(self):
        fondo=self.pilas.fondos.Tarde()
        texto=self.pilas.actores.Texto("Ganaste")