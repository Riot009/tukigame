from configuracion import *
import json
import random


def inicializar_pantalla(tam:tuple)->pg.Surface:
    """D"""
    pantalla = pg.display.set_mode(tam, pg.RESIZABLE)
    return pantalla

def dibujar_boton(pantalla:pg.Surface, color:tuple, color_borde: tuple, pr_x:int, pr_y:int, pr_ancho:int, pr_alto:int, ancho_borde:int, borde:int, texto:str="")->pg.Rect:
    """D"""
    rectangulo = ubicar_boton(pantalla, pr_x, pr_y, pr_ancho, pr_alto)
    boton = pg.draw.rect(pantalla, color, rectangulo, border_radius=borde)
    pg.draw.rect(pantalla, color_borde, rectangulo, ancho_borde, border_radius=borde)
    
    alto_boton = rectangulo.height
    fuente = pg.font.SysFont(None, int(alto_boton * 0.5))  # tamaño relativo
    texto_render = fuente.render(texto, True, (COLOR_BLANCO))  # color blanco

    texto_rect = texto_render.get_rect(center=rectangulo.center)
    pantalla.blit(texto_render, texto_rect)


    return boton


def ubicar_boton(pantalla:pg.Surface, porcentaje_x:int, porcentaje_y:int, porcentaje_ancho:int, porcentaje_alto:int):
    """D"""
    ancho_responsive = int(pantalla.get_width() * porcentaje_ancho)
    alto_responsive = int(pantalla.get_height() * porcentaje_alto)
    x_responsive = int(pantalla.get_width() * porcentaje_x) - int(ancho_responsive / 2)
    y_responsive = int(pantalla.get_height() * porcentaje_y) - int(alto_responsive / 2)

    boton = pg.Rect(x_responsive, y_responsive, ancho_responsive, alto_responsive)
    return boton


def cargar_preguntas(ruta_archivo:str, cantidad:int=10)->list:
    
    archivo = open(ruta_archivo, "r")
    todas = json.load(archivo)
    archivo.close()

    seleccionadas = random.sample(todas, k=cantidad)
    preguntas_formateadas = []

    

    for p in seleccionadas:
        respuestas = [p["r_1"], p["r_2"], p["r_3"], p["r_4"]]
        random.shuffle(respuestas)
        preguntas_formateadas.append({
            "pregunta": p["pregunta"],
            "respuestas": respuestas,
            "correcta": p["correcta"]
        })

    return preguntas_formateadas

  

    