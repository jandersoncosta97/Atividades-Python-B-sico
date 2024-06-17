N = int(input("Digite o número de alunos (uma nota final para cada aluno): "))
lista_notas = [None]*N
acima = []

soma = 0
for i in range(N):
    nota = float(input(f"Digite a nota do {i+1}° aluno: "))
    soma += nota
    lista_notas[i] = nota
media = soma/N

for i in lista_notas:
    if i > media:
        acima.append(i)

print(f"Notas acima de {media}: {acima}")
