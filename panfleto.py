def imprimir_panfleto():
    print("=========================================")
    print("            Cardápio da Pizzaria Brasileira")
    print("=========================================\n")

    # Pizzas Salgadas
    print("Pizzas Salgadas:")
    pizzas_salgadas = ["Calabresa", "Portuguesa", "Mussarela", "Pepperoni"]
    for pizza in pizzas_salgadas:
        print("- " + pizza)
    print("\n")

    # Pizzas Doces
    print("Pizzas Doces:")
    pizzas_doces = ["Prestígio", "Chocolate", "Doce de Leite"]
    for pizza in pizzas_doces:
        print("- " + pizza)
    print("\n")
    
     # Bebidas
    print("Bebidas:")
    bebidas = ["Guaraná", "Cola", "Suco de Laranja", "Suco de Uva"]
    for bebida in bebidas:
        print("- " + bebida)
    print("\n")

    # Adicionais
    print("Adicionais:")
    adicionais = ["Bacon", "Requeijão", "Milho", "Azeitona"]
    for adicional in adicionais:
        print("- " + adicional)

if __name__ == "__main__":
    imprimir_panfleto()