
from src.emisiones.parser import EmisionesParser
from src.emisiones.layout import EmisionesLayoutMapper
from src.utils import generate_combinations
import pandas as pd

data_file = './files/PV.txt'

mapper = EmisionesLayoutMapper(layout_file='./layouts/PV.txt')
parser = EmisionesParser(mapper=mapper, data_file=data_file)
data_cleaned =parser.parse()

print(data_cleaned.head())

# Columnas que se deben expandir, la columna 0 no se incluye aquí
indices_to_expand = [33,34,108]

# Seleccionar columnas usando sus índices
columns_to_expand = [data_cleaned.columns[i] for i in indices_to_expand]

expanded_df = generate_combinations(data_cleaned[[data_cleaned.columns[0]] + columns_to_expand], columns_to_expand)

print(expanded_df.head())

expanded_df.to_csv('./data/emisiones_cuota.csv', index=False)
