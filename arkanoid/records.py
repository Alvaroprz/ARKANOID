import csv
import os

from . import MAX_RECORDS


class Records:

    filename = 'records.csv'
    base_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    path = os.path.join(base_dir, 'data', filename)

    def __init__(self):
        self.game_records = []
        self.comprobar_archivo()

    def comprobar_archivo(self):
        dir_datos = os.path.dirname(self.path)
        # dir_datos = os.path.join(self.base_dir, 'data')
        if not os.path.isdir(dir_datos):
            print('El directorio de datos no existe, lo estoy creando para ti')
            os.makedirs(dir_datos)
        if not os.path.exists(self.path):
            print('El archivo de records no existe, sin records')
            self.reset()

    def guardar(self):
        with open(self.path, mode='w') as file:
            writer = csv.writer(file, lineterminator='\n')
            writer.writerow(['nombre', 'puntos'])
            writer.writerows(self.game_records)

    def cargar(self):
        with open(self.path, mode='r') as file:
            reader = csv.reader(file, lineterminator='\n')
            self.game_records = []
            contador = 0
            for linea in reader:
                contador += 1
                if contador == 1:
                    continue
                self.game_records.append([linea[0], int(linea[1])])

    def puntuacion_menor(self):
        return self.game_records[-1][1]

    def insertar_record(self, nombre, puntuacion):
        if puntuacion <= self.puntuacion_menor():
            return
        contador = 0
        for item in self.game_records:
            if puntuacion > item[1]:
                self.game_records.insert(contador, [nombre, puntuacion])
                break
            contador += 1
        self.game_records = self.game_records[:MAX_RECORDS]
        # self.game_records.append([nombre, puntuacion])
        # self.game_records.sort(key=lambda dato: dato[1], reverse=True)
        self.guardar()

    def reset(self):
        self.game_records = []
        for cont in range(MAX_RECORDS):
            self.game_records.append(['---', 0])
        self.guardar()