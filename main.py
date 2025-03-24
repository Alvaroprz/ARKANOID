from arkanoid import ALTO, ANCHO
from arkanoid.game import Arkanoid

if __name__ == '__main__':
    print('Arrancamos el jugeo Arkanoid desde main.py')
    print(f'La pantalla tiene un tamaño de {ANCHO} x {ALTO}')
    juego = Arkanoid()
    juego.jugar()