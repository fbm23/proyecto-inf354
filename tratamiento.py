import pandas as pd
from sklearn.preprocessing import StandardScaler

# Cargar el dataset
df = pd.read_excel('electricidad.xlsx')

# Conversión de fechas
df['DateTime'] = pd.to_datetime(df['DateTime'])

# Normalización de los datos
scaler = StandardScaler()
columnas_numericas = df.columns[1:]  # Omitir la columna de fechas
df[columnas_numericas] = scaler.fit_transform(df[columnas_numericas])

# Guardar el archivo modificado
df.to_excel('dataset_modificado.xlsx', index=False)
