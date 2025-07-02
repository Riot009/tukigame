from funciones import *
import pygame as pg

pg.init()


'''Banderas Sonidos.'''
sonido_ganaste = False
sonido_perdiste = False
musica_juego_pausada = False
musica_juego_iniciada = False 
musica_principal_iniciada = False
sonido_shrek = False

'''Banderas Pantallas.'''
pantalla_principal = True
pantalla_jugar = False
pantalla_puntaje = False
pantalla_opciones = False
pantalla_version = False
pantalla_ganaste = False
pantalla_perdiste = False
mostrar_fondo_correcto = False
mostrar_fondo_incorrecto = False




preguntas = []
pregunta_actual = 0
respuesta_correcta = ""
opciones = []
boton_respuesta = []
seleccionada = None #variables par
mostrar_resultado = False
tiempo_espera = 0
tiempo_inicio = None
resolucion = (800,600)
indice_resolucion = 0
texto_resolucion = lista_a_string(resolucion)
contador_volumen = 10
incorrectas = 0
puntaje = 0
tiempos_respuesta = []
respuestas_correctas = []
opciones_ocultas = []
comodin_usado = False
tiempo_total = None
archivo = open("datos.json", "r")
todas = json.load(archivo)
archivo.close()
preguntas_correctas = 0
preguntas_incorrectas = 0
volumen = 1


pantalla = inicializar_pantalla(resolucion)

nombre_jugador = ""
ingresando_nombre = False
#input_box = pg.Rect(pantalla.get_width() * 0.35, pantalla.get_height() * 0.45, 250, 50)
color_inactivo = (200, 200, 200)
color_activo = (255, 255, 255)
color = color_inactivo
activo = False
texto_input = ""

while True:
    '''Pantalla principal.'''
    if pantalla_principal == True:       
        for evento in pg.event.get():
            if evento.type == pg.QUIT:
                pg.quit()
                quit()
            
            if not musica_principal_iniciada:
                reproducir_sonido(RUTA_SONIDO_PRINCIPAL, volumen, -1)
                musica_principal_iniciada = True
                musica_juego_iniciada = False

            if evento.type == pg.MOUSEBUTTONDOWN: 
                mouse_pos = evento.pos
                if boton_jugar.collidepoint(mouse_pos):
                    ingresando_nombre = True
                    texto_input = ""                  


                if boton_puntaje.collidepoint(mouse_pos):
                    pantalla_principal = False
                    pantalla_puntaje = True
                
                if boton_opciones.collidepoint(mouse_pos):
                    pantalla_principal = False
                    pantalla_opciones = True

                if boton_mute.collidepoint(mouse_pos):
                    if not musica_juego_pausada:
                        pg.mixer.music.pause()
                        musica_juego_pausada = True
                    else:
                        pg.mixer.music.unpause()
                        musica_juego_pausada = False

                if boton_salir.collidepoint(mouse_pos):
                    pg.quit()
                    quit()

            
        #pantalla
        pantalla.fill(COLOR_FONDO)
        pantalla.blit(rescalar_imagen(imagen_fondo, pantalla), (0,0))
        
        #botones
        titulo = dibujar_boton(pantalla, COLOR_BLANCO,COLOR_FONDO, 0.50, 0.15, 0.6, 0.6, 0, 0, TITULO_JUEGO)
        boton_jugar = dibujar_boton(pantalla, COLOR_BLANCO,COLOR_FONDO, 0.50, 0.35, 0.1, 0.1, 0, 0, "Jugar")
        boton_puntaje = dibujar_boton(pantalla, COLOR_BLANCO,COLOR_FONDO, 0.50, 0.55, 0.1, 0.1, 0, 0, "Puntaje")
        boton_opciones = dibujar_boton(pantalla, COLOR_BLANCO,COLOR_FONDO, 0.50, 0.75, 0.1, 0.1, 0, 0, "Opciones")
        boton_salir = dibujar_boton(pantalla, COLOR_BLANCO,COLOR_FONDO, 0.50, 0.95, 0.1, 0.1, 0, 0, "Salir")
        boton_mute = dibujar_boton(pantalla, COLOR_BLANCO, COLOR_FONDO, 0.94, 0.08, 0.09, 0.09, 0, 0, "Mute")


    '''Pantalla Jugar.'''
    if pantalla_jugar == True:
        for evento in pg.event.get():
            if evento.type == pg.QUIT:
                pg.quit()
                quit()

            if evento.type == pg.MOUSEBUTTONDOWN:
                mouse_pos = evento.pos

                if boton_atras.collidepoint(mouse_pos):
                    pantalla_principal = True
                    pantalla_jugar = False
                    pg.mixer_music.stop()                   
                    musica_juego_pausada = True
                    musica_juego_iniciada = False
                    musica_principal_iniciada = False
                    comodin_usado = False
                    preguntas_incorrectas = 0
                    preguntas_correctas = 0
                    puntaje = 0
                    tiempos_respuesta.clear()
                    respuestas_correctas.clear()
                    preguntas.clear()
                    pregunta_actual = 0
                    seleccionada = None
                    mostrar_resultado = False
                    mostrar_fondo_correcto = False
                    mostrar_fondo_incorrecto = False

                elif not mostrar_resultado:  # Solo permite clic si no está mostrando resultado
                    for i in range(len(boton_respuesta)):
                        if boton_respuesta[i].collidepoint(mouse_pos):
                            seleccionada = opciones[i]
                            mostrar_resultado = True
                            tiempo_espera = pg.time.get_ticks()
                            pausando_tiempo = False
                            tiempo_respuesta = tiempo_espera - tiempo_inicio 
                            tiempos_respuesta.append(tiempo_respuesta)
                            es_correcta = seleccionada == respuesta_correcta
                            respuestas_correctas.append(es_correcta)
                            if seleccionada == respuesta_correcta:
                                preguntas_correctas += 1
                                mostrar_fondo_correcto = True
                                
                            else:
                                preguntas_incorrectas += 1
                                mostrar_fondo_incorrecto = True
                                

                if boton_reiniciar.collidepoint(mouse_pos):
                    puntaje = 0
                    tiempos_respuesta.clear()
                    respuestas_correctas.clear()
                    pregunta_actual = 0
                    seleccionada = None
                    mostrar_resultado = False
                    mostrar_fondo_correcto = False
                    mostrar_fondo_incorrecto = False
                    tiempo_inicio = pg.time.get_ticks()
                    tiempo_total = pg.time.get_ticks()
                    opciones_ocultas = []
                    comodin_usado = False

                if boton_mute.collidepoint(mouse_pos):
                    if not musica_juego_pausada:
                        pg.mixer.music.pause()
                        musica_juego_pausada = True
                    else:
                        pg.mixer.music.unpause()
                        musica_juego_pausada = False

                if boton_comodin1.collidepoint(mouse_pos) and not comodin_usado and not mostrar_resultado:
                    opciones_ocultas = comodin_ocultar(opciones, respuesta_correcta)
                    comodin_usado = True

                if boton_comodin2.collidepoint(mouse_pos) and not comodin_usado:
                    cambiar_pregunta(todas,preguntas, pregunta_actual)
                    comodin_usado = True
                    seleccionada = None
                    mostrar_resultado = False

            

        #pantalla       
        if mostrar_fondo_correcto:
            pantalla.blit(rescalar_imagen(imagen_correcto, pantalla), (0, 0))
        elif mostrar_fondo_incorrecto:
            pantalla.blit(rescalar_imagen(imagen_incorrecto, pantalla), (0, 0))
        else:
            pantalla.blit(rescalar_imagen(imagen_jugar, pantalla), (0, 0))

        if pregunta_actual < len(preguntas):
            pregunta_data = preguntas[pregunta_actual]
            texto_pregunta = pregunta_data["pregunta"]
            respuesta_correcta = pregunta_data["correcta"]

            opciones = []
            for op in pregunta_data["respuestas"]:
                opcion_con_salto_linea = dividir_texto_en_lineas(op, 20)
                opciones.append(opcion_con_salto_linea)

        #botones
            texto_pregunta_multilinea = dividir_pregunta_en_lineas(texto_pregunta, 11)
            pregunta = dibujar_boton(pantalla, COLOR_BLANCO, COLOR_FONDO, 0.50, 0.20, 0.4, 0.14, 0, 0, texto_pregunta_multilinea)

            boton_respuesta.clear()
            colores = [COLOR_BLANCO] * 4
            if mostrar_resultado:
                for i in range(4):
                    if opciones[i] == respuesta_correcta:
                        colores[i] = COLOR_VERDE
                    elif opciones[i] == seleccionada:
                        colores[i] = COLOR_ROJO
                        
            pos_x = [0.225, 0.775, 0.225, 0.775]
            pos_y = [0.35, 0.35, 0.61, 0.61]

            for i in range(4):
                if i not in opciones_ocultas:
                    boton = dibujar_boton(pantalla, colores[i], COLOR_FONDO, pos_x[i], pos_y[i], 0.2, 0.14, 0, 0, opciones[i])
                    boton_respuesta.append(boton)
                else:
                    boton_respuesta.append(pg.Rect(0, 0, 0, 0))

        boton_comodin1 = dibujar_boton(pantalla, COLOR_BLANCO, COLOR_FONDO, 0.175, 0.87, 0.2, 0.08, 0, 0, "50/50")
        boton_comodin2 = dibujar_boton(pantalla, COLOR_BLANCO, COLOR_FONDO, 0.50, 0.87, 0.2, 0.08, 0, 0, "Cambiar Pregunta.")
        boton_comodin3 = dibujar_boton(pantalla, COLOR_BLANCO, COLOR_FONDO, 0.825, 0.87, 0.2, 0.08, 0, 0, "Que venga el amigo!")

        boton_contador = dibujar_reloj(pantalla, tiempo_total)

        boton_atras = dibujar_boton(pantalla, COLOR_BLANCO, COLOR_FONDO, 0.06, 0.08, 0.09, 0.09, 0, 0, "<---")

        boton_mute = dibujar_boton(pantalla, COLOR_BLANCO, COLOR_FONDO, 0.94, 0.08, 0.09, 0.09, 0, 0, "mute")
        boton_reiniciar = dibujar_boton(pantalla, COLOR_BLANCO, COLOR_FONDO, 0.5, 0.95, 0.18, 0.08, 0, 0, "REINICIAR")

        puntaje = calcular_puntaje(tiempos_respuesta, respuestas_correctas)
        boton_puntaje_actual = dibujar_boton(pantalla, COLOR_BLANCO, COLOR_FONDO, 0.5, 0.05, 0.18, 0.08, 0, 0, f"Puntaje: {puntaje}")

    
    if mostrar_resultado:
        tiempo_actual = pg.time.get_ticks()
        if tiempo_actual - tiempo_espera >= 2000:  # 2 segundos
            pregunta_actual += 1
            mostrar_resultado = False
            seleccionada = None
            opciones_ocultas = []
            mostrar_fondo_correcto = False
            mostrar_fondo_incorrecto = False
            if pantalla_jugar and pregunta_actual < len(preguntas):
                tiempo_inicio = pg.time.get_ticks()

            if pregunta_actual >= len(preguntas):

                if preguntas_correctas >= 6:
                    pantalla_ganaste = True
                    pantalla_jugar = False
                    
                
                elif preguntas_incorrectas >= 4:
                    pantalla_perdiste = True
                    pantalla_jugar = False
                    

                
                # Calcular tiempo total de la partida
                tiempo_total_ms = 0
                for t in tiempos_respuesta:
                    tiempo_total_ms += t
                total_preguntas = len(preguntas)
                respuestas_bien = 0
                for r in respuestas_correctas:
                    if r:
                        respuestas_bien += 1
                puntaje = calcular_puntaje(tiempos_respuesta, respuestas_correctas)
                registrar_puntaje_csv(
                    nombre_jugador,
                    tiempo_total_ms,
                    respuestas_bien,
                    total_preguntas,
                    puntaje
                )
                pg.mixer_music.stop()
                pantalla_jugar = False
                pantalla_principal = True



    '''Pantalla Ganador.'''
    if pantalla_ganaste == True:
        for evento in pg.event.get():
            if evento.type == pg.QUIT:
                pg.quit()
                quit()
            if evento.type == pg.KEYDOWN:
                if evento.key == pg.K_RETURN or evento.key == pg.K_ESCAPE:
                    tiempos_respuesta.clear()
                    respuestas_correctas.clear()
                    preguntas.clear()
                    pregunta_actual = 0
                    seleccionada = None
                    mostrar_resultado = False
                    mostrar_fondo_correcto = False
                    mostrar_fondo_incorrecto = False
                    pantalla_ganaste = False
                    pantalla_principal = True
                    musica_principal_iniciada = False


        pantalla.fill(COLOR_FONDO)
        pantalla.blit(rescalar_imagen(imagen_fondo,pantalla), (0,0))        
        if not sonido_ganaste:
            reproducir_sonido(RUTA_SONIDO_GANAR, volumen, 1)
            sonido_ganaste = True
    
        boton_ganaste = dibujar_boton(pantalla, COLOR_BLANCO,COLOR_FONDO, 0.50, 0.15, 0.30, 0.30, 0, 0, 'Ganaste!')

        top_puntajes = leer_top_puntajes()
        margen_izquierdo = pantalla.get_width() * 0.10
        posicion_inicial_y = pantalla.get_height() * 0.35
        ancho_tabla = pantalla.get_width() * 0.80
        alto_fila = pantalla.get_height() * 0.06

        # Encabezados
        encabezados = ["Nombre", "Tiempo", "% Correctas", "Puntaje"]
        dibujar_encabezados(pantalla, encabezados, margen_izquierdo, 0.25, 0.18, alto_fila)

        # Filas de puntajes
        dibujar_filas(pantalla, top_puntajes, margen_izquierdo, posicion_inicial_y, 0.18, alto_fila)


    

    '''Pantalla Perdedor.'''
    if pantalla_perdiste == True:
        for evento in pg.event.get():
            if evento.type == pg.QUIT:
                pg.quit()
                quit()
            if evento.key == pg.K_RETURN or evento.key == pg.K_ESCAPE:
                tiempos_respuesta.clear()
                respuestas_correctas.clear()
                preguntas.clear()
                pregunta_actual = 0
                seleccionada = None
                mostrar_resultado = False
                mostrar_fondo_correcto = False
                mostrar_fondo_incorrecto = False
                pantalla_ganaste = False
                pantalla_principal = True
                musica_principal_iniciada = False

        pantalla.fill(COLOR_FONDO)
        pantalla.blit(rescalar_imagen(imagen_fondo,pantalla), (0,0))        
        if not sonido_perdiste:
            reproducir_sonido(RUTA_SONIDO_PERDER, volumen, 1)
            sonido_perdiste = True
    
        boton_atras = dibujar_boton(pantalla, COLOR_BLANCO, COLOR_FONDO, 0.06, 0.08, 0.09, 0.09, 0, 0, "<---")
        boton_perdiste = dibujar_boton(pantalla, COLOR_BLANCO,COLOR_FONDO, 0.50, 0.15, 0.30, 0.30, 0, 0, 'perdiste!')

        top_puntajes = leer_top_puntajes()
        margen_izquierdo = pantalla.get_width() * 0.10
        posicion_inicial_y = pantalla.get_height() * 0.35
        ancho_tabla = pantalla.get_width() * 0.80
        alto_fila = pantalla.get_height() * 0.06

        # Encabezados
        encabezados = ["Nombre", "Tiempo", "% Correctas", "Puntaje"]
        dibujar_encabezados(pantalla, encabezados, margen_izquierdo, 0.25, 0.18, alto_fila)

        # Filas de puntajes
        dibujar_filas(pantalla, top_puntajes, margen_izquierdo, posicion_inicial_y, 0.18, alto_fila)


    '''Pantalla Puntajes.'''
    if pantalla_puntaje == True:
        for evento in pg.event.get():
            if evento.type == pg.QUIT:
                pg.quit()
                quit()
            if evento.type == pg.MOUSEBUTTONDOWN:
                mouse_pos = evento.pos
                if boton_volver.collidepoint(mouse_pos):
                    pantalla_puntaje = False
                    pantalla_principal = True

        pantalla.blit(rescalar_imagen(imagen_fondo,pantalla), (0,0))

        top_puntajes = leer_top_puntajes()
        margen_izquierdo = pantalla.get_width() * 0.10
        posicion_inicial_y = pantalla.get_height() * 0.25
        ancho_tabla = pantalla.get_width() * 0.80
        alto_fila = pantalla.get_height() * 0.06

        # Encabezados
        encabezados = ["Nombre", "Tiempo", "% Correctas", "Puntaje"]
        dibujar_encabezados(pantalla, encabezados, margen_izquierdo, 0.18, 0.18, alto_fila)

        # Filas de puntajes
        dibujar_filas(pantalla, top_puntajes, margen_izquierdo, posicion_inicial_y, 0.18, alto_fila)

        # Botón para volver
        boton_volver = dibujar_boton(
            pantalla, COLOR_BLANCO, COLOR_FONDO, 0.5, 0.93, 0.18, 0.08, 0, 0, "VOLVER"
        )

    '''Pantalla Opciones.'''
    if pantalla_opciones == True:
        for evento in pg.event.get():
            if evento.type == pg.QUIT:
                pg.quit()
                quit()

            if evento.type == pg.MOUSEBUTTONDOWN:
                mouse_pos = evento.pos

                if boton_resolucion.collidepoint(mouse_pos):
                    indice_resolucion +=1
                    if indice_resolucion > 2:
                        indice_resolucion = 0
                    resolucion = LISTA_RESOLUCIONES[indice_resolucion]
                    pantalla = inicializar_pantalla(resolucion)
                    texto_resolucion = lista_a_string(resolucion)

                if boton_atras.collidepoint(mouse_pos):
                    pantalla_principal = True
                    pantalla_opciones = False

                if boton_mute.collidepoint(mouse_pos):
                    if not musica_juego_pausada:
                        pg.mixer.music.pause()
                        musica_juego_pausada = True
                    else:
                        pg.mixer.music.unpause()
                        musica_juego_pausada = False
                
                if boton_volumen.collidepoint(mouse_pos):
                    contador_volumen += 1
                    if contador_volumen > 10:
                        contador_volumen = 0
                    volumen = VOLUMENES[contador_volumen]
                    pg.mixer_music.set_volume(volumen)

                if boton_version.collidepoint(mouse_pos):
                    pantalla_version = True
                    reproducir_sonido(RUTA_SONIDO_LALA,1,1)
                    


        #pantalla
        pantalla.fill(COLOR_FONDO) # color fondo
        pantalla.blit(rescalar_imagen(imagen_fondo, pantalla), (0,0))
            
        #botones
        boton_resolucion = dibujar_boton(pantalla, COLOR_BLANCO,COLOR_FONDO, 0.50, 0.35, 0.3, 0.3, 0, 0, f"Resolucion: {texto_resolucion}")
        boton_volumen = dibujar_boton(pantalla, COLOR_BLANCO,COLOR_FONDO, 0.50, 0.65, 0.3, 0.3, 0, 0, f"Volumen: {contador_volumen}")
        boton_atras = dibujar_boton(pantalla, COLOR_BLANCO, COLOR_FONDO, 0.06, 0.08, 0.09, 0.09, 0, 0, "<---")
        boton_mute = dibujar_boton(pantalla, COLOR_BLANCO, COLOR_FONDO, 0.94, 0.08, 0.09, 0.09, 0, 0, "mute")
        boton_version = dibujar_boton(pantalla, COLOR_BLANCO, COLOR_FONDO, 0.90, 0.90, 0.09, 0.09, 0, 0, "Version:0.01")


    if pantalla_version == True:
        for evento in pg.event.get():
            if evento.type == pg.QUIT:
                pg.quit()
                quit()

            if evento.type == pg.MOUSEBUTTONDOWN:
                mouse_pos = evento.pos

                if boton_atras.collidepoint(mouse_pos):
                    pantalla_opciones = True
                    pantalla_version = False
                    pg.mixer_music.stop()
        


        pantalla.fill(COLOR_FONDO)
        pantalla.blit(rescalar_imagen(imagen_version,pantalla), (0,0))

        boton_atras = dibujar_boton(pantalla, COLOR_BLANCO, COLOR_FONDO, 0.06, 0.08, 0.09, 0.09, 0, 0, "<---")

    '''Pantalla Ingreso de nombre.'''
    if ingresando_nombre:
        '''Itera sobre los eventos del bucle.'''
        for evento in pg.event.get():
            '''Sale del juego al tocar el boton "X" de la ventana'''
            if evento.type == pg.QUIT:
                pg.quit()
                quit()

            '''Comprueba si se esta tocando algun boton del mouse.'''
            if evento.type == pg.MOUSEBUTTONDOWN:

                if input_box.collidepoint(evento.pos):
                    activo = True
                    color = color_activo
                else:
                    activo = False
                    color = color_inactivo
            
            '''Comprueba si se esta tocando alguna tecla.'''
            if evento.type == pg.KEYDOWN:
                if activo:
                    '''Cuando se toca la tecla ENTER inicia el juego.'''
                    if evento.key == pg.K_RETURN:
                        nombre_jugador = texto_input.strip()
                        if nombre_jugador != "":
                            ingresando_nombre = False
                            pantalla_principal = False
                            pantalla_jugar = True
                            preguntas = cargar_preguntas("datos.json", cantidad=10)
                            preguntas_correctas = 0
                            preguntas_incorrectas = 0
                            pregunta_actual = 0
                            opciones_ocultas = []
                            comodin_usado = False
                            pantalla_principal = False
                            pantalla_jugar = True
                            sonido_perdiste = False
                            sonido_ganaste = False
                            tiempo_inicio = pg.time.get_ticks()
                            tiempo_total = pg.time.get_ticks()                           
                            if not musica_juego_iniciada:
                                reproducir_sonido(RUTA_SONIDO_JUEGO,volumen,-1)
                                musica_juego_iniciada = True
                                musica_juego_pausada = False
                    elif evento.key == pg.K_BACKSPACE:
                        '''Al tocar la tecla borrar elimina el ultimo imput dentro de la casilla de nombre.'''
                        texto_input = texto_input[:-1]
                    else:
                        if len(texto_input) < 20:
                            texto_input += evento.unicode

        pantalla.fill(COLOR_FONDO)
        pantalla.blit(rescalar_imagen(imagen_fondo,pantalla), (0,0))
        mensaje = "Ingrese su nombre y presione Enter:"
        fuente = pg.font.Font(RUTA_FUENTE, 15)
        txt_surface = fuente.render(mensaje, True, COLOR_BLANCO)
        pantalla.blit(txt_surface, (pantalla.get_width() // 2 - txt_surface.get_width() // 2, pantalla.get_height() // 2 - 80))
        # Caja de texto
        input_box_ancho = pantalla.get_width() * 0.3
        input_box_alto = pantalla.get_height() * 0.08
        input_box_x = pantalla.get_width() * 0.5 - input_box_ancho / 2
        input_box_y = pantalla.get_height() * 0.5 - input_box_alto / 2
        input_box = pg.Rect(input_box_x, input_box_y, input_box_ancho, input_box_alto)
        pg.draw.rect(pantalla, color, input_box, 2)
        input_surface = fuente.render(texto_input, True, COLOR_BLANCO)
        pantalla.blit(input_surface, (input_box.x + 5, input_box.y + 10))
        pg.display.update()



    pg.display.update()

