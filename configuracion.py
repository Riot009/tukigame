import pygame as pg
import random as r


#variables juego



COLOR_FONDO = (37, 100, 207)
COLOR_BLANCO = (255,255,255)
COLOR_VERDE = (0, 200, 0)
COLOR_ROJO = (200, 0, 0)
TITULO_JUEGO = "MilloQuest"
RUTA_FUENTE = "recursos//Fuentes//font.ttf"
LISTA_RESOLUCIONES = [(800,600),(1366,768),(1600,900)]
VOLUMENES = (0,0.10,0.20,0.30,0.40,0.50,0.60,0.70,0.80,0.90,1)

#RUTA_IMAGEN_BLANCO =
RUTA_IMAGEN = "recursos\Imagenes\pantalla de inicio.png"
RUTA_IMAGEN_JUGAR = "recursos\Imagenes\pantalla jugar.png"
RUTA_IMAGEN_CORRECTO = "recursos\Imagenes\lampara_800x600 encendida.png"
RUTA_IMAGEN_INCORRECTO = "recursos\Imagenes\lampara_800x600_roj.png"
RUTA_IMAGEN_VERSION = 'recursos\Imagenes\imagen_version.webp'
RUTA_PUNTAJES = 'recursos\\puntajes.csv'

pg.display.set_caption(TITULO_JUEGO)
icono = pg.image.load("recursos//Imagenes//icono.jpg")

pg.display.set_icon(icono)

imagen_fondo = pg.image.load(RUTA_IMAGEN)
imagen_jugar = pg.image.load(RUTA_IMAGEN_JUGAR)
imagen_correcto = pg.image.load(RUTA_IMAGEN_CORRECTO)
imagen_incorrecto = pg.image.load(RUTA_IMAGEN_INCORRECTO)
imagen_version = pg.image.load(RUTA_IMAGEN_VERSION)

RUTA_SONIDO_PERDER = 'recursos\\Sonidos\\price_is_right_lh.mp3'
RUTA_SONIDO_JUEGO = 'recursos\\Sonidos\\elevator.mp3'
RUTA_SONIDO_PRINCIPAL = 'recursos\\Sonidos\\musica_principal.mp3'
RUTA_SONIDO_LALA = 'recursos\\Sonidos\\click.mp3'
RUTA_SONIDO_GANAR = 'recursos\\Sonidos\\roblox_winning_sound.mp3'
RUTA_SONIDO_SHREK = 'recursos\\Sonidos\\latres_latres.mp3'