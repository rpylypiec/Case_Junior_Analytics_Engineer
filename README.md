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

---

# Como executar o projeto

## Pré-requisitos

Antes de executar o projeto, é necessário ter instalado:

- Python 3.9+
- Java 11 (obrigatório para execução do Spark)
- Git

---

## Instalação do Java 11 (macOS)

O Spark requer Java para funcionar corretamente.

### 1️) Verificar se já possui Java instalado

```bash
/usr/libexec/java_home -V
```

Se não houver nenhuma JVM instalada, será necessário instalar.

### 2️) Instalar Java 11 (Temurin recomendado)

Baixe a versão compatível com seu sistema operacional:

 https://adoptium.net/

Escolha:

- Version: 11 (LTS)
- Architecture compatível com sua máquina
- macOS x64 (para Intel) ou ARM (para Apple Silicon)

Instale o arquivo .pkg.

### 3️) Configurar variáveis de ambiente

Após instalar:

```bash
export JAVA_HOME=$(/usr/libexec/java_home -v 11)
export PATH="$JAVA_HOME/bin:$PATH"
```

Para validar:

```bash
java -version
```

Saída esperada:

```
openjdk version "11.x.x"
```

## Configuração do ambiente Python

### 1️) Clonar o repositório

```bash
git clone <url-do-repositorio>
cd spark-analytics-concorrentes
```

### 2️) Criar ambiente virtual

```bash
python -m venv .venv
source .venv/bin/activate
```

Verifique se está usando o Python correto:

```bash
which python
```

Deve apontar para:

```
.../spark-analytics-concorrentes/.venv/bin/python
```

### 3️) Instalar dependências

```bash
pip install -r requirements.txt
```

Dependências principais:

- pyspark
- py4j

## Estrutura do Projeto

```
spark-analytics-concorrentes/
│
├── README.md
├── requirements.txt
├── src/
│   ├── spark_session.py   # Criação da SparkSession
│   ├── extract.py         # Leitura das fontes de dados
│   ├── transform.py       # Limpeza, joins e cálculos
│   ├── load.py            # Escrita do dataset final
│   └── main.py            # Orquestração do pipeline
│
├── data/raw/              # Dados de entrada
└── output/                # Saída particionada em Parquet
```

O projeto segue uma separação modular baseada em pipeline de dados:

- Extract → leitura das fontes
- Transform → tratamento, joins e enriquecimento
- Load → persistência do resultado

## Executando o pipeline

Com o ambiente ativado:

```bash
python -m src.main
```

Ou:

```bash
python src/main.py
```

Durante a execução serão exibidos:

- Schemas das tabelas
- Primeiras linhas do dataset final
- Contagem total de registros
- Validação de nullabilidade

## Resultado gerado

Após execução bem-sucedida:

```
output/
   ├── UF=SP/
   │     ├── CATEGORIA=Restaurant/
   │     ├── CATEGORIA=Bar/
   │     └── ...
```

O dataset final será salvo em:

```
output/saida_concorrentes.parquet
```

Particionado por:

- UF
- CATEGORIA

## Validações aplicadas

O pipeline realiza as seguintes validações:

- Remoção de registros com CODIGO_BAIRRO nulo
- Padronização de tipos para evitar falhas de JOIN
- Correção de notação científica em codigo_bairro
- Tratamento de divisão por zero no cálculo de densidade
- Verificação de colunas nulas após enriquecimento

## Dataset final

Campos finais:

- cod_concorrente
- nome_concorrente
- endereco
- preco_praticado
- bairro
- populacao
- densidade_demografica
- uf
- categoria

Ordenação aplicada:

- Densidade demográfica (desc)
- Faixa de preço (asc)

## Observações Técnicas

Durante o desenvolvimento foi identificado um problema de notação científica na coluna codigo_bairro proveniente do dataset de concorrentes.

Exemplo:

```
3.519071005E9
```

A solução aplicada foi a conversão correta:

```
double → long
```

Garantindo compatibilidade com as tabelas dimensionais e evitando falhas silenciosas de JOIN.

## Resultado

O pipeline gera:

- 1450 registros válidos
- 0 valores nulos em bairro, população ou densidade
- Persistência otimizada em formato Parquet particionado


