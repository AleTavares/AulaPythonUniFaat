# Exemplos de operações com listas em Python
# Listas em Python são coleções ordenadas e mutáveis que permitem armazenar múltiplos itens em uma única variável.
# Elas são definidas usando colchetes [] e os itens são separados por vírgulas.

# Criação da lista com nomes de frutas
frutas = ["maçã", "banana", "laranja", "uva", "manga"]

# Impressão do primeiro e do último elemento da lista
print("Primeiro elemento:", frutas[0])
print("Último elemento:", frutas[-1])

# Adição de um novo elemento à lista
frutas.append("abacaxi")
print("Lista após adicionar um novo elemento:", frutas)

# Remoção de um elemento existente da lista
frutas.remove("laranja")
print("Lista após remover um elemento:", frutas)

# Ordenação da lista em ordem alfabética
frutas.sort()
print("Lista ordenada:", frutas)

# Verificação se um determinado elemento está presente na lista
elemento = "banana"
if elemento in frutas:
    print(f"{elemento} está presente na lista.")
else:
    print(f"{elemento} não está presente na lista.")