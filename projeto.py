# Projeto Mino - Transporte de Laranja
# Sistema simples para analisar risco climático para o transporte da laranja

rotas_cadastradas = []

dados_climaticos = [  # Lista simulada de dados climáticos do mês de Junho
    {"dia": 1, "mes": "Junho", "temperatura": 21.4, "umidade": 82, "previsao_chuva": True, "vento": 18},
    {"dia": 2, "mes": "Junho", "temperatura": 19.8, "umidade": 76, "previsao_chuva": False, "vento": 12},
    {"dia": 3, "mes": "Junho", "temperatura": 23.1, "umidade": 69, "previsao_chuva": False, "vento": 10},
    {"dia": 4, "mes": "Junho", "temperatura": 18.5, "umidade": 88, "previsao_chuva": True, "vento": 25},
    {"dia": 5, "mes": "Junho", "temperatura": 25.0, "umidade": 61, "previsao_chuva": False, "vento": 14},
    {"dia": 6, "mes": "Junho", "temperatura": 17.9, "umidade": 91, "previsao_chuva": True, "vento": 28},
    {"dia": 7, "mes": "Junho", "temperatura": 22.7, "umidade": 73, "previsao_chuva": False, "vento": 11},
    {"dia": 8, "mes": "Junho", "temperatura": 20.2, "umidade": 80, "previsao_chuva": True, "vento": 20},
    {"dia": 9, "mes": "Junho", "temperatura": 24.4, "umidade": 65, "previsao_chuva": False, "vento": 13},
    {"dia": 10, "mes": "Junho", "temperatura": 16.8, "umidade": 92, "previsao_chuva": True, "vento": 30},
    {"dia": 11, "mes": "Junho", "temperatura": 26.1, "umidade": 58, "previsao_chuva": False, "vento": 9},
    {"dia": 12, "mes": "Junho", "temperatura": 21.9, "umidade": 74, "previsao_chuva": False, "vento": 12},
    {"dia": 13, "mes": "Junho", "temperatura": 18.1, "umidade": 89, "previsao_chuva": True, "vento": 26},
    {"dia": 14, "mes": "Junho", "temperatura": 27.3, "umidade": 52, "previsao_chuva": False, "vento": 8},
    {"dia": 15, "mes": "Junho", "temperatura": 23.8, "umidade": 68, "previsao_chuva": False, "vento": 15},
    {"dia": 16, "mes": "Junho", "temperatura": 19.2, "umidade": 84, "previsao_chuva": True, "vento": 22},
    {"dia": 17, "mes": "Junho", "temperatura": 20.5, "umidade": 79, "previsao_chuva": True, "vento": 19},
    {"dia": 18, "mes": "Junho", "temperatura": 24.9, "umidade": 63, "previsao_chuva": False, "vento": 10},
    {"dia": 19, "mes": "Junho", "temperatura": 17.4, "umidade": 90, "previsao_chuva": True, "vento": 27},
    {"dia": 20, "mes": "Junho", "temperatura": 28.0, "umidade": 49, "previsao_chuva": False, "vento": 7},
    {"dia": 21, "mes": "Junho", "temperatura": 22.1, "umidade": 71, "previsao_chuva": False, "vento": 13},
    {"dia": 22, "mes": "Junho", "temperatura": 18.9, "umidade": 87, "previsao_chuva": True, "vento": 24},
    {"dia": 23, "mes": "Junho", "temperatura": 25.6, "umidade": 60, "previsao_chuva": False, "vento": 11},
    {"dia": 24, "mes": "Junho", "temperatura": 21.3, "umidade": 77, "previsao_chuva": True, "vento": 18},
    {"dia": 25, "mes": "Junho", "temperatura": 19.7, "umidade": 83, "previsao_chuva": True, "vento": 21},
    {"dia": 26, "mes": "Junho", "temperatura": 26.8, "umidade": 55, "previsao_chuva": False, "vento": 9},
    {"dia": 27, "mes": "Junho", "temperatura": 23.4, "umidade": 66, "previsao_chuva": False, "vento": 12},
    {"dia": 28, "mes": "Junho", "temperatura": 17.6, "umidade": 93, "previsao_chuva": True, "vento": 31},
    {"dia": 29, "mes": "Junho", "temperatura": 24.1, "umidade": 70, "previsao_chuva": False, "vento": 14},
    {"dia": 30, "mes": "Junho", "temperatura": 20.8, "umidade": 78, "previsao_chuva": True, "vento": 20}
]

# Finalidade: mostrar uma descrição curta da solução Mino.
# Parâmetros: não recebe parâmetros.
# Retorno: não retorna valor, apenas exibe informações na tela.
def mostrar_descricao():
    print("\n--- Sobre o Mino ---")
    print("O Mino ajuda no transporte da laranja após a colheita.")
    print("Ele analisa clima, chuva, umidade e fim de safra.")
    print("Com isso, indica se a rota está segura ou arriscada.")
    print("O sistema usa sinais verde, amarelo e vermelho.")
    print("Assim, o produtor pode decidir o melhor momento para enviar a carga.")

# Finalidade: buscar os dados climáticos de um dia específico.
# Parâmetros: recebe o dia escolhido pelo usuário.
# Retorno: retorna um dicionário com os dados do clima ou None se não encontrar.
def buscar_clima_por_dia(dia):
    for clima in dados_climaticos:
        if clima["dia"] == dia:
            return clima
    return None

# Finalidade: cadastrar uma rota de transporte da laranja.
# Parâmetros: não recebe parâmetros.
# Retorno: retorna um dicionário com os dados da rota cadastrada.
def cadastrar_rota():
    print("\n--- Cadastrar rota de transporte ---")

    produtor = input("Digite o nome do produtor ou empresa: ")
    origem = input("Digite a cidade de origem da carga: ")
    destino = input("Digite a cidade de destino da carga: ")

    try:
        dia = int(input("Digite o dia planejado para o transporte em junho de 1 a 30: "))
    except ValueError:
        print("Erro: digite apenas números para o dia.")
        return None

    fim_safra = input("A carga está no fim de safra? S/N: ").upper()

    if fim_safra != "S" and fim_safra != "N":
        print("Erro: responda apenas S ou N.")
        return None

    clima = buscar_clima_por_dia(dia)

    if clima is None:
        print("Erro: não existem dados climáticos para esse dia.")
        return None

    rota = {
        "produtor": produtor,
        "origem": origem,
        "destino": destino,
        "dia": dia,
        "fim_safra": fim_safra
    }

    rotas_cadastradas.append(rota)

    print("Rota cadastrada com sucesso!")
    return rota

# Finalidade: analisar o risco climático de uma rota cadastrada.
# Parâmetros: recebe uma rota com origem, destino, dia e informação de fim de safra.
# Retorno: retorna o nível de risco e a recomendação para o transporte.
def analisar_risco_transporte(rota):
    clima = buscar_clima_por_dia(rota["dia"])
    pontos_risco = 0
    motivos = []

    if clima["temperatura"] >= 33:
        pontos_risco += 2
        motivos.append("calor extremo, com risco de desidratação da fruta")
    elif clima["temperatura"] >= 29:
        pontos_risco += 1
        motivos.append("temperatura elevada, exigindo cuidado no transporte")

    if clima["previsao_chuva"]:
        pontos_risco += 2
        motivos.append("chuva forte, com risco de atraso e danos na carga")

    if clima["umidade"] >= 85:
        pontos_risco += 2
        motivos.append("umidade alta, aumentando chance de fungos")
    elif clima["umidade"] >= 75:
        pontos_risco += 1
        motivos.append("umidade moderada, exigindo atenção")

    if clima["vento"] >= 55:
        pontos_risco += 2
        motivos.append("vento muito forte, podendo dificultar o transporte e aumentar o risco na estrada")

    elif clima["vento"] >= 30:
        pontos_risco += 1
        motivos.append("vento moderado/forte, exigindo mais cuidado durante o transporte da carga")

    if rota["fim_safra"] == "S":
        pontos_risco += 1
        motivos.append("fim de safra, com frutas mais maduras e sensíveis")

    if pontos_risco <= 1:
        sinal = "VERDE"
        recomendacao = "Clima favorável. A rota está segura para envio."
    elif pontos_risco <= 4:
        sinal = "AMARELO"
        recomendacao = "Atenção! O transporte pode acontecer, mas exige cuidados."
    else:
        sinal = "VERMELHO"
        recomendacao = "Alto risco! O ideal é reprogramar a rota."

    return sinal, recomendacao, motivos , pontos_risco

# Finalidade: procurar o melhor dia para transporte nos próximos 7 dias.
# Parâmetros: recebe a rota escolhida pelo usuário.
# Retorno: retorna o melhor dia encontrado ou None se não existir previsão disponível.
def sugerir_melhor_dia(rota):
    dia_atual = rota["dia"]
    melhor_dia = None
    menor_risco = 999 # Começa com um valor alto para garantir que qualquer dia com risco menor seja escolhido

    for proximo_dia in range(dia_atual + 1, dia_atual + 8):
        clima = buscar_clima_por_dia(proximo_dia)

        if clima is not None:
            rota_teste = {
                "produtor": rota["produtor"],
                "origem": rota["origem"],
                "destino": rota["destino"],
                "dia": proximo_dia,
                "fim_safra": rota["fim_safra"]
            }

            sinal, recomendacao, motivos, pontos_risco = analisar_risco_transporte(rota_teste)

            if pontos_risco < menor_risco:
                menor_risco = pontos_risco
                melhor_dia = {
                    "dia": proximo_dia,
                    "sinal": sinal,
                    "recomendacao": recomendacao,
                    "pontos_risco": pontos_risco,
                    "motivos": motivos
                }

    return melhor_dia

# Finalidade: permitir que o usuário escolha uma rota cadastrada para análise.
# Parâmetros: não recebe parâmetros.
# Retorno: não retorna valor, apenas mostra o resultado da análise.
def consultar_risco_rota():
    print("\n--- Consultar risco da rota ---")

    if len(rotas_cadastradas) == 0:
        print("Nenhuma rota cadastrada ainda.")
        return

    for i, rota in enumerate(rotas_cadastradas):
        print(f"{i + 1} - {rota['origem']} para {rota['destino']} | Dia {rota['dia']}")

    try:
        escolha = int(input("Escolha o número da rota que deseja analisar: "))
    except ValueError:
        print("Erro: digite apenas números.")
        return

    if escolha < 1 or escolha > len(rotas_cadastradas):
        print("Erro: rota não encontrada.")
        return

    rota_escolhida = rotas_cadastradas[escolha - 1]

    sinal, recomendacao, motivos, pontos_risco = analisar_risco_transporte(rota_escolhida)

    clima = buscar_clima_por_dia(rota_escolhida["dia"])

    print("\n--- Resultado da análise ---")
    print(f"Produtor/Empresa: {rota_escolhida['produtor']}")
    print(f"Rota: {rota_escolhida['origem']} para {rota_escolhida['destino']}")
    print(f"Dia do transporte: {rota_escolhida['dia']}")
    print(f"Temperatura: {clima['temperatura']}°C")
    print(f"Umidade: {clima['umidade']}%")
    print(f"Previsão de chuva: {'Sim' if clima['previsao_chuva'] else 'Não'}")
    print(f"Vento: {clima['vento']} km/h")
    print(f"Sinal de risco: {sinal}")
    print(f"Recomendação: {recomendacao}")

    if sinal != "VERDE":
        melhor_dia = sugerir_melhor_dia(rota_escolhida)

        if melhor_dia is not None:
            print("\n--- Sugestão de reagendamento ---")
            print(f"Melhor dia nos próximos 7 dias: Dia {melhor_dia['dia']}")
            print(f"Sinal previsto: {melhor_dia['sinal']}")
            print(f"Pontuação de risco: {melhor_dia['pontos_risco']}")
            print(f"Recomendação: {melhor_dia['recomendacao']}")
        else:
            print("\nNão há dados climáticos disponíveis para os próximos 7 dias.")

    if len(motivos) > 0:
        print("\nMotivos do risco:")
        for motivo in motivos:
            print(f"- {motivo}")

# Finalidade: exibir os dados climáticos fictícios usados pelo sistema.
# Parâmetros: não recebe parâmetros.
# Retorno: não retorna valor, apenas mostra os dados na tela.
def listar_previsao_climatica():
    print("\n--- Previsão climática do mês de junho ---")

    for clima in dados_climaticos:
        chuva = "Sim" if clima["previsao_chuva"] else "Não"

        print(f"Dia {clima['dia']} de {clima['mes']} | "
            f"Temperatura: {clima['temperatura']}°C | "
            f"Umidade: {clima['umidade']}% | "
            f"Previsão de chuva: {chuva} | "
            f"Vento: {clima['vento']} km/h")

# Finalidade: listar todas as rotas cadastradas pelo usuário.
# Parâmetros: não recebe parâmetros.
# Retorno: não retorna valor, apenas exibe as rotas cadastradas.
def listar_rotas():
    print("\n--- Rotas cadastradas ---")

    if len(rotas_cadastradas) == 0:
        print("Nenhuma rota cadastrada ainda.")
        return

    for i, rota in enumerate(rotas_cadastradas):
        fim_safra = "Sim" if rota["fim_safra"] == "S" else "Não"

        print(f"\nRota {i + 1}")
        print(f"Produtor/Empresa: {rota['produtor']}")
        print(f"Origem: {rota['origem']}")
        print(f"Destino: {rota['destino']}")
        print(f"Dia do transporte: {rota['dia']}")
        print(f"Fim de safra: {fim_safra}")

# Finalidade: exibir o menu principal e controlar a navegação do sistema.
# Parâmetros: não recebe parâmetros.
# Retorno: não retorna valor, apenas mantém o programa funcionando até o usuário sair.
def menu():
    while True:
        print("\n===== MENU MINO =====")
        print("1 - Ver descrição da solução")
        print("2 - Cadastrar rota de transporte")
        print("3 - Consultar risco de uma rota")
        print("4 - Ver previsão climática do mês de junho")
        print("5 - Listar rotas cadastradas")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            mostrar_descricao()

        elif opcao == "2":
            cadastrar_rota()

        elif opcao == "3":
            consultar_risco_rota()

        elif opcao == "4":
            listar_previsao_climatica()

        elif opcao == "5":
            listar_rotas()

        elif opcao == "0":
            print("Encerrando o sistema Mino. Até mais!")
            break

        else:
            print("Opção inválida. Tente novamente.")

menu()