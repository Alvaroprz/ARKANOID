import os

"""
Archivo actual
"""
print(__file__)

"""
Convierte una ruta relativa en una ruta absoluta
similar a pwd
"""
# directorio actual. Por defecto desde donde inicio el programa
print(os.path.realpath('.'))
# directorio anterior (padre) del directorio actual
print(os.path.realpath('..'))
print(os.path.realpath('./resources/images/ball1.png'))

"""
Ruta del directorio anterior
cd ..
"""
print(os.path.dirname(__file__))
print(
    os.path.dirname(
        os.path.dirname(
            os.path.dirname(__file__)
        ))
)

print(
    os.path.join(
        os.path.dirname(
            os.path.dirname(__file__)
        ),
        'data',
        'records.csv'
    )
)


"""
__file__  
    /home/tony/Escritorio/arkanoid/arkanoid/pruebas.py

os.path.dirname(__file__)
    /home/tony/Escritorio/arkanoid/arkanoid

os.path.dirname(os.path.dirname(__file__))
    /home/tony/Escritorio/arkanoid

os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    'data',
    'records.csv'

    /home/tony/Escritorio/arkanoid/data/records.csv
"""