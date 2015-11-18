# coding: utf-8
import pilasengine

class KuroPP(pilasengine.actores.Actor):
    def iniciar(self,x=0,y=0):
        self.imagen = "data/Kuro/mario.png"
        self.figura=self.pilas.fisica.Rectangulo(self.x, self.y, 20, 33, friccion=0,restitucion=0)
        self.figura.sin_rotacion=True
        self.sensor_pies = self.pilas.fisica.Rectangulo(self.x, self.y, 10, 5, sensor=True, dinamica=False)
        self.x=x
        self.y=y
    def actualizar(self):
        velocidad = 10
        salto = 2
        self.x = self.figura.x
        self.y = self.figura.y

        if self.x>=1273:
            self.pilas.camara.x=1273
        elif self.x<=-1273:
            self.pilas.camara.x=-1273
        else:
            self.pilas.camara.x=self.x
            
        if self.pilas.control.derecha:
            self.figura.x += velocidad
        elif self.pilas.control.izquierda:
            self.figura.x -= velocidad
        else:
            self.figura.velocidad_x = 0

        if self.esta_pisando_el_suelo():
            if self.pilas.control.arriba:
                self.figura.impulsar(0, salto)

        self.sensor_pies.x = self.x
        self.sensor_pies.y = self.y - 20
        
    def esta_pisando_el_suelo(self):
        return len(self.sensor_pies.figuras_en_contacto) > 0