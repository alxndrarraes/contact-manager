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