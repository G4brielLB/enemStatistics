# Importação das bibliotecas
import pandas as pd
import matplotlib.pyplot as plt

# Importação dos dados e limpeza do dataframe
df = pd.read_csv('MICRODADOS_ENEM_2023.csv', sep=';', encoding='ISO-8859-1')
df.dropna()

# Dados do município de Campinas
df_campinas = df[df['NO_MUNICIPIO_PROVA'] == 'Campinas']