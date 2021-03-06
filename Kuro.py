# coding: utf-8
import pilasengine

class KuroPP(pilasengine.actores.Actor):
    def iniciar(self,x=0,y=0):
        self.imagen = "data/Kuro/mario.png"
        self.figura=self.pilas.fisica.Rectangulo(self.x, self.y, 20, 33, friccion=0, restitucion=0)
        self.figura.sin_rotacion=True
        self.sensor_pies = self.pilas.fisica.Rectangulo(self.x, self.y, 10, 5, sensor=True, dinamica=False)
        self.sensor_cabeza= self.pilas.fisica.Rectangulo(self.x, self.y, 10, 5, sensor=True, dinamica=False)
        self.x=x
        self.y=y

    def actualizar(self):
        velocidad = 5
        salto = 1.5
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

        if self.esta_tocando_el_techo():
            if self.pilas.control.abajo:
                self.figura.impulsar(0, -salto)

        self.sensor_pies.x = self.x
        self.sensor_pies.y = self.y - 20

        self.sensor_cabeza.x = self.x
        self.sensor_cabeza.y = self.y + 20
        
    def esta_pisando_el_suelo(self):
        return len(self.sensor_pies.figuras_en_contacto) > 0

    def esta_tocando_el_techo(self):
        return len(self.sensor_cabeza.figuras_en_contacto) >  0

    def perder(self):
        self.figura.x=-1539
        if self.pilas.fisica.gravedad_y<0:
            self.figura.y=170
        else:
            self.figura.y=-170
