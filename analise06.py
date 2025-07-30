import main 

##QUAL O TOTAL DE VENDAS POR SEGMENTO E POR ANO?
dados = main.df_dsa
main.pd.set_option('display.max_columns', None)

dados['Data_Pedido'] = main.pd.to_datetime(dados['Data_Pedido'], dayfirst=True)

dados['Ano'] = dados['Data_Pedido'].dt.year

vendas_ano_seg = dados.groupby(['Ano','Segmento'])['Valor_Venda'].sum()

print(vendas_ano_seg)