import main 

##considere que a empresa concedeu o desconto de 15%
##qual seria a media do valor de venda antes e depois do descontro??
dados = main.df_dsa
main.pd.set_option('display.max_columns', None)

dados['Desconto'] = main.np.where(dados['Valor_Venda'] > 1000, 0.15, 0.10)

dados['Valor_Venda_Desconto'] = dados['Valor_Venda'] -(dados['Valor_Venda'] * dados['Desconto'])

Sem_desconto = dados.loc[dados['Desconto'] == 0.15, 'Valor_Venda']

Com_Desconto = dados.loc[dados['Desconto'] == 0.15, 'Valor_Venda_Desconto']

Media_Antes = Sem_desconto.mean()

Media_Apos = Com_Desconto.mean()

print(f' Media antes do desconto de 15% : {Media_Antes} media depois do desconto de 15% :{Media_Apos}')