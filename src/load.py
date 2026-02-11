def write_parquet(df, path):
    (
        df
        .write
        .mode("overwrite")
        .partitionBy("uf", "categoria")
        .parquet(path)
    )
