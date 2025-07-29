import main as dados

##QUAL CIDADE COM MAIOR VALOR DE VENDA DE PRODUTOS DA CATEGORIA 'OFFICE SUPPLIES'?
dados = dados.df_dsa
#print(dados.head())

dados_office_supplies = dados[dados['Categoria'] == 'Office Supplies']

vendas_por_cidade = dados_office_supplies.groupby('Cidade')['Valor_Venda'].sum()

cidade_maior_venda_office = vendas_por_cidade.idxmax()
valor_maior_venda_office = vendas_por_cidade.max()
print(cidade_maior_venda_office)
