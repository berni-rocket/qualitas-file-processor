import pandas as pd
import itertools

def generate_combinations(df, columns_to_expand, delimiter='ý'):
    expanded_rows = []
    for idx, row in df.iterrows():
        # Dividir valores en columnas especificadas por 'ý' y generar combinaciones
        split_values = [row[col].split(delimiter) if delimiter in str(row[col]) else [row[col]] for col in columns_to_expand]
        for combination in itertools.product(*split_values):
            # Mantener fijo el valor de la columna 0
            new_row = [row[df.columns[0]]] + list(combination)
            expanded_rows.append(new_row)
    return pd.DataFrame(expanded_rows, columns=[df.columns[0]] + columns_to_expand)

data_cleaned = pd.read_csv('./data/emisiones.csv', header=1)

# Columnas que se deben expandir, la columna 0 no se incluye aquí
indices_to_expand = [33, 34, 13, 19]

# Seleccionar columnas usando sus índices
columns_to_expand = [data_cleaned.columns[i] for i in indices_to_expand]

expanded_df = generate_combinations(data_cleaned[[data_cleaned.columns[0]] + columns_to_expand], columns_to_expand)

expanded_df.to_csv('data/bonificacion_parseado.csv', index=False)
