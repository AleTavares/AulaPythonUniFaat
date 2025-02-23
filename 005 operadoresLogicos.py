# Utilizando comparadores Lógicos

# Solicita dois valores booleanos ao usuário
valor1 = input("Digite o primeiro valor booleano (True/False): ")
valor2 = input("Digite o segundo valor booleano (True/False): ")

# Converte as entradas para booleanos
valor1 = valor1 == "True"
valor2 = valor2 == "True"

# Realiza operações lógicas
resultado_and = valor1 and valor2
resultado_or = valor1 or valor2
resultado_not_valor1 = not valor1
resultado_not_valor2 = not valor2

# Imprime os resultados das operações lógicas
print(f"{valor1} AND {valor2} = {resultado_and}")
print(f"{valor1} OR {valor2} = {resultado_or}")
print(f"NOT {valor1} = {resultado_not_valor1}")
print(f"NOT {valor2} = {resultado_not_valor2}")