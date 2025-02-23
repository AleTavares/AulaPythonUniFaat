# Programa para realizar operações aritméticas básicas

# Solicita dois números ao usuário
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Realiza as operações aritméticas
soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2 #if num2 != 0 else "Indefinida (divisão por zero)"

# Imprime os resultados das operações
print(f"A soma de {num1} e {num2} é: {soma}")
print(f"A subtração de {num1} e {num2} é: {subtracao}")
print(f"A multiplicação de {num1} e {num2} é: {multiplicacao}")
print(f"A divisão de {num1} por {num2} é: {divisao}")