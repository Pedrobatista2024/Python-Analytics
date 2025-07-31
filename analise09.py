import main 

##QUAL A MEDIA DE VENDAS POR SEGMENTO, POR ANO E POR MÊS?
dados = main.df_dsa
main.pd.set_option('display.max_columns', None)

dados['Data_Pedido'] = main.pd.to_datetime(dados['Data_Pedido'], dayfirst=True)

dados['Ano'] = dados['Data_Pedido'].dt.year

dados['Mes'] = dados['Data_Pedido'].dt.month

media_seg_ano_mes = dados.groupby(['Ano','Mes','Segmento'])['Valor_Venda'].agg([main.np.sum, main.np.mean, main.np.median])

#print(media_seg_ano_mes)

anos = media_seg_ano_mes.index.get_level_values(0)
mes = media_seg_ano_mes.index.get_level_values(1)
segmento = media_seg_ano_mes.index.get_level_values(2)

main.plt.figure(figsize=(10,5))
main.sns.set()
fig1 = main.sns.relplot(kind='line',
                        data=media_seg_ano_mes,
                        y='mean',
                        x=mes,
                        hue=segmento,
                        col=anos,
                        col_wrap=2)

main.plt.show()