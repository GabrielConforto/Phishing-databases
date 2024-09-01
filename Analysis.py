import pandas as pd

# Leitura das bases
url = "https://raw.githubusercontent.com/GabrielConforto/Phishing-databases/main/urls_phishing.csv"
url_x = "https://raw.githubusercontent.com/GabrielConforto/Phishing-databases/main/phishing_base_X.csv"
url_y = "https://raw.githubusercontent.com/GabrielConforto/Phishing-databases/main/phishing_base_Y.csv"

df = pd.read_csv(url)
df_x = pd.read_csv(url_x)
df_y = pd.read_csv(url_y)

# Gerar uma amostra aleatória da base principal
amostra_df = df.sample(n=1000, random_state=43)

#  Análise Exploratória de Dados (EDA)

print("Dimensões do dataframe:", df.shape)

print("Estatísticas descritivas:\n", df.describe())

print("Valores nulos por coluna:\n", df.isnull().sum())

if 'phishing' in df.columns:
    print("Distribuição da variável 'phishing':\n", df['phishing'].value_counts(normalize=True))
else:
    print("Distribuição das categorias:\n", df.iloc[:, -1].value_counts(normalize=True))

# Identificar qual das outras duas bases tem maior potencial de ter dados de phishing

colunas_comuns_x = df.columns.intersection(df_x.columns)
colunas_comuns_y = df.columns.intersection(df_y.columns)

colunas_numericas_comuns_x = df[colunas_comuns_x].select_dtypes(include=['number'])
colunas_numericas_comuns_y = df[colunas_comuns_y].select_dtypes(include=['number'])

correlacao_x = colunas_numericas_comuns_x.corrwith(df_x[colunas_numericas_comuns_x.columns].mean())
correlacao_y = colunas_numericas_comuns_y.corrwith(df_y[colunas_numericas_comuns_y.columns].mean())

print("Correlação com base X:\n", correlacao_x)
print("Correlação com base Y:\n", correlacao_y)

if correlacao_x.mean() > correlacao_y.mean():
    print("A base X tem maior potencial de ter dados de phishing.")
else:
    print("A base Y tem maior potencial de ter dados de phishing.")
