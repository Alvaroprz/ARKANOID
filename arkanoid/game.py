import pygame as pg

from . import ALTO, ANCHO
from .escenas import Partida, Portada, Puntuaciones


class Arkanoid:

    def __init__(self):
        pg.init()
        self.pantalla = pg.display.set_mode((ANCHO, ALTO))

        portada = Portada(self.pantalla)
        partida = Partida(self.pantalla)
        records = Puntuaciones(self.pantalla)

        self.escenas = [portada, partida, records]

    def jugar(self):

        for escena in self.escenas:
            fin = escena.bucle_principal()
            if fin == True:
                break

        pg.quit()


if __name__ == '__main__':
    print('Arrancamos el juego desde arkanoid.py')
    juego = Arkanoid()
    juego.jugar()