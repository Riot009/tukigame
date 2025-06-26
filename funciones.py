from configuracion import *
import json 

def cargar_preguntas(archivo:str)->list:
    """Carga las preguntas desde el JSON."""
    with open(archivo, "r") as f:
        preguntas = json.load(f)
    return preguntas

def extraer_preguntas(datos)->list[str]:
    preguntas = []
    for item in datos:
        pregunta = str(item.get("pregunta", ""))
        preguntas.append(pregunta)
    return preguntas

cargar_preguntas("datos.json")
print(extraer_preguntas(cargar_preguntas("datos.json")))
# def obtener_textos_pregunta(pregunta: dict) -> tuple[str, str, str, str, str]:
#     """
#     Devuelve los textos de la pregunta y sus respuestas como tupla.
#     """
#     texto_pregunta = ""
#     respuesta1 = ""
#     respuesta2 = ""
#     respuesta3 = ""
#     respuesta4 = ""
#     if pregunta:
#         if "pregunta" in pregunta:
#             texto_pregunta = pregunta["pregunta"]
#         if "r_1" in pregunta:
#             respuesta1 = pregunta["r_1"]
#         if "r_2" in pregunta:
#             respuesta2 = pregunta["r_2"]
#         if "r_3" in pregunta:
#             respuesta3 = pregunta["r_3"]
#         if "r_4" in pregunta:
#             respuesta4 = pregunta["r_4"]
#     return texto_pregunta, respuesta1, respuesta2, respuesta3, respuesta4

# Uso:
# preguntas = cargar_preguntas("datos.json")
# textos_botones = extraer_textos_botones(preguntas)
# Luego puedes usar textos_botones['jugar'], etc. para los botones

#def crear_boton ( tx:int, ty:int, px:int, py:int, color:int):
#    pygame.draw.rect(color(px,py,tx,ty))


# #def crear_boton(surface, px: int, py: int, tx: int, ty: int, color: tuple):
#     rect = pygame.draw.rect(px, py, tx, ty)
#     ubicar_boton()

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






#def pantalla_princcipal():
        # #pantalla
        # pantalla.fill(COLOR_FONDO) # color fondo
        # pantalla.blit(imagen_fondo, (0,0))
        
        # #botones
        # titulo = dibujar_boton(pantalla, COLOR_BLANCO,COLOR_FONDO, 0.50, 0.15, 0.1, 0.1, 0, 0, "TUKIGAME")
        # boton_jugar = dibujar_boton(pantalla, COLOR_BLANCO,COLOR_FONDO, 0.50, 0.35, 0.1, 0.1, 0, 0, "JUGAR")
        # boton_puntaje = dibujar_boton(pantalla, COLOR_BLANCO,COLOR_FONDO, 0.50, 0.50, 0.1, 0.1, 0, 0, "PUNTAJE")
        # boton_opciones = dibujar_boton(pantalla, COLOR_BLANCO,COLOR_FONDO, 0.50, 0.65, 0.1, 0.1, 0, 0, "OPCIONES")
        # boton_salir = dibujar_boton(pantalla, COLOR_BLANCO,COLOR_FONDO, 0.50, 0.80, 0.1, 0.1, 0, 0, "SALIR")
    
