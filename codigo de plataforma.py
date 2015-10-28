# coding: utf-8
import pilasengine

pilas = pilasengine.iniciar()
pilas.fisica.definir_gravedad(0,0)
actor=pilas.actores.Calvo()
fondo= pilas.fondos.Fondo("data/plataforma.png")
rectangulo=pilas.fisica.Rectangulo(-170.0,18.0,355,30,dinamica=False)
rectangulo=pilas.fisica.Rectangulo(264.0,15.8,100,30,dinamica=False)
rectangulo=pilas.fisica.Rectangulo(181.3,-108.7,325,25,dinamica=False)
rectangulo=pilas.fisica.Rectangulo(-4.0,137.2,155,25,dinamica=False)
rectangulo=pilas.fisica.Rectangulo(231.8,190.8,180,25,dinamica=False)
pilas.ejecutar()
