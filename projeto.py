
dados_climaticos = [
    {"dia": 1, "mes": "Junho", "temperatura": 21.4, "umidade": 82, "previsao_chuva": True},
    {"dia": 2, "mes": "Junho", "temperatura": 19.8, "umidade": 76, "previsao_chuva": False},
    {"dia": 3, "mes": "Junho", "temperatura": 23.1, "umidade": 69, "previsao_chuva": False},
    {"dia": 4, "mes": "Junho", "temperatura": 18.5, "umidade": 88, "previsao_chuva": True},
    {"dia": 5, "mes": "Junho", "temperatura": 25.0, "umidade": 61, "previsao_chuva": False},
    {"dia": 6, "mes": "Junho", "temperatura": 17.9, "umidade": 91, "previsao_chuva": True},
    {"dia": 7, "mes": "Junho", "temperatura": 22.7, "umidade": 73, "previsao_chuva": False},
    {"dia": 8, "mes": "Junho", "temperatura": 20.2, "umidade": 80, "previsao_chuva": True},
    {"dia": 9, "mes": "Junho", "temperatura": 24.4, "umidade": 65, "previsao_chuva": False},
    {"dia": 10, "mes": "Junho", "temperatura": 16.8, "umidade": 92, "previsao_chuva": True},
    {"dia": 11, "mes": "Junho", "temperatura": 26.1, "umidade": 58, "previsao_chuva": False},
    {"dia": 12, "mes": "Junho", "temperatura": 21.9, "umidade": 74, "previsao_chuva": False},
    {"dia": 13, "mes": "Junho", "temperatura": 18.1, "umidade": 89, "previsao_chuva": True},
    {"dia": 14, "mes": "Junho", "temperatura": 27.3, "umidade": 52, "previsao_chuva": False},
    {"dia": 15, "mes": "Junho", "temperatura": 23.8, "umidade": 68, "previsao_chuva": False},
    {"dia": 16, "mes": "Junho", "temperatura": 19.2, "umidade": 84, "previsao_chuva": True},
    {"dia": 17, "mes": "Junho", "temperatura": 20.5, "umidade": 79, "previsao_chuva": True},
    {"dia": 18, "mes": "Junho", "temperatura": 24.9, "umidade": 63, "previsao_chuva": False},
    {"dia": 19, "mes": "Junho", "temperatura": 17.4, "umidade": 90, "previsao_chuva": True},
    {"dia": 20, "mes": "Junho", "temperatura": 28.0, "umidade": 49, "previsao_chuva": False},
    {"dia": 21, "mes": "Junho", "temperatura": 22.1, "umidade": 71, "previsao_chuva": False},
    {"dia": 22, "mes": "Junho", "temperatura": 18.9, "umidade": 87, "previsao_chuva": True},
    {"dia": 23, "mes": "Junho", "temperatura": 25.6, "umidade": 60, "previsao_chuva": False},
    {"dia": 24, "mes": "Junho", "temperatura": 21.3, "umidade": 77, "previsao_chuva": True},
    {"dia": 25, "mes": "Junho", "temperatura": 19.7, "umidade": 83, "previsao_chuva": True},
    {"dia": 26, "mes": "Junho", "temperatura": 26.8, "umidade": 55, "previsao_chuva": False},
    {"dia": 27, "mes": "Junho", "temperatura": 23.4, "umidade": 66, "previsao_chuva": False},
    {"dia": 28, "mes": "Junho", "temperatura": 17.6, "umidade": 93, "previsao_chuva": True},
    {"dia": 29, "mes": "Junho", "temperatura": 24.1, "umidade": 70, "previsao_chuva": False},
    {"dia": 30, "mes": "Junho", "temperatura": 20.8, "umidade": 78, "previsao_chuva": True}
]

monitoramentos = []

def mostrar_descricao():
    """
    Finalidade: mostrar uma breve descrição da solução.
    Parâmetros: nenhum.
    Retorno: não retorna valor, apenas exibe informações na tela.
    """
    print("\nDESCRIÇÃO DA SOLUÇÃO")
    print("O Mino registra propriedades rurais, setores de plantio e dados climáticos. Com base na temperatura e umidade, o sistema informa o risco da lavoura. A solução ajuda o produtor a identificar seca, chuva excessiva ou risco de pragas. Assim, é possível tomar decisões antes que a produção seja prejudicada.")

def calcular_risco(temperatura_media, umidade_media, dias_com_chuva):
    """
    Finalidade: calcular o risco da lavoura usando médias climáticas.
    Parâmetros: temperatura_media (float), umidade_media (float), dias_com_chuva (int).
    Retorno: texto com o risco identificado.
    """
    if temperatura_media >= 30 and umidade_media <= 45:
        return "Alto risco de seca"

    elif temperatura_media <= 18:
        return "Risco de frio para a lavoura"

    elif umidade_media >= 85:
        return "Alto risco de umidade excessiva"

    elif dias_com_chuva >= 4 and umidade_media >= 75:
        return "Risco de chuva excessiva"

    elif temperatura_media >= 24 and umidade_media >= 70:
        return "Risco de pragas"

    else:
        return "Risco baixo"

def analisar_periodo():
    """
    Finalidade: permitir que o usuário escolha análise semanal ou mensal,
    desde que exista uma empresa cadastrada.
    Parâmetros: nenhum.
    Retorno: não retorna valor, apenas mostra o resultado da análise.
    """

    if len(monitoramentos) == 0:
        print("\nVocê precisa cadastrar uma empresa antes de analisar o risco climático.")
        return

    print("\n====== EMPRESAS CADASTRADAS ======")

    for empresa in monitoramentos:
        print(f"ID: {empresa['id']} - {empresa['propriedade']} | Cultura: {empresa['cultura']}")

    id_empresa = int(input("\nDigite o ID da empresa que deseja analisar: "))

    empresa_escolhida = None

    for empresa in monitoramentos:
        if empresa["id"] == id_empresa:
            empresa_escolhida = empresa

    if empresa_escolhida == None:
        print("Empresa não encontrada.")
        return

    print("\n====== ANÁLISE CLIMÁTICA ======")
    print("1 - Análise semanal")
    print("2 - Análise mensal")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        periodo = "Semanal"
        quantidade_dias = 7

    elif opcao == "2":
        periodo = "Mensal"
        quantidade_dias = 30

    else:
        print("Opção inválida.")
        return

    dados_periodo = dados_climaticos[:quantidade_dias]

    soma_temperatura = 0
    soma_umidade = 0
    dias_com_chuva = 0

    for dado in dados_periodo:
        soma_temperatura += dado["temperatura"]
        soma_umidade += dado["umidade"]

        if dado["previsao_chuva"] == True:
            dias_com_chuva += 1

    temperatura_media = soma_temperatura / quantidade_dias
    umidade_media = soma_umidade / quantidade_dias

    risco = calcular_risco(temperatura_media, umidade_media, dias_com_chuva)

    empresa_escolhida["periodo_analisado"] = periodo
    empresa_escolhida["temperatura_media"] = temperatura_media
    empresa_escolhida["umidade_media"] = umidade_media
    empresa_escolhida["dias_com_chuva"] = dias_com_chuva
    empresa_escolhida["risco"] = risco

    print("\n====== RESULTADO DA ANÁLISE ======")
    print(f"Propriedade: {empresa_escolhida['propriedade']}")
    print(f"Cidade: {empresa_escolhida['cidade']}")
    print(f"Setor: {empresa_escolhida['setor']}")
    print(f"Cultura: {empresa_escolhida['cultura']}")
    print(f"Período analisado: {periodo}")
    print(f"Quantidade de dias analisados: {quantidade_dias}")
    print(f"Média de temperatura: {temperatura_media:.1f}°C")
    print(f"Média de umidade: {umidade_media:.1f}%")
    print(f"Dias com previsão de chuva: {dias_com_chuva}")
    print(f"Risco identificado: {risco}")

def cadastrar_empresa():
    """
    Finalidade: cadastrar propriedade, setor de plantio e cultura.
    Parâmetros: nenhum.
    Retorno: não retorna valor, apenas salva os dados na lista de monitoramentos.
    """
    print("====== CADASTRAR EMPRESA ======")
    nome_propriedade = input("Digite o nome da propriedade: ")
    cidade = input("Digite a cidade da propriedade: ")
    area = float(input("Digite a área da propriedade em hectares: "))

    nome_setor = input("Digite o nome do setor de plantio: ")
    cultura = input("Digite a cultura plantada, exemplo: milho, soja, café: ")

    monitoramento = {
        "id": len(monitoramentos) + 1,
        "propriedade": nome_propriedade,
        "cidade": cidade,
        "area": area,
        "setor": nome_setor,
        "cultura": cultura
    }

    monitoramentos.append(monitoramento)

    print("\nMonitoramento cadastrado com sucesso!")

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

            if "risco" in item:
                print(f"Período analisado: {item['periodo_analisado']}")
                print(f"Média de temperatura: {item['temperatura_media']:.1f}°C")
                print(f"Média de umidade: {item['umidade_media']:.1f}%")
                print(f"Dias com previsão de chuva: {item['dias_com_chuva']}")
                print(f"Risco: {item['risco']}")
            else:
                print("Risco climático: ainda não analisado")

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
        print("3 - Analisar risco climático")
        print("4 - Mostrar relatório")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            mostrar_descricao()
        elif opcao == "2":
            cadastrar_empresa()
        elif opcao == "3":
            analisar_periodo()
        elif opcao == "4":
            mostrar_relatorio()
        elif opcao == "0":
            print("Sistema encerrado.")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()