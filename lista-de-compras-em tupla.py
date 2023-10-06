# tranformar a lista de compras em dados não mutáveis

compras = ['Farinha de Trigo', 'Calabresa', 'Milho', 'Açucar', 'Levain',
'Champignon', 'Molho de Tomate', 'Frango', 'Requeijão', 'Lombo']

compras_tupla = tuple(compras)

print(type(compras_tupla))