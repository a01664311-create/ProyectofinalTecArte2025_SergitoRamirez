import pandas as pd

dataFile = pd.read.csv("figuras.csv")

areas = []
perimetros = []

for index, row in dataFile.iterrows():
	print(f"Fila{index}: FIGURA={row['FIGURA']}, Medida1={row['MEDIDA1']}, Medida2={row['MEDIDA2']}")

