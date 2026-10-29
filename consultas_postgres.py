
import pandas as pd
from sqlalchemy import create_engine, text

# Conexión a PostgreSQL
engine = create_engine(
    "postgresql+psycopg2://alumno:alvedro123@localhost:5432/meteoroloxia"
)

# 1. Temperatura media de cada ano

consulta_temperatura = """
SELECT
    EXTRACT(YEAR FROM "Data"::date) AS ano,
    AVG(
        REPLACE("Temp. media (ºC)", ',', '.')::numeric
    ) AS temperatura_media
FROM meteorologia
GROUP BY EXTRACT(YEAR FROM "Data"::date)
ORDER BY ano;
"""


with engine.connect() as conexion:
    resultado_temperatura = pd.read_sql(
        text(consulta_temperatura), conexion
    )

print("Temperatura media de cada ano:")
print(resultado_temperatura.round(2).to_string(index=False))

engine.dispose()



# 2. Precipitación media mensual por mes do calendario

consulta_chuvia = """
SELECT
    EXTRACT(MONTH FROM "Data"::date)::integer AS mes,
    AVG(
        REPLACE("Precipitación (mm)", ',', '.')::numeric
    ) AS precipitacion_media
FROM meteorologia
WHERE NOT (
    EXTRACT(YEAR FROM "Data"::date) = 2023
    AND EXTRACT(MONTH FROM "Data"::date) = 7
)
GROUP BY EXTRACT(MONTH FROM "Data"::date)
ORDER BY mes;
"""

consulta_vento = """
SELECT
    "Data" AS data,
    REPLACE("Vento medio (km/h)", ',', '.')::numeric AS vento_kmh
FROM meteorologia
WHERE NULLIF(REPLACE("Vento medio (km/h)", ',', '.'), '') IS NOT NULL
ORDER BY REPLACE("Vento medio (km/h)", ',', '.')::numeric DESC
LIMIT 1;
"""

resultado_vento = pd.read_sql(
    text(consulta_vento),
    engine
)



with engine.connect() as conexion:
    resultado_chuvia = pd.read_sql(
        text(consulta_chuvia), conexion
    )

nomes_meses = {
    1: "Xaneiro", 2: "Febreiro", 3: "Marzo",
    4: "Abril", 5: "Maio", 6: "Xuño",
    7: "Xullo", 8: "Agosto", 9: "Setembro",
    10: "Outubro", 11: "Novembro", 12: "Decembro"
}

resultado_chuvia["mes"] = (
    resultado_chuvia["mes"].astype(int).map(nomes_meses)
)

print("\nPrecipitación media mensual (mm), de maior a menor:")
print(resultado_chuvia.round(2).to_string(index=False))

print("\nMes máis chuvioso:")
print(resultado_chuvia.iloc[0].to_string())

print("\nMes máis seco:")
print(resultado_chuvia.iloc[-1].to_string())

print("\nDía con máis vento de todo o período:")
print(resultado_vento.to_string(index=False))
