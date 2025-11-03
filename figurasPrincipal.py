import pandas as pd

from funciones import triangulo, rectangulo, circulo


dataFile = pd.read_csv("figuras.csv")

print('Procesando figuras ...\n')

areas = []


for index, row in dataFile.iterrows():

    if row['FIGURA'] == 't':
        area = triangulo(row['MEDIDA1'], row['MEDIDA2'])
        print(area)
    elif row['FIGURA'] == 'r':
        area = rectangulo(row['MEDIDA1'], row['MEDIDA2'])
        print(area)
    elif row['FIGURA'] == 'r':
        area = circulo(row['MEDIDA1'])    
        print(area)
