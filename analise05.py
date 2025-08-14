import main 

dados = main.df_dsa
main.pd.set_option('display.max_columns', None)

segmento_mais_venda = dados.groupby('Segmento')['Valor_Venda'].sum().reset_index().sort_values(by= 'Valor_Venda', ascending= False)
print(segmento_mais_venda.head())

def autopct_format(values):
    def my_format(pct):
        total = sum(values)
        val = int(round(pct * total / 100.0))
        return '$ {v:d}'.format(v = val)
    return my_format

main.plt.figure(figsize=(10,5))

main.plt.pie(segmento_mais_venda['Valor_Venda'],
             labels=segmento_mais_venda['Segmento'],
             autopct=autopct_format(segmento_mais_venda['Valor_Venda']),
             startangle=90)

centre_circle = main.plt.Circle((0,0), 0.82, fc= 'white')
fig = main.plt.gcf()
fig.gca().add_artist(centre_circle)

main.plt.annotate(text='Total de Vendas:' + '$ ' + str(int(sum(segmento_mais_venda['Valor_Venda']))), xy= (-0.25, 0))
main.plt.title('Total de Vendas por Segmento')
main.plt.show()