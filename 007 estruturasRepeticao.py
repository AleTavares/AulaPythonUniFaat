# Estruturas de Repetição

# Programa que utiliza a estrutura de repetição for para imprimir os números de 1 a 10 na tela
for i in range(1, 11):
    print(i)

print()  # Linha em branco para separar os dois programas

# Programa que utiliza a estrutura de repetição while para imprimir os números pares de 1 a 20 na tela
num = 1
while num <= 20:
    if num % 2 == 0:
        print(num)
    num += 1