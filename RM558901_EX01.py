# Definição de variáveis
votos = {'segunda-feira': 0, 'terça-feira': 0, 'quarta-feira': 0, 'quinta-feira': 0, 'sexta-feira': 0}
acesso_liberado = False
total_colaboradores = 0


# Função para realizar a votação
def realizar_votacao():
    global total_colaboradores
    global acesso_liberado
    contador_votos = 0
    senha_admin = "BIDU"

    while True:
        usuario = input("Se você é o administrador, digite ADMINISTRADOR para liberar a votação."
                        "Se você é um colaborador, digite seu nome: ")
        if usuario.upper() == "ADMINISTRADOR":
            senha = input("Digite a senha do administrador da empresa BIDU: ")
            if senha.upper() == senha_admin:
                total_colaboradores = int(input("Quantos colaboradores irão participar da votação? "))
                acesso_liberado = True
                print("Acesso liberado para os outros usuários.")
            else:
                print("Senha incorreta. Acesso negado.")
                continue
        elif not acesso_liberado:
            print("Esperando o administrador liberar a votação.")
            continue
        else:
            print("Dias disponíveis para votação: segunda-feira, terça-feira, quarta-feira, quinta-feira, sexta-feira.")
            voto = input("Qual dia da semana é o melhor para realizar a live? ").lower()
            if voto in votos:
                votos[voto] += 1
                contador_votos += 1
                print(f"Obrigado pelo seu voto, {usuario}!")
            else:
                print("Dia inválido. Por favor, escolha um dia entre segunda-feira e sexta-feira.")
            if contador_votos >= total_colaboradores:
                break

    # Finalização da votação
    if acesso_liberado and contador_votos == total_colaboradores:
        print("Pesquisa finalizada, todos os colaboradores responderam à votação.")
        dia_escolhido = max(votos, key=votos.get)
        print(f"Ao final, o melhor dia para a realização das lives escolhido pelos colaboradores é: {dia_escolhido}.")


# Chamada da função para iniciar a votação
realizar_votacao()
