from configuracion import *
import json
import random


def inicializar_pantalla(tam:tuple)->pg.Surface:
    """D"""
    pantalla = pg.display.set_mode(tam, pg.RESIZABLE)
    return pantalla


def dibujar_boton(pantalla: pg.Surface, color_texto: tuple, _color_borde: tuple,
                  pr_x: float, pr_y: float, pr_ancho: float, pr_alto: float,
                  _ancho_borde: int, _borde: int, texto: str = "") -> pg.Rect:
    
    rect = ubicar_boton(pantalla, pr_x, pr_y, pr_ancho, pr_alto)

    tamaño_fuente_max = 35
    tamaño_fuente = tamaño_fuente_max

    fuente = pg.font.Font(RUTA_FUENTE, tamaño_fuente)

    lineas = texto.split("\n")
    texto_render = []

    for linea in lineas:
        render = fuente.render(linea, True, color_texto)
        texto_render.append(render)

    while True:
        ancho_max = 0
        alto_total = 0
        for render in texto_render:
            ancho = render.get_width()
            alto = render.get_height()

            if ancho > ancho_max:
                ancho_max = ancho
            alto_total += alto

        if (ancho_max > rect.width * 0.95 or alto_total > rect.height * 0.95) and tamaño_fuente > 10:
            tamaño_fuente -= 1
            fuente = pg.font.Font(RUTA_FUENTE, tamaño_fuente)
            texto_render = []
            for linea in lineas:
                render = fuente.render(linea, True, color_texto)
                texto_render.append(render)
        else:
            break

    suma_altos = 0
    for render in texto_render:
        suma_altos += render.get_height()
    y_inicial = rect.centery - (suma_altos // 2)

    for render in texto_render:
        texto_rect = render.get_rect(center=(rect.centerx, y_inicial))
        pantalla.blit(render, texto_rect)
        y_inicial += render.get_height()

    return rect

def dividir_texto_en_lineas(texto, max_caracteres):
    lineas = []
    linea = ""
    palabras = texto.split()

    for palabra in palabras:
        if len(linea) + len(palabra) + 1 <= max_caracteres:
            if linea == "":
                linea = palabra
            else:
                linea = linea + " " + palabra
        else:
            lineas.append(linea)
            linea = palabra

    lineas.append(linea)
    return "\n".join(lineas)

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

  

    