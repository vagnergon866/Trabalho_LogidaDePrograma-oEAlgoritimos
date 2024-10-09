print("Bem vindo a Lista de Contatos do Vagner do Amaral Gonçalves")
print("-" * 60)
print("-" * 22, "MENU PRINCIPAL", "-" * 22)

lista_contatos = []
id_global = 5020784


def cadastrar_contato(id):
    print("-" * 17, "MENU CADASTRAR CONTRATOS", "-" * 17)
    global id_global
    print(f"Id do Contato: {id_global}")

    contato = {'id': id_global,
               'nome': input("Por favor entre com o nome do Contato: "),
               'atividade': input("Por favor entre com a atividade do Contato: "),
               'telefone': input("Por favor entre com o telefone do Contato: ")
               }

    id_global += 1
    lista_contatos.append(contato.copy())

    return


def consultar_contatos():
    print("-" * 17, "MENU DE CONSULTAS", "-" * 17)
    while True:
        consultar = input("Escolha uma das opções:\n"
                          "1. Consultar Todos\n"
                          "2. Consultar por Id \n"
                          "3. Consultar por Setor \n"
                          "4. Retornar ao menu\n")

        if consultar == "1":
            for contato in lista_contatos:
                print("-" * 30)
                print(f"id: {contato['id']}")
                print(f"Nome: {contato['nome']}")
                print(f"atividade: {contato['atividade']}")
                print(f"telefone: {contato['telefone']}")
                print("-" * 30)

        elif consultar == "2":
            id = int(input("Digite o id desejado: "))
            contrato_encontrado = lista_contatos

            for contato in lista_contatos:
                if contato['id'] == id:
                    print("-" * 30)
                    print(f"id: {contato['id']}")
                    print(f"Nome: {contato['nome']}")
                    print(f"atividade: {contato['atividade']}")
                    print(f"telefone: {contato['telefone']}")
                    print("-" * 30)

        elif consultar == "3":
            atividade = (input("Digite a Atividade do(s) Contato(s): "))
            contrato_encontrado = lista_contatos

            for contatos in lista_contatos:
                if contatos['atividade'].lower() == atividade.lower():
                    contrato_encontrado = contatos
                    print("-" * 30)
                    print(f"id: {contatos['id']}")
                    print(f"Nome: {contatos['nome']}")
                    print(f"atividade: {contatos['atividade']}")
                    print(f"telefone: {contatos['telefone']}")
                    print("-" * 30)

        elif consultar == "4":
            return

        else:
            print("Opção inválida")
            continue


def remover_contrato():
    print("-" * 17, "MENU REMOVER CONTATO", "-" * 17)
    id = int(input("Digite o id que deseja remover: "))
    contrato_encontrado = False

    for contato in lista_contatos:
        if contato['id'] == id:
            lista_contatos.remove(contato)
            print("Contato removido com sucesso!")
            break

        else:
            print("Id inválido")


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
