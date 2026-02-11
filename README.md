spark-analytics-concorrentes/
│
├── README.md
├── requirements.txt
├── src/
│   ├── __init__.py
│   ├── spark_session.py
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── main.py
│
├── data/
│   └── raw/
│       ├── bairros.csv
│       ├── concorrentes.parquet
│       ├── eventos_de_fluxo.csv.gz
│       └── populacao.json
│
└── output/


# Desafio Técnico
A equipe de produtos têm recebido feedbacks do time comercial informando que clientes do setor de alimentação (restaurantes, pizzarias, bares, etc.) desejam análises mais profundas sobre concorrentes. Abaixo está um desafio com maior complexidade técnica e foco em escala, limpeza e análise de dados com **Pyspark** ou **SparkSQL**.

## Objetivo
Criar um job em **Spark/PySpark** que produza um conjunto de dados com as seguintes informações por concorrente:

- Código, nome e endereço do concorrente
- Faixa de preço praticada
- Nome do bairro
- População e densidade demográfica do bairro (população / área)

**A saída deve sere ordenada por densidade decrescente, depois por preço praticado crescente.**
&nbsp;

## Requisitos

1. **Tratar dados faltantes ou inconsistentes**
> Concorrentes com `CODIGO_BAIRRO` nulo devem ser descartados
2. **Persistência**
> O DataFrame final deve ser salvo em formato **Parquet**, particionado por `UF` e `CATEGORIA`
&nbsp;

## Dados disponíveis

Os dados que você utilizará para desenvolver o desafio podem ser acessados em:

```bash
bairros.csv
concorrentes.parquet
eventos_de_fluxo.csv.gz
populacao.json
```

### Descrição dos dados

**bairros.csv:** contém as informações dos bairros.

*Campo*        | *Descrição*
-------------  | -----------------
*CODIGO*       | *Código do bairro*
*NOME*         | *Nome do bairro*
*MUNICIPIO*    | *Cidade*
*UF*    	     | *Estado*
*AREA*    	   | *Área do bairro em km²*

&nbsp;

**concorrentes.parquet:** contém os dados de concorrentes.

*Campo*         | *Descrição*
-------------   | -----------------
*CODIGO*        | *Código do concorrente*
*NOME*          | *Nome do concorrente*
*CATEGORIA*     | *Atividade econômica*
*FAIXA_PRECO*   | *Faixa de preço praticada*
*ENDERECO*      | *Endereço*
*MUNICIPIO*     | *Cidade*
*UF*    	    | *Estado*
*CODIGO_BAIRRO* | *Bairro*

&nbsp;

**eventos_de_fluxo.csv.gz:** contém os dados do fluxo de pessoas. São eventos dos celulares de pessoas que permanecem mais de 5 minutos em um estabelecimento comercial.
Esses dados são enviados diariamente para a area. Este arquivo possui uma pequena amostra dos dados.

*Campo*                 | *Descrição*
---------------------   | -----------------
*CODIGO*                | *Código do evento*
*DATETIME*              | *Data e hora do evento*
*CODIGO_CONCORRENTE*    | *Código do concorrente*

&nbsp;

**populacao.json:** contém a quantidade de habitantes por bairro.

*Campo*                 | *Descrição*
---------------------   | -----------------
*CODIGO*                | *Código do bairro*
*POPULACAO*             | *Quantidade de habitantes*

&nbsp;

## Exemplo de saída:

```
{
   "cod_concorrente":"247437008633513",
   "nome_concorrente":"Porto da Pizza",
   "endereço":"Av Campos Salles, 751",
   "preco_praticado":"50.00",
   "bairro":"Morumbi",
   "população":32281,
   "densidade":2832,
}
```
&nbsp;

## Expectativa
Sua solução será avaliada pelos seguintes critérios:
- Qualidade e legibilidade do código
- Eficiência no processamento dos dados (uso de *JOINs*, filtros e transformações otimizadas)
- Tratamento de dados faltantes e inconsistentes
- Saída correta em formato **Parquet com particionamento exigido**
- Uso adequado de transformações distribuídas (como *groupBy*, *join*, *withColumn*, *explode*, etc.)
&nbsp;

## Entrega
- O notebook deve conter:
   - Células de código implementando as transformações
   - Células *markdown* explicando suas escolhas
   - *Opcional: uma função principal (main) ou pipeline reutilizável*
- O resultado deve ser salvo como `saida_concorrentes.parquet` particionado por `UF` e `CATEGORIA`


# Bom teste!

----------