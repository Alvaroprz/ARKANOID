# estándar
import os

# librerías de terceros
import pygame as pg

# tus dependencias
from . import ALTO, ANCHO, FPS
from .entidades import Ladrillo, Raqueta


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
        self.muro = []

    def bucle_principal(self):
        super().bucle_principal()
        print('Escena de jugar la partida')

        salir = False
        while not salir:
            self.reloj.tick(FPS)
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    salir = True

            self.pintar_fondo()
            self.pintar_muro()

            self.jugador.update()
            self.pantalla.blit(self.jugador.image, self.jugador.rect)

            pg.display.flip()

    def pintar_fondo(self):
        self.pantalla.fill((0, 0, 99))
        self.pantalla.blit(self.fondo, (0, 0))

    def crear_muro(self):
        filas = 4
        columnas = 6

        for fila in range(filas):
            for col in range(columnas):
                ladrillo = Ladrillo()
                self.muro.append(ladrillo)
                # TODO: pintar cada ladrillo en su posición


class Puntuaciones(Escena):

    def __init__(self, pantalla):
        super().__init__(pantalla)

    def bucle_principal(self):
        super().bucle_principal()
        print('Escena de records')

        salir = False
        while not salir:
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    salir = True

            self.pantalla.fill((0, 99, 0))
            pg.display.flip()