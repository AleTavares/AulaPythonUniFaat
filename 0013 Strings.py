# Strings em Python são sequências de caracteres usadas para armazenar e manipular texto.
# Elas são imutáveis, o que significa que uma vez criadas, não podem ser alteradas.
# Strings podem ser criadas usando aspas simples, aspas duplas ou triplas aspas.

# Criação de uma string com uma frase longa
frase_longa = "A programação é uma habilidade essencial no mundo moderno, permitindo a automação de tarefas e a criação de soluções inovadoras."

# Imprimir o número de caracteres na string
numero_de_caracteres = len(frase_longa)
print(f"Número de caracteres na string: {numero_de_caracteres}")

# Imprimir a string em letras maiúsculas
print("String em letras maiúsculas:")
print(frase_longa.upper())

# Imprimir a string em letras minúsculas
print("String em letras minúsculas:")
print(frase_longa.lower())

# Verificar se uma determinada palavra está presente na string
palavra = "automação"
if palavra in frase_longa:
    print(f"A palavra '{palavra}' está presente na string.")
else:
    print(f"A palavra '{palavra}' não está presente na string.")