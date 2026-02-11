from .spark_session import get_spark
from .extract import *
from .transform import clean_concorrentes, enrich_concorrentes, build_final_dataset
from .load import write_parquet
from pyspark.sql.functions import col, sum

def main():
    spark = get_spark()

    df_bairros = read_bairros(spark, "data/raw/bairros.csv")
    df_concorrentes = read_concorrentes(spark, "data/raw/concorrentes.parquet")
    df_populacao = read_populacao(spark, "data/raw/populacao.json")

    df_concorrentes_clean = clean_concorrentes(df_concorrentes)

    df_enriched = enrich_concorrentes(
        df_concorrentes_clean,
        df_bairros,
        df_populacao
    )

    df_final = build_final_dataset(df_enriched)

    #tipos de dados nas tabelas
    print("=== CONCORRENTES ===")
    df_concorrentes.printSchema()

    print("=== BAIRROS ===")
    df_bairros.printSchema()

    print("=== POPULACAO ===")
    df_populacao.printSchema()

    


    #validar tipos de dados final
    df_final.printSchema()
    df_final.show(5, truncate=False)

    #contagem de linhas final
    print("Total de registros:", df_final.count())

    #validar nulos
    df_final.select([
    sum(col(c).isNull().cast("int")).alias(c)
    for c in df_final.columns
    ]).show()



    write_parquet(df_final, "output/saida_concorrentes.parquet")

    spark.stop()

if __name__ == "__main__":
    main()

