#! /usr/bin/env python
# -*- coding: utf-8 -*-
import pilasengine

class SaltarUnaVez(pilasengine.comportamientos.Comportamiento):
    """Realiza un salto, cambiando los atributos 'y'."""
    def iniciar(self, receptor, velocidad_inicial=10, cuando_termina=None):
        """Se invoca cuando se anexa el comportamiento a un actor.
        :param receptor: El actor que comenzará a ejecutar este comportamiento.
        """
        super(SaltarUnaVez, self).iniciar(receptor)
        self.velocidad_inicial = velocidad_inicial
        self.cuando_termina = cuando_termina
        self.suelo = int(self.receptor.y)
        self.velocidad = self.velocidad_inicial
        self.velocidad_aux = self.velocidad_inicial
        self.receptor.saltando = True

    def actualizar(self):
        self.receptor.y += self.velocidad
        self.velocidad -= 0.3
        if self.receptor.y <= self.suelo:
            self.velocidad_aux /= 3.5
            self.velocidad = self.velocidad_aux
            if self.velocidad_aux <= 1:
                # Si toca el suelo
                self.receptor.y = self.suelo
                if self.cuando_termina:
                    self.cuando_termina()
                self.receptor.saltando = False
                return True