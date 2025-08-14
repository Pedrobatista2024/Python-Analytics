import main 

dados = main.df_dsa
main.pd.set_option('display.max_columns', None)

top10_cidades_vendas = dados.groupby('Cidade')['Valor_Venda'].sum().reset_index().sort_values(by= 'Valor_Venda', ascending= False)
print(top10_cidades_vendas.head(10))

main.plt.figure(figsize=(16,6))
main.sns.set_palette('coolwarm')
main.sns.barplot(data= top10_cidades_vendas.head(10),y='Valor_Venda', x='Cidade').set(title= 'As 10 Cidades com Maior Total de Vendas')
main.plt.show()