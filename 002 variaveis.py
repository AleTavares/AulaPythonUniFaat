# Declaração de variáveis de diferentes tipos
inteiro = 10
flutuante = 3.14
string = "Olá, mundo!"
booleano = True

# Imprimindo os valores das variáveis utilizando diferentes métodos de formatação

# Usando vírgulas
print("Valor do inteiro:", inteiro)
print("Valor do flutuante:", flutuante)
print("Valor da string:", string)
print("Valor do booleano:", booleano)

# Usando o operador de formatação %
print("Valor do inteiro: %d" % inteiro)
print("Valor do flutuante: %.2f" % flutuante)
print("Valor da string: %s" % string)
print("Valor do booleano: %s" % booleano)

# Usando o método format()
print("Valor do inteiro: {}".format(inteiro))
print("Valor do flutuante: {:.2f}".format(flutuante))
print("Valor da string: {}".format(string))
print("Valor do booleano: {}".format(booleano))

# Usando f-strings (Python 3.6+)
print(f"Valor do inteiro: {inteiro}")
print(f"Valor do flutuante: {flutuante:.2f}")
print(f"Valor da string: {string}")
print(f"Valor do booleano: {booleano}")