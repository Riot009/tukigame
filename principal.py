from funciones import *
import pygame as pg

pg.init()
pantalla = inicializar_pantalla(RESOLUCION)

musica_pausada = False
musica_iniciada = False 

pantalla_principal = True
pantalla_jugar = False
pantalla_puntaje = False


preguntas = []
pregunta_actual = 0
respuesta_correcta = ""
opciones = []
boton_respuesta = []

while True:
    if pantalla_principal == True:
    #eventos
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
                    
                    #break
            
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
                else:
                    for i in range(len(boton_respuesta)):
                        if boton_respuesta[i].collidepoint(mouse_pos):
                            if opciones[i] == respuesta_correcta:
                                print("✅ Correcto")
                            else:
                                print("❌ Incorrecto")

                            pregunta_actual += 1
                            if pregunta_actual >= len(preguntas):
                                print("Fin del juego")
                                pantalla_jugar = False
                                pantalla_principal = True
                            break
                if boton_mute.collidepoint(mouse_pos):
                    if not musica_pausada:
                        pg.mixer.music.pause()
                        musica_pausada = True
                    else:
                        pg.mixer.music.unpause()
                        musica_pausada = False


            

        #pantalla       
        pantalla.blit(imagen_jugar, (0,0))

        if pregunta_actual < len(preguntas):
            pregunta_data = preguntas[pregunta_actual]
            texto_pregunta = pregunta_data["pregunta"]
            opciones = pregunta_data["respuestas"]
            respuesta_correcta = pregunta_data["correcta"]

        #botones

            pregunta = dibujar_boton(pantalla, COLOR_BLANCO, COLOR_FONDO, 0.50, 0.12, 0.4, 0.1, 0, 0, texto_pregunta)

            boton_respuesta.append(dibujar_boton(pantalla, COLOR_BLANCO, COLOR_FONDO, 0.225, 0.37, 0.2, 0.1, 0, 0, opciones[0]))
            boton_respuesta.append(dibujar_boton(pantalla, COLOR_BLANCO, COLOR_FONDO, 0.775, 0.37, 0.2, 0.1, 0, 0, opciones[1]))
            boton_respuesta.append(dibujar_boton(pantalla, COLOR_BLANCO, COLOR_FONDO, 0.225, 0.62, 0.2, 0.1, 0, 0, opciones[2]))
            boton_respuesta.append(dibujar_boton(pantalla, COLOR_BLANCO, COLOR_FONDO, 0.775, 0.62, 0.2, 0.1, 0, 0, opciones[3]))

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

    pg.display.update()

