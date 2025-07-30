import main 

##QUAL O TOTAL DE VENDAS POR ESTADO?
dados = main.df_dsa
main.pd.set_option('display.max_columns', None)

#print(dados.head())

total_vendas_estado = dados.groupby('Estado')['Valor_Venda'].sum().reset_index()

print(total_vendas_estado.head())

main.plt.figure(figsize=(10,5))
main.sns.barplot(data=dados, y= 'Valor_Venda', x= 'Estado').set(title= 'Vendas Por Estado')
main.plt.xticks(rotation=80)
main.plt.show()