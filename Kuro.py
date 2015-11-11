# coding: utf-8
import pilasengine
from compo import SaltarUnaVez

class KuroPP(pilasengine.actores.Actor):
    def iniciar(self):
        self.imagen = "data/Kuro/mario.png"
        self.pilasengine.iniciar().comportamientos.vincular(SaltarUnaVez)

    def actualizar(self):
        if pilas.control.izquierda:
            print "hola"