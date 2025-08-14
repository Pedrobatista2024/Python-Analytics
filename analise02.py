import main as dadoss

dados = dadoss.df_dsa
dadoss.pd.set_option('display.max_columns', None)
#print(dados.head())

vendas_por_data = dados.groupby('Data_Pedido')['Valor_Venda'].sum()

print(vendas_por_data.head())

dadoss.plt.figure(figsize= (20,6))
vendas_por_data.plot(x = 'Data_Pedido', y = 'Valor_Venda', color = 'green')
dadoss.plt.title('Total de vendas Por Data do Pedido')
dadoss.plt.show()