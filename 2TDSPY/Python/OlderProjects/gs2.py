# Função para validar a entrada do usuário
def validar_entrada(opcoes):
    while True:
        escolha = input("Escolha uma opção: ")
        if escolha in opcoes:
            return escolha
        else:
            print("Opção inválida, tente novamente.")

# Função para cadastrar um novo usuário
def cadastrar_usuarios(usuarios):
    while True:
        nome = input("Digite seu nome: ").strip()
        email = input("Digite seu email: ").strip()
        senha = input("Digite uma senha: ").strip()
        if nome and email and senha:
            usuarios.append({'nome': nome, 'email': email, 'senha': senha})
            print("Cadastro realizado com sucesso!")
            break
        else:
            print("Todos os campos são obrigatórios. Tente novamente.")

# Função para realizar login
def realizar_login(usuarios):
    email = input("Digite seu email: ").strip()
    senha = input("Digite sua senha: ").strip()
    for usuario in usuarios:
        if usuario['email'] == email and usuario['senha'] == senha:
            print(f"Bem-vindo(a), {usuario['nome']}!")
            return True
    print("Email ou senha incorretos. Tente novamente.")
    return False

# Função para escolher um plano mensal
def escolher_plano(planos):
    print("Planos disponíveis:")
    for idx, plano in enumerate(planos):
        print(f"{idx + 1} - {plano['nome']} - R$ {plano['preco']}")
    escolha = validar_entrada([str(i + 1) for i in range(len(planos))])
    return planos[int(escolha) - 1]

# Função para escolher uma praia famosa
def escolher_praia(praias):
    print("Praias disponíveis:")
    for idx, praia in enumerate(praias):
        print(f"{idx + 1} - {praia}")
    escolha = validar_entrada([str(i + 1) for i in range(len(praias))])
    return praias[int(escolha) - 1]

# Menu principal
def menu():
    usuarios = []
    planos = [
        {'nome': 'Plano Comunitário', 'preco': 50},
        {'nome': 'Plano Individual', 'preco': 200}
    ]
    praias = ['Copacabana', 'Ipanema', 'Praia do Forte', 'Praia de Pipa']

    while True:
        print("\nMenu Inicial:")
        print("1 - Cadastrar Usuário")
        print("2 - Login")
        print("3 - Sair")
        
        opcao = validar_entrada(['1', '2', '3'])
        
        if opcao == '1':
            cadastrar_usuarios(usuarios)
        elif opcao == '2':
            if realizar_login(usuarios):
                break
        elif opcao == '3':
            print("Saindo do programa.")
            return

    while True:
        print("\nMenu Principal:")
        print("1 - Escolher Plano Mensal")
        print("2 - Escolher Praia para Limpeza")
        print("3 - Sair")
        
        opcao = validar_entrada(['1', '2', '3'])
        
        if opcao == '1':
            plano_escolhido = escolher_plano(planos)
            print(f"Plano escolhido: {plano_escolhido['nome']} - R$ {plano_escolhido['preco']}")
        elif opcao == '2':
            praia_escolhida = escolher_praia(praias)
            print(f"Praia escolhida para limpeza: {praia_escolhida}")
        elif opcao == '3':
            print("Saindo do programa.")
            break

if _name_ == "_main_":
    menu()