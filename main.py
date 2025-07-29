import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt

#carrega o dataset
df_dsa = pd.read_csv(r"C:\Users\estudante\Desktop\Pedro\projetos\python_analyts\dataset_projeto2.csv")

##shape
#print(df_dsa.shape)
#
##amostra dos dados(5 primeiras linhas)
#print(df_dsa.head())
#
##amostra dos dados(5 ultimas linhas)
#print(df_dsa.tail())

#ANALISE EXPLORATORIA

##colunas do conjunto de dados
#print(df_dsa.columns)

##tipo de dados de cada coluna
#print(df_dsa.dtypes)

##resumo estatistico da coluna com o valor de venda
#print(df_dsa['Valor_Venda'].describe())

##verificando se há registros duplicados
#print(df_dsa[df_dsa.duplicated()])

##verificando se a valores ausentes
#print(df_dsa.isnull().sum())

