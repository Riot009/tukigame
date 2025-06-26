import pygame as pg
import random as r


COLOR_FONDO = (37, 100, 207)
COLOR_BLANCO = (255,255,255)
TITULO_JUEGO = "TUKI QUEST"
RESOLUCION = (800,600)


#RUTA_IMAGEN_BLANCO =
RUTA_IMAGEN = "recursos\pantalla de inicio.png"
RUTA_IMAGEN_JUGAR = "recursos\pantalla jugar.png"
RUTA_IMAGEN_PUNTAJE = "recursos\homero.jpg"

pg.display.set_caption(TITULO_JUEGO)
icono = pg.image.load("recursos/icono.jpg")

pg.display.set_icon(icono)

imagen_fondo = pg.image.load(RUTA_IMAGEN)
imagen_jugar = pg.image.load(RUTA_IMAGEN_JUGAR)
imagen_puntaje = pg.image.load(RUTA_IMAGEN_PUNTAJE)

