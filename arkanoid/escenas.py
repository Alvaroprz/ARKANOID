import pygame as pg


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

    def bucle_principal(self):
        super().bucle_principal()

        print('Escena de Portada')

        salir = False
        while not salir:
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    salir = True

            self.pantalla.fill((99, 0, 0))
            pg.display.flip()


class Partida(Escena):

    def __init__(self, pantalla):
        super().__init__(pantalla)

    def bucle_principal(self):
        super().bucle_principal()
        print('Escena de jugar la partida')

        salir = False
        while not salir:
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    salir = True

            self.pantalla.fill((0, 0, 99))
            pg.display.flip()


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