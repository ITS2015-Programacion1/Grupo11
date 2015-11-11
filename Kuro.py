# coding: utf-8
import pilasengine
from compo import SaltarUnaVez

class KuroPP(pilasengine.actores.Actor):
    def iniciar(self):
        self.imagen = "data/Kuro/mario.png"
        self.figura=self.pilas.fisica.Rectangulo(self.x, self.y, 20, 33, friccion=0,restitucion=0)
        self.figura.sin_rotacion=True
        self.salta
    def actualizar(self):
        velocidad = 10
        salto = 15
        self.x = self.figura.x
        self.y = self.figura.y


        if self.esta_pisando_el_suelo():
            if self.pilas.control.arriba:
                self.figura.impulsar(0, salto)

        self.sensor_pies.x = self.x
        self.sensor_pies.y = self.y - 20
        
    def esta_pisando_el_suelo(self):
        return len(self.sensor_pies.figuras_en_contacto) > 0