# Dicionários em Python são coleções de pares chave-valor. Cada chave é única e mapeia para um valor.
# Eles são úteis para armazenar dados que precisam ser associados a identificadores únicos.

# Criação do dicionário com informações sobre um aluno
aluno = {
    "nome": "João",
    "idade": 20,
    "notas": [7.5, 8.0, 9.0]
}

# Impressão do nome e idade do aluno
print(f"Nome: {aluno['nome']}")
print(f"Idade: {aluno['idade']}")

# Adicionando uma nova nota ao dicionário
aluno["notas"].append(8.5)
print(f"Notas atualizadas: {aluno['notas']}")

# Removendo uma nota existente
aluno["notas"].remove(7.5)
print(f"Notas após remoção: {aluno['notas']}")

# Verificando se uma determinada chave está presente no dicionário
chave = "idade"
if chave in aluno:
    print(f"A chave '{chave}' está presente no dicionário.")
else:
    print(f"A chave '{chave}' não está presente no dicionário.")