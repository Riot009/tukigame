from configuracion import *
import json
import random
import os


def inicializar_pantalla(tam:tuple)->pg.Surface:
    """La Funcion inicializa la pantalla de PyGame.\n
    Se le debe pasar como parametro el tamaño de la pantalla.\n
    Retorna la superficie de la pantalla."""
    pantalla = pg.display.set_mode(tam, pg.RESIZABLE)
    return pantalla


def dibujar_boton(pantalla: pg.Surface, color_texto: tuple, _color_borde: tuple,pr_x: float, pr_y: float, pr_ancho: float, pr_alto: float,_ancho_borde: int, _borde: int, texto: str = "") -> pg.Rect:
    
    '''La funcion crea un boton con un tamaño, y texto ingresado por el usuario.\n
    se le debe pasar como parametro:\n
    La pantalla\n
    Color del texto\n
    Color del borde\n
    Posicion en x\n
    Posicion en y\n
    tamaño x\n
    tamaño y\n
    ancho del borde\n
    borde (0 para si, 1 para no)\n
    texto del boton\n
    Retorna el boton como rectangulo.'''
    
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

def dividir_texto_en_lineas(texto:str, max_caracteres:str)->str:
    '''La funcion divide el texto por linea.\n
    se le debe pasar por parametro el texto y la cantidad maxima de caracteres por linea.\n
    Retorna el texto con los salto de lineas.'''
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
    """La funcion ubica un boton en la pantalla.\n
    se le pasa como parametro:\n
    pantalla\n
    posicion del boton en x\n
    posicion del boton en y\n
    tamaño del boton en x\n
    tamaño del boton en y\n
    Devuelve el boton colocado."""
    ancho_responsive = int(pantalla.get_width() * porcentaje_ancho)
    alto_responsive = int(pantalla.get_height() * porcentaje_alto)
    x_responsive = int(pantalla.get_width() * porcentaje_x) - int(ancho_responsive / 2)
    y_responsive = int(pantalla.get_height() * porcentaje_y) - int(alto_responsive / 2)

    boton = pg.Rect(x_responsive, y_responsive, ancho_responsive, alto_responsive)
    return boton


def cargar_preguntas(ruta_archivo: str, cantidad: int = 10) -> list:
    '''La funcion lee el archivo de preguntas y las carga al juego.\n
    se le pasa como parametro la ruta del archivo y la cantidad de preguntas a cargar(de forma aleatoria.).\n
    Devuelve una lista con las preguntas.'''
    with open(ruta_archivo, "r") as archivo:
        todas = json.load(archivo)

    indices_usados = []
    preguntas_formateadas = []

    while len(preguntas_formateadas) < cantidad:
        i = random.randint(0, len(todas) - 1)
        if i not in indices_usados:
            indices_usados.append(i)
            p = todas[i]

            respuestas = [p["r_1"], p["r_2"], p["r_3"], p["r_4"]]

            # Mezclar sin usar shuffle
            respuestas_reordenadas = []
            indices = []
            while len(indices) < 4:
                r = random.randint(0, 3)
                if r not in indices:
                    indices.append(r)
                    respuestas_reordenadas.append(respuestas[r])

            preguntas_formateadas.append({
                "pregunta": p["pregunta"],
                "respuestas": respuestas_reordenadas,
                "correcta": p["correcta"]
            })

    return preguntas_formateadas


def calcular_puntaje(puntaje:int,segundo_puntaje:int)->int:
    '''La funcion calcula el bonus de puntaje.\n
    se le debe pasar por parametro el puntaje, y la cantidad de tiempo que tardo en contestar la pregunta.\n
    Retorna un int.'''

    if segundo_puntaje <= 20:
        puntaje += 3 
    else:
        puntaje = puntaje
    return puntaje

def rescalar_imagen(imagen:pg.image, pantalla:pg.surface)->pg.image:
    '''La funcion rescala imagenes al tamaño actual de la pantalla.\n
    se le debe pasar como parametro la imagen a rescalar y la pantalla.\n
    retorna la imagen ya rescalada.'''
    imagen_rescalada = pg.transform.scale(imagen,(pantalla.get_width(), pantalla.get_height()))
    return imagen_rescalada
      
def lista_a_string(lista:list,sep:str)->str:
    """
    Convierte una lista en un string, permitiendo elegir el separador.\n
    se le debe pasar la lista a convertir y el seperador a usar.\n
    Retorna los elementos de la lista como str.
    """
    resultado = ""
    for i in range(len(lista)):
        resultado += str(lista[i])
        if i < len(lista) - 1:
            resultado += sep
    return resultado


def reproducir_sonido(sonido:pg.mixer.Sound , volumen: int , loops:int )->None:
    '''La funcion carga y reproduce sonidos.\n
    se le debe pasar como parametros la ruta del sonido, el volumen deseado, y la cantidad de veces que se reproduce el sonido(-1 para que sea infinito.)\n
    No posee retorno.'''
    pg.mixer_music.load(sonido)
    pg.mixer_music.set_volume(volumen)
    pg.mixer_music.play(loops)

def dividir_pregunta_en_lineas(texto:str, palabras_por_linea:str=11):
    '''La funcion divide el texto de las preguntar con saltos de linea.\n
    se le pasar como parametro la pregunta y la cantidad de palabras que se desean por linea.\n
    retorna la pregunta con los saltos de linea.'''
    palabras = texto.split()
    if len(palabras) > palabras_por_linea:
        lineas = []
        for i in range(0, len(palabras), palabras_por_linea):
            linea = " ".join(palabras[i:i+palabras_por_linea])
            lineas.append(linea)
        return "\n".join(lineas)
    else:
        return texto
    

def calcular_porcentaje(preguntas_correctas:int)->int:
    '''la funcion calcula el porcentaje de respuestas correctas sobre el total de preguntas.\n
    se le debe pasar como parametro la cantidad de preguntas correctas.\n
    Retorna un int.'''
    porcentaje_correctas = 0
    porcentaje_correctas = (preguntas_correctas * 100) // 10
    return porcentaje_correctas


def guardar_jugador_csv(respuestas_correctas,nombre:str, puntos:int, timer:str, ruta:str=RUTA_PUNTAJES):
    """
    Guarda o actualiza jugador en un csv de 10 mejores. Si existe, reemplaza sólo si el nuevo puntaje es mejor.
    Args:
        nombre(str): Nombre del jugador.
        puntos(int): Cantidad de puntos.
        tiempo(str): Tiempo jugado.
        ruta(str): Ruta del CSV por Defaul Ruta del CSV del juego.
    Returns:
    """
    porcentaje = calcular_porcentaje(respuestas_correctas)
    if not nombre.strip():
        pass

    # Leer existentes
    jugadores = []
    try:
        with open(ruta, "r") as archivo:
            for linea in archivo:
                datos = linea.strip().split(",")
                if len(datos) == 4:
                    jugadores.append({"nombre": datos[0], "puntos": int(datos[1]), "tiempo": datos[2], "porcentaje":datos[3]})
    except FileNotFoundError:
        print("Archivo no encontrado. Se creará nuevo.")

    # Reemplazo o agregado
    reemplazado = False
    for j in jugadores:
        if j["nombre"].lower() == nombre.lower():
            if puntos > j["puntos"]:
                print(f"Reemplazando puntaje de {nombre} por mayor puntaje")
                j["puntos"] = puntos
                j["tiempo"] = timer
                j["porcentaje"] = porcentaje
            else:
                print(f"Puntaje de {nombre} no supera el anterior")
            reemplazado = True
            break

    if not reemplazado:
        print(f"Agregando nuevo jugador: {nombre}")
        jugadores.append({"nombre": nombre, "puntos": puntos, "tiempo": timer,"porcentaje":porcentaje})

    # Ordenar
    jugadores.sort(key=lambda x: x["puntos"], reverse=True)
    jugadores = jugadores[:10]

    # Guardar
    try:
        with open(ruta, "w", encoding="utf-8") as archivo:
            for j in jugadores:
                linea = f"{j['nombre']},{j['puntos']},{j['tiempo']},{j['porcentaje']}\n"
                archivo.write(linea)
        print("Archivo guardado exitosamente.")
    except Exception as e:
        print(f"No se pudo escribir el archivo: {e}")

def leer_top_puntajes(preguntas_correctas,preguntas,ruta_csv=RUTA_PUNTAJES, top=10):
    '''La funcion lee el archivo de puntajes y extrae los 10 primeros jugadores.\n
    se le pasa como parametro la ruta al archivo y la cantidad de jugadores a extraer.\n
    Retorna una lista.'''
    puntajes = []
    
    with open(ruta_csv, "r", encoding="utf-8") as archivo:
        # encabezado = archivo.readline()
        
        for linea in archivo:
            partes = linea.strip().split(",")
            if len(partes) == 4:
                nombre = partes[0]
                tiempo = partes[2]
                porcentaje = partes[3]
                try:
                    puntaje = int(partes[1])
                except:
                    puntaje = 0
                puntajes.append({"Nombre": nombre,"Tiempo total": tiempo,"Puntaje": puntaje,"porcentaje": porcentaje})
    # Ordenar por puntaje descendente
    for i in range(len(puntajes)):
        for j in range(i+1, len(puntajes)):
            if puntajes[j]["Puntaje"] > puntajes[i]["Puntaje"]:
                temp = puntajes[i]
                puntajes[i] = puntajes[j]
                puntajes[j] = temp
    return puntajes[:top]

    
def comodin_ocultar(opciones:list, respuesta_correcta:list)->list:
    '''La funcion oculta dos respuesta incorrectas.\n
    se le debe pasar como parametro las respuestas, y la respuesta correcta.\n
    Retorna una lista.'''
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


def preguntas_sin_usar(todas, seleccionadas:dict)->list:
    '''La funcion descubre cuales preguntas quedaron sin usar.\n
    se le pasa como parametro la lista con todas las preguntas y la lista con las preguntas ya utilizadas.\n
    retorna una lista.'''
    sin_usar = []
    for i in todas:
        pregunta_usada = False
        for j in seleccionadas:
            if i["pregunta"] == j["pregunta"]:
                pregunta_usada = True
        if pregunta_usada == False:
            sin_usar.append(i)

    return sin_usar


def cambiar_pregunta(todas, preguntas:list, pregunta_actual:list)->None:
    '''La funcion cambia la pregunta actual.\n
    se le debe pasar como parametro: la lista de todas las preguntas, la lista de preguntas seleccionadas para el juego, y la pregunta actual.\n
    No retorna'''
    sin_usar = preguntas_sin_usar(todas, preguntas)

    nueva_pregunta = sin_usar[random.randint(0, len(sin_usar) - 1)]

    
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


def dibujar_encabezados(pantalla:pg.surface, encabezados:list, x_base:int, y:int, ancho_col:int, alto_fila:int)->None:
    '''la funcion dibuja encabezados.\n
    se le pasa como parametro: pantalla, el encabezado a dibujar, la posicion en "x" y en "y", el ancho de las columnas y el alto de las filas\n
    No retorna.'''
    for i, texto in enumerate(encabezados):
        x_rel = x_base / pantalla.get_width() + (i + 0.5) * ancho_col
        dibujar_boton(pantalla, COLOR_BLANCO, COLOR_FONDO, x_rel, y, ancho_col, alto_fila, 0, 0, texto)

def dibujar_filas(pantalla:pg.surface, filas:list, x_base:int, y_base:int, ancho_col:int, alto_fila:int)->None:
    '''la funcion dibuja filas.\n
    se le debe pasar como parametro: pantalla, cantidad de filas, posicion en x, posicion en y, ancho de columna, alto de fila\n
    No retorna.'''
    for idx, fila in enumerate(filas):
        datos = [fila["Nombre"], str(fila["Puntaje"]), fila["Tiempo total"], fila["porcentaje"]]
        y_rel = (y_base + idx * alto_fila + alto_fila / 2) / pantalla.get_height()
        for i, texto in enumerate(datos):
            x_rel = x_base / pantalla.get_width() + (i + 0.5) * ancho_col
            dibujar_boton(pantalla, COLOR_BLANCO, COLOR_FONDO, x_rel, y_rel, ancho_col, alto_fila, 0, 0, texto)