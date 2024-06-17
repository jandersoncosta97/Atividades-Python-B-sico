N = int(input("Digite o tamanho de cada vetor: "))

vetor1 = [""]*N
vetor2 = [""]*N
vetor3 = [""]*N

print("Primeiro vetor: ")
for i in range(N):
    num = int(input(f"Digite o {i+1}° número inteiro para o primeiro vetor: "))
    vetor1[i] = num

print("Segundo vetor: ")
for i in range(N):
    num = int(input(f"Digite o {i+1}° número inteiro para o segundo vetor: "))
    vetor2[i] = num

print("Vetor1: ", vetor1)
print("Vetor2: ", vetor2)

for chave1, i in enumerate(vetor1):
    for chave2, j in enumerate(vetor2):
        if chave1 == chave2:
            vetor3[chave1] = int(i)+int(j) 
print(f"{vetor1} + {vetor2} = {vetor3}")
