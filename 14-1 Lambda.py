# Uma função lambda é uma pequena função anônima definida usando a palavra-chave 'lambda'.
# Elas podem ter qualquer número de argumentos, mas apenas uma expressão.
# A expressão é avaliada e retornada quando a função é chamada.


# Exemplo de utilização de função lambda em Python

# Função lambda para adicionar 10 a um número
soma_10 = lambda x: x + 10
print(soma_10(5))  # Saída: 15

# Função lambda para multiplicar dois números
multiplica = lambda x, y: x * y
print(multiplica(4, 5))  # Saída: 20

# Função lambda para inverter uma string
inverte_string = lambda s: s[::-1]
print(inverte_string("lambda"))  # Saída: "adbmal"

# Função lambda para filtrar números pares de uma lista
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # Saída: [2, 4, 6, 8, 10]

# Função lambda para ordenar uma lista de tuplas pelo segundo elemento
tuplas = [(1, 2), (3, 1), (5, 4), (2, 3)]
tuplas_ordenadas = sorted(tuplas, key=lambda x: x[1])
print(tuplas_ordenadas)  # Saída: [(3, 1), (1, 2), (2, 3), (5, 4)]