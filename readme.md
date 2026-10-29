

# Análise de datos meteorolóxicos de Alvedro

## 1. Descrición do proxecto

Este proxecto ten como obxectivo analizar un conxunto de datos meteorolóxicos mediante Python, realizando tarefas de limpeza, preparación, análise exploratoria e visualización de datos.

Trabállanse variables como a temperatura, a precipitación, a humidade relativa, a velocidade do vento e a presión atmosférica. Tamén se analiza a evolución temporal destas variables e compáranse diferentes métodos de cálculo para avaliar a súa eficiencia.


## 2a. Tecnoloxías utilizadas

- **Python:** linguaxe de programación utilizada para a análise.
- **Pandas:** manipulación, limpeza e análise de datos.
- **NumPy:** operacións numéricas.
- **Matplotlib:** representación gráfica dos resultados.
- **Jupyter Notebook:** desenvolvemento e documentación do proceso de análise.

## 2b. Obtención dos datos

Os datos meteorolóxicos utilizados no proxecto proceden da fonte indicada como Meteosat e están dispoñibles nun ficheiro CSV publicado en GitHub.

- **Fonte indicada:** Meteosat.
- **Repositorio:** [Datasets de BigDataWirtz](https://github.com/bigdatawirtz/datasets).
- **Ficheiro:** [meteo_alvedro_2021_2025.csv](https://github.com/bigdatawirtz/datasets/tree/main/datasets/meteo_alvedro_2021_2025.csv).

### Notebook de descarga

O proxecto inclúe un notebook específico para descargar os datos orixinais e gardalos localmente. Para iso, utilízase a libraría `requests`, que permite realizar a petición HTTP ao enderezo do ficheiro CSV.

O código comproba que a descarga se realizou correctamente e garda o contido recibido, sen modificar os bytes, na seguinte ruta:

`datos/raw/meteo_alvedro_2021_2025.csv`

Deste xeito, consérvase unha copia dos datos orixinais na carpeta `datos/raw`, separada dos datos limpos que se xeran durante o proceso de preparación.

Este paso facilita a reproducibilidade do proxecto, xa que permite obter os datos de novo e manter separados o ficheiro orixinal e o resultado do proceso de limpeza.

## 3. Conxunto de datos

O conxunto de datos inicial contén **1.812 rexistros e 8 columnas**, correspondentes ás seguintes variables:

- Data.
- Temperatura media (ºC).
- Temperatura mínima (ºC).
- Temperatura máxima (ºC).
- Humidade relativa (%).
- Precipitación (mm).
- Vento medio (km/h).
- Presión atmosférica (hPa).

Os datos corresponden ao período comprendido entre 2021 e 2025.

## 4. Limpeza e preparación dos datos

Antes de realizar a análise, levouse a cabo un proceso de revisión e limpeza para identificar valores ausentes, erros de formato e medicións anómalas.

### 4.1. Revisión inicial

Analizáronse as dimensións do conxunto de datos, os tipos de cada columna e a presenza de valores nulos.

Detectáronse valores ausentes nas variables de temperatura, precipitación e presión atmosférica. Tamén se identificaron valores `-9999` nas columnas de temperatura e precipitación, que non representan medicións meteorolóxicas válidas.

Estes valores substituíronse por `NaN` para poder tratalos como datos ausentes.

### 4.2. Conversión dos tipos de datos

Unificáronse os formatos das datas mediante a súa conversión ao tipo `datetime`. As columnas de precipitación e presión atmosférica tamén se converteron a formato numérico (`float`).

Estas modificacións permiten realizar operacións temporais, cálculos estatísticos e representacións gráficas correctamente.

### 4.3. Detección de datas faltantes

Comparáronse as datas rexistradas co calendario diario completo do período 2021-2025. Identificáronse 27 días sen rexistro, dos cales 21 corresponden ao período comprendido entre o 3 e o 23 de xullo de 2023.

Debido á duración deste intervalo sen datos, decidiuse excluír xullo de 2023 das comparacións mensuais de temperatura e precipitación, xa que os resultados poderían non ser representativos.

Para os días illados sen rexistro, valorouse o tratamento de cada variable segundo a súa natureza e a dispoñibilidade de información.

### 4.4. Tratamento dos valores ausentes

Aplicáronse diferentes métodos de imputación en función da variable:

- **Precipitación:** os valores ausentes imputáronse mediante a media mensual correspondente.
- **Presión atmosférica:** o dato ausente imputouse utilizando a media do mes de setembro.
- **Temperaturas:** os valores ausentes imputáronse mediante a media mensual, debido á existencia de varios días sen datos e á dificultade de aplicar a interpolación en todos os casos.

### 4.5. Detección e corrección de valores anómalos nas temperaturas

Mediante estatísticas descritivas e representacións gráficas detectáronse valores extremos e incoherencias entre as temperaturas máxima, media e mínima.

Un dos casos identificados foi o do 13 de febreiro de 2025, no que a temperatura media superaba a máxima. Para corrixilo, substituíuse a temperatura media pola media aritmética das temperaturas máxima e mínima, obtendo un valor de 13,3 ºC.

Tamén se identificaron tres valores extremos:

- Temperatura mínima do 10 de setembro de 2021.
- Temperatura máxima do 19 de marzo de 2024.
- Temperatura máxima do 21 de marzo de 2025.

Estes valores corrixíronse mediante interpolación a partir de datos próximos. No caso do 19 de marzo de 2024, utilizouse o rexistro do 21 de marzo, xa que non había datos correspondentes ao día 20.

Finalmente, volveron representarse as variables meteorolóxicas para comprobar os resultados das correccións.

## 5. Análise exploratoria e visualización de datos

Unha vez limpos e preparados os datos, realizáronse diferentes representacións gráficas para estudar o comportamento das variables meteorolóxicas.

### 5.1. Evolución da temperatura media diaria

Representouse a temperatura media diaria e engadíronse medias móbiles de 7 e 30 días.

A media móbil de 7 días permite seguir máis de preto as variacións da temperatura, mentres que a de 30 días suaviza as oscilacións diarias e facilita a identificación das tendencias xerais a longo prazo.

### 5.2. Precipitación total mensual

Agrupáronse os datos de precipitación por mes e calculouse a precipitación total acumulada en cada período mensual.

Esta gráfica permite identificar os meses máis e menos chuviosos e observar a distribución da precipitación ao longo do período analizado.

### 5.3. Comparación da temperatura do último ano coa media histórica

Comparouse a temperatura media mensual do último ano dispoñible coa media histórica correspondente a cada mes.

Esta representación permite identificar os meses nos que a temperatura foi superior ou inferior á media histórica mensual. Para evitar resultados pouco representativos, excluíuse xullo de 2023 dos datos utilizados.

Cómpre ter en conta que a media histórica inclúe tamén os datos do último ano analizado.

### 5.4. Humidade relativa media por mes

Calculouse a humidade relativa media para cada mes do ano e representouse mediante un gráfico de barras.

As medias mensuais non mostran diferenzas moi destacadas. Para afondar na análise, utilizouse tamén un boxplot que permite comparar a distribución, a dispersión e os posibles valores extremos de cada mes.

No boxplot obsérvanse valores centrais algo máis baixos en marzo e abril, aínda que as diferenzas visuais non permiten concluír que sexan estatisticamente significativas.

## 6. Comparación de eficiencia: bucle `for` fronte a vectorización

Para estudar a eficiencia dos cálculos con pandas, calculouse a amplitude térmica diaria mediante dous métodos:

- Un bucle `for` que percorre as filas do DataFrame.
- Unha operación vectorizada que resta directamente as columnas de temperatura máxima e mínima.

A amplitude térmica calcúlase como:

`Amplitude térmica = Temperatura máxima − Temperatura mínima`

### Resultados obtidos

| Método | DataFrame orixinal (1.812 filas) | DataFrame ampliado (9.060 filas) |
|---|---:|---:|
| Bucle `for` | 64,9 ms | 329 ms |
| Operación vectorizada | 65 μs | 71,2 μs |

Os resultados mostran que a operación vectorizada é arredor de 1.000 veces máis rápida no DataFrame orixinal e máis de 4.000 veces máis rápida no DataFrame ampliado, segundo os tempos medidos.

Ao multiplicar por cinco o número de filas, o tempo do bucle aumenta aproximadamente na mesma proporción. Pola contra, o tempo da operación vectorizada apenas varía nesta proba.

Isto evidencia a vantaxe de utilizar operacións vectorizadas con pandas para realizar cálculos sobre grandes cantidades de datos, evitando percorrer as filas unha a unha mediante Python.

## 7. Gardado dos datos limpos

Unha vez finalizado o proceso de limpeza, corrección e imputación, os datos preparados gárdanse na carpeta `datos/clean`.

Deste xeito, quedan dispoñibles para realizar novas análises sen ter que repetir todo o proceso de preparación inicial.

## 8. Consultas en PostgreSQL

Para este exercicio utilizouse PostgreSQL, executado mediante Docker, para almacenar e consultar os datos meteorolóxicos limpos. A carga dos datos realizouse mediante Python, empregando pandas e SQLAlchemy coa función `to_sql()`. A táboa creada chámase `meteorologia` e contén 1.812 rexistros.

### 1. Cal foi a temperatura media de cada ano? Obsérvase algunha tendencia?

Calculouse a temperatura media anual mediante unha consulta SQL que agrupa os rexistros por ano e aplica a función `AVG()` á columna de temperatura media.

Os resultados obtidos foron os seguintes:

| Ano | Temperatura media (°C) |
|---:|---:|
| 2021 | 14,15 |
| 2022 | 15,00 |
| 2023 | 14,92 |
| 2024 | 14,44 |
| 2025 | 14,48 |

**Interpretación:** os valores máis altos corresponden a 2022 e 2023, mentres que o máis baixo se rexistrou en 2021. A temperatura media pasou de 14,15 °C en 2021 a 14,48 °C en 2025, o que supón un incremento de 0,33 °C.

Porén, non se observa unha tendencia ascendente continua durante os cinco anos analizados. Para avaliar unha posible tendencia relacionada co quentamento global sería necesario dispoñer dunha serie temporal máis longa.

### 2. Cal é, de media, o mes máis chuvioso e o máis seco?

Calculouse a precipitación media diaria para cada mes do ano, agrupando os rexistros polo mes do calendario e empregando a función `AVG()`. Excluíuse xullo de 2023 para evitar que os 21 días consecutivos sen rexistros distorsionasen o resultado.

Os resultados obtidos foron os seguintes:

| Mes | Precipitación media diaria (mm) |
|---|---:|
| Xaneiro | 4,06 |
| Febreiro | 3,45 |
| Marzo | 2,77 |
| Abril | 2,73 |
| Maio | 2,15 |
| Xuño | 1,73 |
| Xullo | 0,51 |
| Agosto | 0,44 |
| Setembro | 2,49 |
| Outubro | 4,77 |
| Novembro | 5,08 |
| Decembro | 4,42 |

**Interpretación:** novembro é o mes máis chuvioso, cunha precipitación media diaria de 5,08 mm, seguido de outubro, con 4,77 mm. Pola contra, agosto é o mes máis seco, cunha media de 0,44 mm diarios, seguido de xullo, con 0,51 mm.

Os resultados mostran que a precipitación media diaria é maior durante o outono e o inverno e menor durante o verán.

### Verificación dos resultados

As consultas executadas en PostgreSQL devolveron resultados coincidentes cos obtidos previamente no notebook de análise con pandas `alvedro_analise.ipynb` na sección `Cuestións`. 

Isto permite comprobar que os datos cargados na base de datos e as consultas realizadas son coherentes coas análises anteriores. Os resultados das demais cuestións e as gráficas correspondentes poden consultarse no notebook de análise.


### 3. Cal foi o día con máis vento rexistrado entre 2021 e 2025?

Para responder esta pregunta, realizouse unha consulta SQL sobre a táboa `meteorologia`. Ordenáronse os rexistros pola columna `Vento medio (km/h)` de maior a menor e seleccionouse o primeiro resultado mediante `LIMIT 1`.

**Resultado:** o día con máis vento de todo o período analizado foi o **31 de decembro de 2022**, cunha velocidade media do vento de **38,5 km/h**.

Este resultado permite identificar o día no que se rexistrou a maior velocidade media do vento nos datos meteorolóxicos de Alvedro entre 2021 e 2025.

## 9. Conclusión

O proxecto permite aplicar un fluxo de traballo completo de análise de datos meteorolóxicos: revisión inicial, conversión de tipos, detección de anomalías, tratamento de valores ausentes, visualización e comparación de métodos de cálculo.

A limpeza dos datos é fundamental para obter resultados fiables, mentres que as representacións gráficas facilitan a interpretación das tendencias meteorolóxicas. Ademais, a comparación de eficiencia mostra a importancia de empregar operacións vectorizadas para mellorar o rendemento do código.

## 10. Uso da intelixencia artificial

Durante a realización deste proxecto utilizouse **ChatGPT** como ferramenta de apoio para:

- Resolver dúbidas sobre Python, pandas e SQL.
- Axudar na limpeza e no tratamento dos datos meteorolóxicos, incluíndo os valores ausentes e os posibles erros.
- Corrixir erros no código e axudar a elaborar consultas SQL en PostgreSQL.
- Interpretar os resultados das análises e das gráficas.
- Comparar os resultados obtidos con pandas cos calculados en PostgreSQL.
- Mellorar a redacción das explicacións e a documentación do proxecto no ficheiro `README.md`.

A intelixencia artificial utilizouse como apoio durante o desenvolvemento, pero os códigos executáronse e os resultados comprobáronse no entorno de traballo para verificar que fosen coherentes cos datos analizados.

