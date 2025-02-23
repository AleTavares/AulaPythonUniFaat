# Utilizando Operadores de Comparação

# Solicita dois números ao usuário
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Verifica se os números são iguais
if num1 == num2:
    print(f"Os números {num1} e {num2} são iguais.")
else:
    print(f"Os números {num1} e {num2} são diferentes.")

# Verifica se o primeiro número é maior que o segundo
if num1 > num2:
    print(f"O número {num1} é maior que o número {num2}.")
else:
    print(f"O número {num1} não é maior que o número {num2}.")

# Verifica se o primeiro número é menor que o segundo
if num1 < num2:
    print(f"O número {num1} é menor que o número {num2}.")
else:
    print(f"O número {num1} não é menor que o número {num2}.")

# Verifica se o primeiro número é maior ou igual ao segundo
if num1 >= num2:
    print(f"O número {num1} é maior ou igual ao número {num2}.")
else:
    print(f"O número {num1} não é maior ou igual ao número {num2}.")

# Verifica se o primeiro número é menor ou igual ao segundo
if num1 <= num2:
    print(f"O número {num1} é menor ou igual ao número {num2}.")
else:
    print(f"O número {num1} não é menor ou igual ao número {num2}.")