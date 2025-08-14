import main 

dados = main.df_dsa
main.pd.set_option('display.max_columns', None)

def autopct_format(values):
    def my_format(pct):
        total = sum(values)
        val = int(round(pct * total / 100.0))
        return '$ {v:d}'.format(v = val)
    return my_format



vendas_sub_cat = dados.groupby(['Categoria', 'SubCategoria']).sum(numeric_only = True).sort_values('Valor_Venda', ascending= False).head(12)

vendas_sub_cat = vendas_sub_cat[['Valor_Venda']].astype(int).sort_values(by='Categoria').reset_index()

agrup_categoria = dados.groupby('Categoria').sum(numeric_only = True).reset_index()

print(agrup_categoria)

cores_cat = ['#5d00de', '#0ee84f', '#e80e27']

cores_sub = ['#aa8cd4','#aa8cd5','#aa8cd6','#aa8cd7',
             '#26c957','#26c958','#26c959','#26c960',
             '#e65e65','#e65e66','#e65e67','#e65e68']

fig, ax = main.plt.subplots(figsize= (18,12) )

p1 = ax.pie(agrup_categoria['Valor_Venda'],
            radius= 1,
            labels= agrup_categoria['Categoria'],
            wedgeprops= dict(edgecolor= 'white'),
            colors= cores_cat)

p2 = ax.pie(vendas_sub_cat['Valor_Venda'],
            radius= 0.9,
            labels= vendas_sub_cat['SubCategoria'],
            autopct= autopct_format(vendas_sub_cat['Valor_Venda']),
            colors= cores_sub,
            labeldistance=0.7,
            wedgeprops=dict(edgecolor= 'white'),
            pctdistance=0.53,
            rotatelabels=True)

centre_circle = main.plt.Circle((0,0), 0.6, fc= 'white')

fig = main.plt.gcf()
fig.gca().add_artist(centre_circle)
main.plt.annotate(text='Total de Vendas' + '$ ' + str(int(sum(vendas_sub_cat['Valor_Venda']))), xy=(-0.2, 0))
main.plt.title('total de vendas por categorias e sub categorias')
main.plt.show()