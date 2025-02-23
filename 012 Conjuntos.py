# Conjuntos em Python são coleções não ordenadas de elementos únicos. Eles são úteis para realizar operações matemáticas como união, interseção e diferença.

# Definindo os conjuntos com nomes de alunos em duas turmas diferentes
turma1 = {"Ana", "Bruno", "Carlos", "Daniela", "Eduardo"}
turma2 = {"Carlos", "Fernanda", "Gabriel", "Helena", "Ana"}

# Encontrando os alunos que estão presentes em ambas as turmas
alunos_em_ambas = turma1.intersection(turma2)
print("Alunos presentes em ambas as turmas:", alunos_em_ambas)

# Encontrando os alunos que estão presentes apenas na primeira turma
alunos_somente_turma1 = turma1.difference(turma2)
print("Alunos presentes apenas na primeira turma:", alunos_somente_turma1)

# Verificando se um determinado aluno está presente em um dos conjuntos
aluno = "Carlos"
presente_na_turma1 = aluno in turma1
presente_na_turma2 = aluno in turma2
print(f"O aluno {aluno} está presente na turma 1?", presente_na_turma1)
print(f"O aluno {aluno} está presente na turma 2?", presente_na_turma2)