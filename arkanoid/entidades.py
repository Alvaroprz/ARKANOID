import os

import pygame as pg

from . import ALTO, ANCHO


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


class Ladrillo(pg.sprite.Sprite):

    def __init__(self):
        super().__init__()

        ruta_verde = os.path.join('resources', 'images', 'greenTile.png')
        self.image = pg.image.load(ruta_verde)
        self.rect = self.image.get_rect()

    def update(self):
        pass