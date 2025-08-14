import main 

dados = main.df_dsa
main.pd.set_option('display.max_columns', None)

dados['Desconto'] = main.np.where(dados['Valor_Venda'] > 1000, 0.15, 0.10)

ndesconto = dados['Desconto'].value_counts()

print(f'No total:{ndesconto[0.15]} receberam o desconto de 15%')