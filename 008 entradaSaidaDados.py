# Entrada e saída de dados
# Aprenda a solicitar dados ao usuário e a ler arquivos de texto em Python.

# Programa que solicita o nome e a idade do usuário e imprime uma mensagem personalizada
def solicitar_dados_usuario():
    nome = input("Digite seu nome: ")
    idade = input("Digite sua idade: ")
    print(f"Olá {nome}, você tem {idade} anos.")

# Programa que lê um arquivo de texto e imprime o seu conteúdo na tela
def ler_arquivo_texto(caminho_arquivo):
    try:
        with open(caminho_arquivo, 'r') as arquivo:
            conteudo = arquivo.read()
            print(conteudo)
    except FileNotFoundError:
        print(f"O arquivo {caminho_arquivo} não foi encontrado.")

# Chamada das funções
if __name__ == "__main__":
    solicitar_dados_usuario()
    caminho_arquivo = input("Digite o caminho do arquivo de texto que deseja ler: ")
    ler_arquivo_texto(caminho_arquivo)