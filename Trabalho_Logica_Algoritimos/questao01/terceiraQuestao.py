print("Bem-vindo a Madeireira do Lenhador Vagner do Amaral Gonçalves")


def escolha_tipo():
    """
    Pergunta ao usuário o tipo de madeira e retorna o valor da madeira
    Repete a pergunta caso o tipo de madeira seja invalido, aceitando somente PIN/PER/MOG/IPE/IMB.
    """
    while True:
        tipo_de_madeira = input("Entre com o tipo de madeira desejado\n"
                                "PIN - Tora de Pinho\n"
                                "PER - Tora de Peroba\n"
                                "MOG - Tora de Mogno\n"
                                "IPE - Tora de Ipê\n"
                                "IMB - Tora de Imbuia\n")

        if tipo_de_madeira == "PIN":
            valor_madeira = 150.40
        elif tipo_de_madeira == "PER":
            valor_madeira = 156.20
        elif tipo_de_madeira == "MOG":
            valor_madeira = 190.90
        elif tipo_de_madeira == "IPE":
            valor_madeira = 210.10
        elif tipo_de_madeira == "IMB":
            valor_madeira = 220.70
        else:
            print("Escolha inválida, entre com o modelo novamente\n")
            continue
        break

    return valor_madeira


def qtd_toras():
    """
    Pergunta ao usuário a quantidade de toras e retorna o desconto de acordo com a quantidade passada.
    Repete a pergunta caso o valor inserido seja inválido, entrada não númerica ou quantidade maior que 2000.
    """
    while True:
        try:
            qtd = float(input("Entre com a quantidade de toras (m³): "))
            if qtd > 2000:
                print(
                    "Não aceitamos pedidos com essa quantidade de toras.\n"
                    "Por favor, entre com a quantidade novamente.\n")
                continue
            elif qtd <= 100:
                desconto = 0
            elif qtd >= 100 and qtd < 500:
                desconto = 0.04
            elif qtd >= 500 and qtd < 1000:
                desconto = 0.09
            elif qtd >= 1000 and qtd <= 2000:
                desconto = 0.16

            return qtd, desconto

        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido.\n")


def tranporte():
    """
    Pergunta ao usuário o tipo de transporte e retorna o valor do transporte
    Repete a pergunta caso o tipo de transporte seja invalido, aceitando somente 1/2/3.
    """
    while True:
        tipo_transporte = input("Escolha o tipo de transporte:\n"
                                "1 - Transporte Rodoviário  - R$ 1000.00\n"
                                "2 - Transporte Ferroviário - R$ 2000.00\n"
                                "3 - Transporte Hidroviário - R$ 2500.00\n")

        if tipo_transporte == "1":
            valor_transporte = 1000.00
        elif tipo_transporte == "2":
            valor_transporte = 2000.00
        elif tipo_transporte == "3":
            valor_transporte = 2500.00
        else:
            print("Escolha inválida, entre com o modelo novamente (1/2/3)\n")
            continue
        break

    return valor_transporte


# Programa principal (main)
tipos_madeira = escolha_tipo()
qtd_tora, desconto = qtd_toras()
valor_transporte = tranporte()

total = ((tipos_madeira * qtd_tora) * (1 - desconto)) + valor_transporte
print(f"Total: R$ {total:.2f}")
