print("Bem vindo a Lista de Contatos do Vagner do Amaral Gonçalves")
print("-" * 60)
print("-" * 22, "MENU PRINCIPAL", "-" * 22)

lista_contatos = []
id_global = 5020784


def cadastrar_contato(id):
    print("-" * 17, "MENU CADASTRAR CONTRATOS", "-" * 17)

    global id_global

    contato = {'id': id_global,
               'nome': input("Por favor entre com o nome do Contato: "),
               'atividade': input("Por favor entre com a atividade do Contato: "),
               'telefone': input("Por favor entre com o telefone do Contato: ")
               }

    id_global += 1
    lista_contatos.append(contato.copy())

    return


def consultar_contatos():
    while True:
        consultar = input("Escolha uma das opções:\n"
                          "1. Consultar Todos\n"
                          "2. Consultar por Id \n"
                          "3. Consultar por Setor \n"
                          "4. Retornar ao menu")

        if consultar == "1":
            for contatos in lista_contatos:
                print(lista_contatos)

        elif consultar == "2":
            id = int(input("Digite o id desejado: "))
            contrato_encontrado = lista_contatos

            for contato in lista_contatos:
                if contato['id'] == id:
                    contrato_encontrado = contato
                    print(contato)

        elif consultar == "3":
            atividade = int(input("Digite a atividade desejada: "))
            contrato_encontrado = lista_contatos

            for contatos in lista_contatos:
                if contatos['atividade'].lower().upper() == atividade:
                    contrato_encontrado = contatos

        elif consultar == "4":
            return

        else:
            print("Opção inválida")
            continue


def remover_contrato():
    while True:
        id = int(input("Digite o id que deseja remover: "))
        contrato_encontrado = lista_contatos

        for contato in lista_contatos:
            if contato['id'] == id:
                contrato_encontrado = contato.delete()
            else:
                print("Id inválido")
                continue


# Programa principal (main)
while True:
    opcao = input("Escolha a opção desejada: \n"
                  "1 - Cadastrar Contrato\n"
                  "2 - Consultar Contrato(s)\n"
                  "3 - Remover Contrato\n"
                  "4 - Sair\n")

    if opcao == "1":
        cadastrar_contato(id_global)

    elif opcao == "2":
        consultar_contatos()

    elif opcao == "3":
        remover_contrato()

    elif opcao == "4":
        exit()
    else:
        print("Opção inválida\n")
        continue
