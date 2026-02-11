def read_bairros(spark, path):
    return spark.read.csv(path, header=True, inferSchema=True)

def read_concorrentes(spark, path):
    return spark.read.parquet(path)

def read_populacao(spark, path):
    return spark.read.json(path)

def read_eventos(spark, path):
    return spark.read.csv(path, header=True, inferSchema=True)
