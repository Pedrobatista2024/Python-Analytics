import main 

##OS GESTORES DA EMPRESA ESTÃO CONSIDERANDO CONCEDER DIFERENTES FAIXAS DE DESCONDO USANDO AS REGRAS
## - SE O VALOR DA VENDA FOR MAIOR QUE 1000 RECEBE 15% DE DESCONCO
##- SE O VALOR DA VENDA FOR MENOR QUE 1000 RECEBE 10% DE DESCONCO
## QUANTAS VENDAS RECEBERIAM 15 % DE DESCONTO??
dados = main.df_dsa
main.pd.set_option('display.max_columns', None)

dados['Desconto'] = main.np.where(dados['Valor_Venda'] > 1000, 0.15, 0.10)

ndesconto = dados['Desconto'].value_counts()

print(f'No total:{ndesconto[0.15]} receberam o desconto de 15%')