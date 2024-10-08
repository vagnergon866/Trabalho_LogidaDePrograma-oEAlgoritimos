print("-" * 10, "Bem-vindos a Pizzaria do Vagner do Amaral Gonçalves", "-" * 10)
print("-" * 30, " Cardápio  ", "-" * 30)
print("-" * 73)
print("-" * 9, "| Tamanho  |  Pizza Salgada(PS)  |  Pizza Doce(PD)  |", "-" * 9)
print("-" * 9, "|    P     |      R$ 30.00       |    R$ 34.00      |", "-" * 9)
print("-" * 9, "|    M     |      R$ 45.00       |    R$ 48.00      |", "-" * 9)
print("-" * 9, "|    G     |      R$ 60.00       |    R$ 66.00      |", "-" * 9)
print("-" * 73)

valor_total = 0
while True:
    while True:  # Loop para garantir que o tamanho esteja correto
        sabor = input("Entre com o sabor desejado (PS/PD): ")
        if sabor != "PS" and sabor != "PD":
            print("Sabor inválido. Tente novamente")
            continue
        break

    while True:  # Loop para garantir que o tamanho esteja correto
        tamanho = input("Entre com o tamanho desejado (P/M/G): ")
        if tamanho != "P" and tamanho != "M" and tamanho != "G":
            print("Tamanho inválido. Tente novamente")
            continue
        break

    if sabor == "PS" and tamanho == "P":
        sabor = "Salgada"
        valor = 30.00

    elif sabor == "PS" and tamanho == "M":
        sabor = "Salgada"
        valor = 45.00

    elif sabor == "PS" and tamanho == "G":
        sabor = "Salgada"
        valor = 60.00

    elif sabor == "PD" and tamanho == "P":
        sabor = "Doce"
        valor = 34.00

    elif sabor == "PD" and tamanho == "M":
        sabor = "Doce"
        valor = 48.00

    elif sabor == "PD" and tamanho == "G":
        sabor = "Doce"
        valor = 66.00

    print(f"Você pediu uma Pizza {sabor} no tamanho {tamanho}: R${valor}\n")

    valor_total += valor

    continuar_pedido = input("Deseja pedir mais alguma coisa? (S/N): ")
    if continuar_pedido == "S":
        continue  # Volta ao início do loop para novo pedido
    elif continuar_pedido == "N":
        print(f"Valor total a ser pago: R$ {valor_total}")
        break
