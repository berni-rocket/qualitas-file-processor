import pandas as pd
import itertools

def generate_combinations(df, columns_to_expand, delimiter='ý'):
    expanded_rows = []
    for idx, row in df.iterrows():
        split_values = [row[col].split(delimiter) if delimiter in str(row[col]) else [row[col]] for col in columns_to_expand]
        for combination in itertools.product(*split_values):
            new_row = [row['ramo_poliza_endoso']] + list(combination)
            expanded_rows.append(new_row)
    return pd.DataFrame(expanded_rows, columns=['ramo_poliza_endoso'] + columns_to_expand)

data_cleaned = pd.read_csv('emisiones.data-emisiones', header=1)

multivariable_data_corrected = data_cleaned[['0', '33', '34', '13', '19']].copy()

multivariable_data_corrected.columns = ['ramo_poliza_endoso', 'fecha_vto_cuotas', 'importe_cuotas', '%_bonificacion', 'codigo_de_ramo_subramos']

columns_to_expand = ['fecha_vto_cuotas', 'importe_cuotas', '%_bonificacion', 'codigo_de_ramo_subramos']
expanded_df = generate_combinations(multivariable_data_corrected, columns_to_expand)

expanded_df.to_csv('data/bonificacion_parseado.csv', index=False)
