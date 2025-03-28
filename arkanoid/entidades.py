import os
from random import randint

import pygame as pg

from . import ALTO, ANCHO, VEL_MAX_X, VEL_MAX_Y, VEL_MIN_Y


class Raqueta(pg.sprite.Sprite):
    """
    1. Es un sprite, usar herencia
    2. Se puede mover...
    3. Pintar en pantalla...
    4. Situarlo en la pos inicial...
    """

    velocidad = 10

    def __init__(self):
        super().__init__()

        self.imagenes = []
        for i in range(3):
            ruta_img = os.path.join('resources', 'images', f'electric0{i}.png')
            img = pg.image.load(ruta_img)
            self.imagenes.append(img)
        self.contador = 0
        self.image = self.imagenes[self.contador]
        self.rect = self.image.get_rect(midbottom=(ANCHO // 2, ALTO - 25))

    def update(self):
        # 00 -> 01 -> 02 -> 00 -> 01...
        # 00 -> 01 -> 02 -> 01 -> 00...
        self.contador += 1
        if self.contador >= len(self.imagenes):
            self.contador = 0
        self.image = self.imagenes[self.contador]

        teclas = pg.key.get_pressed()

        if teclas[pg.K_LEFT]:
            self.rect.x -= self.velocidad
            if self.rect.left < 0:
                self.rect.left = 0

        if teclas[pg.K_RIGHT]:
            self.rect.x += self.velocidad
            if self.rect.right > (ANCHO-1):
                self.rect.right = (ANCHO-1)


"""
- Cargar la imagen roja, además de la verde
- La única diferencia es la imagen

verde = Ladrillo(0)
rojo = Ladrillo("RJ")

"""
# TODO: hacer esto menos cutre, es decir, más elegante
IMAGENES = [
    pg.image.load(os.path.join('resources', 'images', 'greenTile.png')),
    pg.image.load(os.path.join('resources', 'images', 'redTile.png')),
    pg.image.load(os.path.join('resources', 'images', 'redTileBreak.png')),
]


class Ladrillo(pg.sprite.Sprite):

    VERDE = 0
    ROJO = 1
    ROJO_ROTO = 2

    def __init__(self, color=VERDE):
        super().__init__()
        self.tipo = color
        # en función del valor que recibo en `color` uso la imagen adecuada
        self.image = IMAGENES[color]
        self.rect = self.image.get_rect()

    def update(self):
        if self.tipo == Ladrillo.ROJO:
            self.tipo = Ladrillo.ROJO_ROTO
        else:
            self.kill()
        self.image = IMAGENES[self.tipo]


class Pelota(pg.sprite.Sprite):

    def __init__(self, raqueta):
        super().__init__()
        self.jugador = raqueta
        ruta = os.path.join('resources', 'images', 'ball1.png')
        self.image = pg.image.load(ruta)
        self.rect = self.image.get_rect()
        self.init_velocidades()
        self.he_perdido = False

    def update(self, en_movimiento):

        if en_movimiento == False:
            self.rect.midbottom = self.jugador.rect.midtop
        else:
            self.rect.x += self.vel_x
            self.rect.y += self.vel_y

            # rebota a izquierda y derecha en la pantalla
            if self.rect.left <= 0 or self.rect.right >= ANCHO:
                self.vel_x = -self.vel_x

            # rebota en la parte superior de la pantalla
            if self.rect.top <= 0:
                self.vel_y = self.vel_y * (-1)

            # rebota en la raqueta
            if pg.sprite.collide_mask(self, self.jugador):
                self.init_velocidades()

            # True si la pelota se sale de la pantalla por la parte inferior
            self.he_perdido = self.rect.top > ALTO

    def init_velocidades(self):
        self.vel_x = randint(-VEL_MAX_X, +VEL_MAX_X)
        self.vel_y = randint(-VEL_MAX_Y, -VEL_MIN_Y)

    def pierdes(self):
        print('Pierdes una vida')


class ContadorVidas:

    def __init__(self, vidas_iniciales):
        self.vidas = vidas_iniciales

    def perder_vida(self):
        self.vidas -= 1
        print('Has perdido una vida. Te quedan', self.vidas)
        return self.vidas == 0

    def pintar(self):
        pass