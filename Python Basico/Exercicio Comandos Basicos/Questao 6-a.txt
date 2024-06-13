# -------------------- Letra a ---------------------------

# for

N = int(input("Digite o número de termos: "))
while N < 0:
    N = int(input("Digite um número maior ou igual a zero: "))

numerador = 1

soma = 0
for denominador in range(1,N+1):
    soma += (numerador)/denominador
    numerador += 2
print(f"A soma da sequência de {N} termos (letra a) é {soma}")




# while
N = int(input("Digite o número de termos: "))
while N < 0:
    N = int(input("Digite um número maior ou igual a zero: "))


numerador = 1
denominador = 1

soma = 0
while numerador <= (2*N-1) and denominador <= N:
    soma += numerador/denominador
    numerador += 2
    denominador += 1

print(f"A soma da sequência de {N} termos (letra a) é {soma}")
