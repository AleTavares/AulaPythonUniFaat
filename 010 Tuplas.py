# Tuplas são coleções ordenadas e imutáveis em Python. Elas são usadas para agrupar dados.
# Uma vez criada, uma tupla não pode ser modificada (adicionar, remover ou alterar elementos).

# Criando uma tupla com informações sobre um livro
livro = ("O Senhor dos Anéis", "J.R.R. Tolkien", 1954)

# Imprimindo cada informação do livro em uma linha separada
print("Título:", livro[0])
print("Autor:", livro[1])
print("Ano de Publicação:", livro[2])

# Tentando modificar um elemento da tupla
try:
    livro[1] = "George R.R. Martin"
except TypeError as e:
    print("Erro ao tentar modificar a tupla:", e)