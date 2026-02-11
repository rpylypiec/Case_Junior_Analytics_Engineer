from pyspark.sql.functions import col, regexp_replace, round, when

def clean_concorrentes(df):
    return (
        df
        .filter(col("codigo_bairro").isNotNull())
        .withColumn(
            "codigo_bairro_norm",
            col("codigo_bairro").cast("double").cast("long")
        )
    )

def enrich_concorrentes(df_concorrentes, df_bairros, df_populacao):

    # Padronizando tipos antes do join
    df_bairros = df_bairros.withColumn(
        "codigo",
        col("codigo").cast("long")
    )

    df_populacao = df_populacao.withColumn(
        "codigo",
        col("codigo").cast("long")
    )

    df = (
        df_concorrentes.alias("c")
        .join(
            df_bairros.alias("b"),
            col("c.codigo_bairro_norm") == col("b.codigo"),
            "left"
        )
        .join(
            df_populacao.alias("p"),
            col("b.codigo") == col("p.codigo"),
            "left"
        )
    )

    return df

def build_final_dataset(df):
    return (
        df
        .withColumn(
    "densidade_demografica",
    round(
        col("p.populacao") / 
        when(col("b.area") != 0, col("b.area")).otherwise(None),
        2
    )
)

        .select(
            col("c.codigo").alias("cod_concorrente"),
            col("c.nome").alias("nome_concorrente"),
            "c.endereco",
            col("c.faixa_preco").alias("preco_praticado"),
            col("b.nome").alias("bairro"),
            "p.populacao",
            "densidade_demografica",
            "c.uf",
            "c.categoria"
        )
        .orderBy(
            col("densidade_demografica").desc(),
            col("preco_praticado").asc()
        )
    )
