class GerenciadorDeContatos:
    def __init__(self):
        self.contatos = {}

    def adicionar_contato(self, nome, numero_telefone):
        self.contatos[nome] = numero_telefone

    def listar_contatos(self):
        return self.contatos

    def remover_contato(self, nome):
        del self.contatos[nome]

def main():
    gerenciador_contatos = GerenciadorDeContatos()

    while True:
        print("\nEscolha uma opção:")
        print("1. Adicionar contato")
        print("2. Listar contatos")
        print("3. Remover contato")
        print("4. Sair")

        escolha = input("Digite o número da opção desejada: ")

        if escolha == '1':
            nome = input("Digite o nome do contato: ")
            numero_telefone = input("Digite o número de telefone: ")
            gerenciador_contatos.adicionar_contato(nome, numero_telefone)
        elif escolha == '2':
            print("Lista de contatos:")
            for nome, numero_telefone in gerenciador_contatos.listar_contatos().items():
                print(f"Nome: {nome}, Telefone: {numero_telefone}")
        elif escolha == '3':
            nome = input("Digite o nome do contato que deseja remover: ")
            gerenciador_contatos.remover_contato(nome)
        elif escolha == '4':
            print("Encerrando...")
            break
        else:
            print("Opção inválida. Por favor, escolha novamente.")

if __name__ == "__main__":
    main()