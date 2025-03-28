
import os

# Função para limpar a tela do console
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Função para exibir o menu principal
def display_menu():
    clear_screen()
    print("Bem-vindo ao Portal AutoCare - Porto Seguro")
    print("Selecione uma opção:")
    print("1. Catálogo de Peças")
    print("2. Oficinas Próximas")
    print("3. Chatbot de Diagnóstico")
    print("0. Sair")

# Função para o Catálogo de Peças
def catalogo_pecas():
    # Aqui vamos incluir a lógica para exibir e/ou comprar peças
    print("Catálogo de Peças")

# Função para as Oficinas Próximas
def oficinas_proximas():
    # Aqui vamos incluir a lógica para encontrar oficinas próximas
    print("Oficinas Próximas")

# Função para o Chatbot de Diagnóstico
def chatbot_diagnostico():
    # Aqui vamos incluir a lógica para o chatbot de diagnóstico
    print("Chatbot de Diagnóstico")

# Função principal
def main():
    while True:
        display_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            catalogo_pecas()
        elif opcao == "2":
            oficinas_proximas()
        elif opcao == "3":
            chatbot_diagnostico()
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            input("Opção inválida! Pressione Enter para continuar.")

if __name__ == "__main__":
    main()
