

import pandas as pd
from sqlalchemy import create_engine

# Ruta do CSV limpo
ruta_csv = "datos/clean/alvedro_limpio.csv"

# Ler os datos
df = pd.read_csv(ruta_csv, sep=";")

print("Columnas:", df.columns.tolist())
print("Rexistros:", len(df))

# Conexión a PostgreSQL
engine = create_engine(
    "postgresql+psycopg2://alumno:alvedro123@localhost:5432/meteoroloxia"
)

# Cargar os datos limpos
df.to_sql("meteorologia", engine, if_exists="replace", index=False)

print("Datos limpos cargados correctamente.")
print(f"Rexistros cargados: {len(df)}")

engine.dispose()
