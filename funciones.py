from configuracion import *
import json
import random
import os


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

def cronometro_juego()-> int:
    """D"""
    evento_tick = pg.USEREVENT + 1
    un_segundo = 1000
    pg.time.set_timer(evento_tick, un_segundo)
    return evento_tick

def dibujar_reloj(pantalla, tiempo_inicio, duracion_pausas=0):
    # Esta función puede estar fuera del bucle principal
    if tiempo_inicio is not None:
        tiempo_actual = pg.time.get_ticks()
        tiempo_transcurrido = (tiempo_actual - tiempo_inicio - duracion_pausas) // 1000  # en segundos
        minutos = tiempo_transcurrido // 60
        segundos = tiempo_transcurrido % 60
        texto_tiempo = f"{minutos:02}:{segundos:02}"
    else:
        texto_tiempo = "00:00"
    return dibujar_boton(pantalla, COLOR_BLANCO, COLOR_FONDO, 0.50, 0.75, 0.1, 0.1, 0, 0, texto_tiempo)

def rescalar_imagen(imagen, pantalla):
    imagen_rescalada = pg.transform.scale(imagen,(pantalla.get_width(), pantalla.get_height()))
    return imagen_rescalada
      
def lista_a_string(lista):
    """
    Convierte una lista en un string, separando los elementos por comas, usando solo lógica.
    """
    resultado = ""
    for i in range(len(lista)):
        resultado += str(lista[i])
        if i < len(lista) - 1:
            resultado += "x"
    return resultado


def reproducir_sonido(sonido,volumen,loops):
    pg.mixer_music.load(sonido)
    pg.mixer_music.set_volume(volumen)
    pg.mixer_music.play(loops)

def dividir_pregunta_en_lineas(texto, palabras_por_linea=11):
    palabras = texto.split()
    if len(palabras) > palabras_por_linea:
        lineas = []
        for i in range(0, len(palabras), palabras_por_linea):
            linea = " ".join(palabras[i:i+palabras_por_linea])
            lineas.append(linea)
        return "\n".join(lineas)
    else:
        return texto
    
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

def calcular_puntaje(tiempos_respuesta, respuestas_correctas):
    # 3 puntos por cada respuesta correcta en menos de 20 segundos
    puntos = 0
    for correcto, tiempo in zip(respuestas_correctas, tiempos_respuesta):
        if (correcto and tiempo >= 10000) and (correcto and tiempo <= 20000):
            puntos += 150
        elif correcto and tiempo < 10000:
            puntos += 300
        elif correcto and tiempo > 20000:
            puntos += 50

    return puntos

def registrar_puntaje_csv(nombre_jugador, tiempo_total_ms, respuestas_correctas, total_preguntas, puntaje_total, ruta_csv=RUTA_PUNTAJES):
    """
    Guarda el puntaje del jugador en un archivo CSV (sin usar el módulo csv).
    Cada fila es: Nombre,Tiempo total,Porcentaje de respuestas correctas,Puntaje total
    """
    tiempo_segundos = tiempo_total_ms // 1000
    minutos = tiempo_segundos // 60
    segundos = tiempo_segundos % 60
    tiempo_formateado = f"{minutos:02}:{segundos:02}"

    if total_preguntas > 0:
        porcentaje_correctas = round((respuestas_correctas / total_preguntas) * 100)
    else:
        porcentaje_correctas = 0

    encabezado = "Nombre,Tiempo total,Porcentaje de respuestas correctas,Puntaje total\n"
    fila = (
        str(nombre_jugador) + "," +
        str(tiempo_formateado) + "," +
        str(porcentaje_correctas) + "%," +
        str(puntaje_total) + "\n"
    )

    try:
        escribir_encabezado = False
        try:
            archivo = open(ruta_csv, "r", encoding="utf-8")
            primera_linea = archivo.readline()
            archivo.close()
            if primera_linea == "":
                escribir_encabezado = True
        except FileNotFoundError:
            escribir_encabezado = True

        archivo = open(ruta_csv, "a", encoding="utf-8")
        if escribir_encabezado:
            archivo.write(encabezado)
        archivo.write(fila)
        archivo.close()
    except Exception as e:
        print(f"Error al guardar puntaje: {e}")

def leer_top_puntajes(ruta_csv=RUTA_PUNTAJES, top=10):
    puntajes = []
    if not os.path.exists(ruta_csv):
        return puntajes
    try:
        with open(ruta_csv, "r", encoding="utf-8") as archivo:
            encabezado = archivo.readline()
            for linea in archivo:
                partes = linea.strip().split(",")
                if len(partes) == 4:
                    nombre = partes[0]
                    tiempo = partes[1]
                    porcentaje = partes[2]
                    try:
                        puntaje = int(partes[3])
                    except:
                        puntaje = 0
                    puntajes.append({
                        "Nombre": nombre,
                        "Tiempo total": tiempo,
                        "Porcentaje": porcentaje,
                        "Puntaje": puntaje
                    })
        # Ordenar por puntaje descendente
        for i in range(len(puntajes)):
            for j in range(i+1, len(puntajes)):
                if puntajes[j]["Puntaje"] > puntajes[i]["Puntaje"]:
                    temp = puntajes[i]
                    puntajes[i] = puntajes[j]
                    puntajes[j] = temp
        return puntajes[:top]
    except Exception as e:
        print(f"Error al leer puntajes: {e}")
        return []
    
def comodin_ocultar(opciones, respuesta_correcta):
    indices_incorrectos = []
    for i in range(len(opciones)):
        if opciones[i] != respuesta_correcta:
            indices_incorrectos.append(i)

    if len(indices_incorrectos) >= 2:
        i_random = random.randint(0, len(indices_incorrectos) - 1)
        indice1 = indices_incorrectos.pop(i_random)
        i_random2 = random.randint(0, len(indices_incorrectos) - 1)
        indice2 = indices_incorrectos[i_random2]
        return [indice1, indice2]
    
    return []

def preguntas_sin_usar(todas, seleccionadas)->list:
    sin_usar = []
    for i in todas:
        pregunta_usada = False
        for j in seleccionadas:
            if i["pregunta"] == j["pregunta"]:
                pregunta_usada = True
        if pregunta_usada == False:
            sin_usar.append(i)

    return sin_usar


def cambiar_pregunta(todas, preguntas, pregunta_actual):
    sin_usar = preguntas_sin_usar(todas, preguntas)

    nueva_pregunta = sin_usar[random.randint(0, len(sin_usar) - 1)]

    # Reordenar las respuestas manualmente
    respuestas = [nueva_pregunta["r_1"], nueva_pregunta["r_2"], nueva_pregunta["r_3"], nueva_pregunta["r_4"]]

    respuestas_mezcladas = []
    usados = []
    while len(respuestas_mezcladas) < 4:
        i = random.randint(0, 3)
        if i not in usados:
            respuestas_mezcladas.append(respuestas[i])
            usados.append(i)

    preguntas[pregunta_actual] = {
        "pregunta": nueva_pregunta["pregunta"],
        "respuestas": respuestas_mezcladas,
        "correcta": nueva_pregunta["correcta"]
    }


def tiempo_total(tiempo_total_ms):
    tiempo_segundos = tiempo_total_ms // 1000
    minutos = tiempo_segundos // 60
    segundos = tiempo_segundos % 60
    tiempo_formateado = f"{minutos:02}:{segundos:02}"

    return tiempo_formateado