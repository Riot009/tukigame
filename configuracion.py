import pygame as pg
import random as r


COLOR_FONDO = (37, 100, 207)
COLOR_BLANCO = (255,255,255)
COLOR_VERDE = (0, 200, 0)
COLOR_ROJO = (200, 0, 0)
TITULO_JUEGO = "TUKI QUEST"
RESOLUCION = (800,600)
RUTA_FUENTE = "recursos/font.ttf"

#RUTA_IMAGEN_BLANCO =
RUTA_IMAGEN = "recursos\pantalla de inicio.png"
RUTA_IMAGEN_JUGAR = "recursos\pantalla jugar.png"
RUTA_IMAGEN_CORRECTO = "recursos\lampara_800x600 encendida.png"
RUTA_IMAGEN_INCORRECTO = "recursos\lampara_800x600_roj.png"
RUTA_IMAGEN_PUNTAJE = "recursos\homero.jpg"

pg.display.set_caption(TITULO_JUEGO)
icono = pg.image.load("recursos/icono.jpg")

pg.display.set_icon(icono)

imagen_fondo = pg.image.load(RUTA_IMAGEN)
imagen_jugar = pg.image.load(RUTA_IMAGEN_JUGAR)
imagen_correcto = pg.image.load(RUTA_IMAGEN_CORRECTO)
imagen_incorrecto = pg.image.load(RUTA_IMAGEN_INCORRECTO)
imagen_puntaje = pg.image.load(RUTA_IMAGEN_PUNTAJE)

