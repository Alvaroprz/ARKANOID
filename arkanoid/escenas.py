# estándar
import os
import random

# librerías de terceros
import pygame as pg

# tus dependencias
from . import ALTO, ANCHO, FPS, VIDAS
from .entidades import ContadorVidas, Ladrillo, Pelota, Raqueta
from .records import Records


class Escena:

    def __init__(self, pantalla):
        self.pantalla = pantalla

    def bucle_principal(self):
        """
        Este método debe ser implementado por todas y cada una de las escenas,
        en función de lo que estén esperando hasta la condición de salida
        del bucle de la escena.
        """
        print('Método vacío buble_principal de ESCENA')


class Portada(Escena):

    def __init__(self, pantalla):
        super().__init__(pantalla)
        ruta = os.path.join('resources', 'images', 'arkanoid_name.png')
        self.logo = pg.image.load(ruta)

        ruta_letra = os.path.join('resources', 'fonts', 'CabinSketch-Bold.ttf')
        self.letra = pg.font.Font(ruta_letra, 25)

    def bucle_principal(self):
        super().bucle_principal()

        print('Escena de Portada')

        salir = False
        finalizar = False
        while not salir:
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    salir = True
                    finalizar = True
                elif evento.type == pg.KEYDOWN:
                    if evento.key == pg.K_SPACE:
                        salir = True
                    elif evento.key == pg.K_ESCAPE:
                        salir = True
                        finalizar = True

            self.pantalla.fill((99, 0, 0))

            self.pintar_logo()
            self.pintar_mensaje()

            pg.display.flip()

        return finalizar

    def pintar_mensaje(self):
        mensaje = 'Pulsa <ESPACIO> para comenzar la partida'
        img = self.letra.render(mensaje, True, (255, 255, 255))
        x = (ANCHO - img.get_width()) // 2
        y = ALTO * 5 / 6
        self.pantalla.blit(img, (x, y))

    def pintar_logo(self):
        ancho, alto = self.logo.get_size()
        x = (ANCHO - ancho) // 2
        y = (ALTO - alto) // 3
        self.pantalla.blit(self.logo, (x, y))


class Partida(Escena):

    def __init__(self, pantalla):
        super().__init__(pantalla)

        self.reloj = pg.time.Clock()

        ruta_fondo = os.path.join('resources', 'images', 'background.jpg')
        self.fondo = pg.image.load(ruta_fondo)

        self.jugador = Raqueta()
        self.muro = pg.sprite.Group()
        self.pelota = Pelota(self.jugador)
        self.contador_vidas = ContadorVidas(VIDAS)

    def bucle_principal(self):
        super().bucle_principal()
        print('Escena de jugar la partida')

        self.crear_muro()
        salir = False
        pelota_en_movimiento = False
        abandonar_juego = False
        while not salir:
            self.reloj.tick(FPS)
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    salir = True
                    abandonar_juego = True
                if evento.type == pg.KEYDOWN:
                    if evento.key == pg.K_ESCAPE:
                        abandonar_juego = True
                        salir = True
                    elif evento.key == pg.K_SPACE:
                        pelota_en_movimiento = True
            self.pintar_fondo()
            self.muro.draw(self.pantalla)

            self.jugador.update()
            self.pantalla.blit(self.jugador.image, self.jugador.rect)

            self.pelota.update(pelota_en_movimiento)
            self.pantalla.blit(self.pelota.image, self.pelota.rect)

            if self.pelota.he_perdido:
                # parar la pelota
                pelota_en_movimiento = False
                # descontar una vida
                salir = self.contador_vidas.perder_vida()
                # desactivamos la marca de he perdido al reiniciar
                # la posición de la pelota y descontar una vida
                self.pelota.he_perdido = False

            golpeados = pg.sprite.spritecollide(self.pelota, self.muro, False)
            if len(golpeados) > 0:
                self.pelota.vel_y = -self.pelota.vel_y
                for ladrillo in golpeados:
                    ladrillo.update()

            pg.display.flip()

        return abandonar_juego

    def pintar_fondo(self):
        self.pantalla.fill((0, 0, 99))
        self.pantalla.blit(self.fondo, (0, 0))

    def crear_muro(self):
        filas = 4
        columnas = 5
        margen_superior = 40

        color = Ladrillo.ROJO
        for fila in range(filas):
            for col in range(columnas):
                if color == Ladrillo.ROJO:
                    color = Ladrillo.VERDE
                else:
                    color = Ladrillo.ROJO
                ladrillo = Ladrillo(color)
                ancho_muro = ladrillo.rect.width*columnas
                margen_izquierdo = (ANCHO - ancho_muro) // 2
                ladrillo.rect.x = margen_izquierdo + col * ladrillo.rect.width
                ladrillo.rect.y = margen_superior + fila * ladrillo.rect.height
                self.muro.add(ladrillo)


class Puntuaciones(Escena):

    def __init__(self, pantalla):
        super().__init__(pantalla)
        ruta_letra = os.path.join(
            'resources', 'fonts', 'CabinSketch-Bold.ttf')
        self.alto_linea = 90
        self.letra = pg.font.Font(ruta_letra, self.alto_linea // 2)
        self.color_letra = (245, 239, 66)
        self.margen_superior = ALTO // 4
        self.margen = ANCHO // 6

    def bucle_principal(self):
        super().bucle_principal()
        print('Escena de records')

        records = Records()
        records.cargar()
        print(records.game_records)

        salir = False
        while not salir:
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    salir = True

            self.pantalla.fill((0, 99, 0))

            img_titulo = self.letra.render('RECORDS', True, self.color_letra)
            x = (ANCHO - img_titulo.get_width()) // 2
            y = self.margen_superior // 2
            self.pantalla.blit(img_titulo, (x, y))

            linea = 0
            for record in records.game_records:
                nombre = record[0]
                puntos = str(record[1])
                # pintar nombre alineado a la izquierda
                img_nombre = self.letra.render(nombre, True, self.color_letra)
                x = self.margen
                y = self.margen_superior + self.alto_linea * linea
                self.pantalla.blit(img_nombre, (x, y))

                # pintar puntos alineados a la derecha
                img_puntos = self.letra.render(puntos, True, self.color_letra)
                x = ANCHO - self.margen - img_puntos.get_width()
                self.pantalla.blit(img_puntos, (x, y))

                linea += 1

            pg.display.flip()