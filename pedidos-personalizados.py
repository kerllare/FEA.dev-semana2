# Dicionário de preços dos ingredientes
precos_ingredientes = {
    'massa sem gúten': 10.0,
    'massa tradicional': 8.0,
    'massa integral': 9.0,
    'molho barbecue': 2.0,
    'molho de tomate': 1.5,
    'atum': 3.0,
    'frango': 4.0,
    'mussarela': 2.5,
    'azeitona': 1.0,
    'cebola': 1.0,
    'pimentão': 1.5,
    'tomate': 1.0,
    'borda com queijo': 3.0,
    'molho bechamel': 2.0,
}

# Função para calcular o preço de um pedido
def calcular_preco_pedido(pedido):
    preco_total = 0.0
    for ingrediente in pedido:
        if ingrediente in precos_ingredientes:
            preco_total += precos_ingredientes[ingrediente]
        else:
            print(f"Ingrediente desconhecido: {ingrediente}")
    return preco_total

# Pedidos
pedido1 = ['massa sem gúten', 'molho barbecue', 'frango', 'pimentão', 'tomate']
pedido2 = ['massa tradicional', 'molho de tomate', 'atum', 'mussarela', 'azeitona', 'cebola', 'pimentão', 'tomate', 'borda com queijo']
pedido3 = ['massa integral', 'molho bechamel', 'cebola', 'pimentão', 'tomate', 'frango', 'borda com queijo']

# Calcular o preço de cada pedido
preco_pedido1 = calcular_preco_pedido(pedido1)
preco_pedido2 = calcular_preco_pedido(pedido2)
preco_pedido3 = calcular_preco_pedido(pedido3)

# Imprimir o preço de cada pedido
print(f'Preço do pedido 1: R$ {preco_pedido1:.2f}')
print(f'Preço do pedido 2: R$ {preco_pedido2:.2f}')
print(f'Preço do pedido 3: R$ {preco_pedido3:.2f}')

# Total das vendas
total_vendas = preco_pedido1 + preco_pedido2 + preco_pedido3
print(f'Total das vendas: R$ {total_vendas:.2f}')
