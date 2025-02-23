# List comprehension é uma maneira concisa de criar listas em Python.
# Utiliza uma única linha de código para definir uma nova lista, 
# aplicando uma expressão a cada item de uma sequência ou iterável.

# Lista com os números pares de 1 a 20 utilizando list comprehension
numeros_pares = [x for x in range(1, 21) if x % 2 == 0]

# Lista com o quadrado de cada número de 1 a 10 utilizando list comprehension
quadrados = [x**2 for x in range(1, 11)]

print("Números pares de 1 a 20:", numeros_pares)
print("Quadrados de 1 a 10:", quadrados)