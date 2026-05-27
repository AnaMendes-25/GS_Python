
monitoramentos = []

def mostrar_descricao():
    """
    Finalidade: mostrar uma breve descrição da solução.
    Parâmetros: nenhum.
    Retorno: não retorna valor, apenas exibe informações na tela.
    """
    print("\nDESCRIÇÃO DA SOLUÇÃO")
    print("O Mino registra propriedades rurais, setores de plantio e dados climáticos. Com base na temperatura e umidade, o sistema informa o risco da lavoura. A solução ajuda o produtor a identificar seca, chuva excessiva ou risco de pragas. Assim, é possível tomar decisões antes que a produção seja prejudicada.")

def calcular_risco(temperatura, umidade):
    """
    Finalidade: calcular o risco da lavoura com base na temperatura e umidade.
    Parâmetros: temperatura (float), umidade (float).
    Retorno: texto com o nível de risco identificado.
    """
    if temperatura >= 35 and umidade <= 40:
        return "Alto risco de seca"
    elif umidade >= 85:
        return "Alto risco de chuva excessiva"
    elif temperatura >= 28 and umidade >= 70:
        return "Risco de pragas"
    else:
        return "Risco baixo"

def cadastrar_empresa():
    print("====== CADASTRAR EMPRESA ======")
    nome_propriedade = input("Digite o nome da propriedade: ")
    cidade = input("Digite a cidade da propriedade: ")
    area = float(input("Digite a área da propriedade em hectares: "))

    nome_setor = input("Digite o nome do setor de plantio: ")
    cultura = input("Digite a cultura plantada, exemplo: milho, soja, café: ")

    temperatura = float(input("Digite a temperatura atual: "))
    umidade = float(input("Digite a umidade atual: "))

    risco = calcular_risco(temperatura, umidade)

    monitoramento = {
        "id": len(monitoramentos) + 1,
        "propriedade": nome_propriedade,
        "cidade": cidade,
        "area": area,
        "setor": nome_setor,
        "cultura": cultura,
        "temperatura": temperatura,
        "umidade": umidade,
        "risco": risco
    }

    monitoramentos.append(monitoramento)

    print("\nMonitoramento cadastrado com sucesso!")
    print(f"Risco identificado: {risco}")

def mostrar_relatorio():
    """
    Finalidade: mostrar todos os monitoramentos cadastrados no sistema.
    Parâmetros: nenhum.
    Retorno: não retorna valor, apenas exibe o relatório na tela.
    """
    print("\nRELATÓRIO DE MONITORAMENTOS")

    if len(monitoramentos) == 0:
        print("Nenhum monitoramento cadastrado.")
    else:
        for item in monitoramentos:
            print("-----------------------------")
            print(f"ID: {item['id']}")
            print(f"Propriedade: {item['propriedade']}")
            print(f"Cidade: {item['cidade']}")
            print(f"Área: {item['area']} hectares")
            print(f"Setor: {item['setor']}")
            print(f"Cultura: {item['cultura']}")
            print(f"Temperatura: {item['temperatura']}°C")
            print(f"Umidade: {item['umidade']}%")
            print(f"Risco: {item['risco']}")

def menu():
    """
    Finalidade: exibir o menu principal e permitir a navegação do sistema.
    Parâmetros: nenhum.
    Retorno: nenhum.
    """
    while True:
        print("\n========== MINO ==========")
        print("1 - Descrição da solução")
        print("2 - Cadastrar empresa")
        print("3 - Mostrar relatório")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            mostrar_descricao()

        elif opcao == "2":
            cadastrar_empresa()

        elif opcao == "3":
            mostrar_relatorio()

        elif opcao == "0":
            print("Sistema encerrado.")
            break

        else:
            print("Opção inválida. Tente novamente.")

menu()