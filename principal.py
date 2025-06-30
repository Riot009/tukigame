from funciones import *
import pygame as pg

pg.init()
pantalla = inicializar_pantalla(RESOLUCION)

musica_pausada = False
musica_iniciada = False 

pantalla_principal = True
pantalla_jugar = False
pantalla_puntaje = False
mostrar_fondo_correcto = False
mostrar_fondo_incorrecto = False


preguntas = []
pregunta_actual = 0
respuesta_correcta = ""
opciones = []
boton_respuesta = []
seleccionada = None
mostrar_resultado = False
tiempo_espera = 0

while True:
    if pantalla_principal == True:
        for evento in pg.event.get():
            if evento.type == pg.QUIT:
                pg.quit()
                quit()
            if evento.type == pg.MOUSEBUTTONDOWN:
                mouse_pos = evento.pos
                if boton_jugar.collidepoint(mouse_pos):
                    preguntas = cargar_preguntas("datos.json", cantidad=10)
                    pregunta_actual = 0
                    pantalla_principal = False
                    pantalla_jugar = True
                    if not musica_iniciada:
                        pg.mixer.music.load("recursos\\elevator.mp3")
                        pg.mixer.music.set_volume(1)
                        pg.mixer.music.play(-1)
                        musica_iniciada = True
                        musica_pausada = False

                if boton_puntaje.collidepoint(mouse_pos):
                    pantalla_principal = False
                    pantalla_puntaje = True

                if boton_salir.collidepoint(mouse_pos):
                    pg.quit()
                    quit()

            
        #pantalla
        pantalla.fill(COLOR_FONDO) # color fondo
        pantalla.blit(imagen_fondo, (0,0))
        
        #botones
        titulo = dibujar_boton(pantalla, COLOR_BLANCO,COLOR_FONDO, 0.50, 0.15, 0.1, 0.1, 0, 0, "TITULO")
        boton_jugar = dibujar_boton(pantalla, COLOR_BLANCO,COLOR_FONDO, 0.50, 0.35, 0.1, 0.1, 0, 0, "JUGAR")
        boton_puntaje = dibujar_boton(pantalla, COLOR_BLANCO,COLOR_FONDO, 0.50, 0.50, 0.1, 0.1, 0, 0, "PUNTAJE")
        boton_opciones = dibujar_boton(pantalla, COLOR_BLANCO,COLOR_FONDO, 0.50, 0.65, 0.1, 0.1, 0, 0, "OPCIONES")
        boton_salir = dibujar_boton(pantalla, COLOR_BLANCO,COLOR_FONDO, 0.50, 0.80, 0.1, 0.1, 0, 0, "SALIR")

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

                elif not mostrar_resultado:  # Solo permite clic si no está mostrando resultado
                    for i in range(len(boton_respuesta)):
                        if boton_respuesta[i].collidepoint(mouse_pos):
                            seleccionada = opciones[i]
                            mostrar_resultado = True
                            tiempo_espera = pg.time.get_ticks()
                            if seleccionada == respuesta_correcta:
                                mostrar_fondo_correcto = True
                            else:
                                mostrar_fondo_incorrecto = True

                if boton_mute.collidepoint(mouse_pos):
                    if not musica_pausada:
                        pg.mixer.music.pause()
                        musica_pausada = True
                    else:
                        pg.mixer.music.unpause()
                        musica_pausada = False


            

        #pantalla       
        if mostrar_fondo_correcto:
            pantalla.blit(imagen_correcto, (0, 0))
        elif mostrar_fondo_incorrecto:
            pantalla.blit(imagen_incorrecto, (0, 0))
        else:
            pantalla.blit(imagen_jugar, (0, 0))

        if pregunta_actual < len(preguntas):
            pregunta_data = preguntas[pregunta_actual]
            texto_pregunta = pregunta_data["pregunta"]
            respuesta_correcta = pregunta_data["correcta"]

            opciones = []
            for op in pregunta_data["respuestas"]:
                opcion_con_salto_linea = dividir_texto_en_lineas(op, 20)
                opciones.append(opcion_con_salto_linea)

        #botones

            pregunta = dibujar_boton(pantalla, COLOR_BLANCO, COLOR_FONDO, 0.50, 0.20, 0.4, 0.14, 0, 0, texto_pregunta)

            boton_respuesta.clear()
            colores = [COLOR_BLANCO] * 4
            if mostrar_resultado:
                for i in range(4):
                    if opciones[i] == respuesta_correcta:
                        colores[i] = COLOR_VERDE
                    elif opciones[i] == seleccionada:
                        colores[i] = COLOR_ROJO

            boton_respuesta.append(dibujar_boton(pantalla, colores[0], COLOR_FONDO, 0.225, 0.35, 0.2, 0.14, 0, 0, opciones[0]))
            boton_respuesta.append(dibujar_boton(pantalla, colores[1], COLOR_FONDO, 0.775, 0.35, 0.2, 0.14, 0, 0, opciones[1]))
            boton_respuesta.append(dibujar_boton(pantalla, colores[2], COLOR_FONDO, 0.225, 0.61, 0.2, 0.14, 0, 0, opciones[2]))
            boton_respuesta.append(dibujar_boton(pantalla, colores[3], COLOR_FONDO, 0.775, 0.61, 0.2, 0.14, 0, 0, opciones[3]))

        boton_comodin1 = dibujar_boton(pantalla, COLOR_BLANCO, COLOR_FONDO, 0.175, 0.87, 0.2, 0.08, 0, 0, "comodin 1")
        boton_comodin2 = dibujar_boton(pantalla, COLOR_BLANCO, COLOR_FONDO, 0.50, 0.87, 0.2, 0.08, 0, 0, "comodin 2")
        boton_comodin3 = dibujar_boton(pantalla, COLOR_BLANCO, COLOR_FONDO, 0.825, 0.87, 0.2, 0.08, 0, 0, "comodin 3")

        boton_contador = dibujar_boton(pantalla, COLOR_BLANCO, COLOR_FONDO, 0.50, 0.75, 0.1, 0.1, 0, 0, "contador")

        boton_atras = dibujar_boton(pantalla, COLOR_BLANCO, COLOR_FONDO, 0.06, 0.08, 0.09, 0.09, 0, 0, "atras")

        boton_mute = dibujar_boton(pantalla, COLOR_BLANCO, COLOR_FONDO, 0.94, 0.08, 0.09, 0.09, 0, 0, "mute")



    if pantalla_puntaje == True:
        for evento in pg.event.get():
            if evento.type == pg.QUIT:
                pg.quit()
                quit()
            
            
        pantalla.blit(imagen_puntaje, (0,0))

    
    if mostrar_resultado:
        tiempo_actual = pg.time.get_ticks()
        if tiempo_actual - tiempo_espera >= 2000:  # 2 segundos
            pregunta_actual += 1
            mostrar_resultado = False
            seleccionada = None
            mostrar_fondo_correcto = False
            mostrar_fondo_incorrecto = False

            if pregunta_actual >= len(preguntas):
                print("Fin del juego")
                pantalla_jugar = False
                pantalla_principal = True

    pg.display.update()

