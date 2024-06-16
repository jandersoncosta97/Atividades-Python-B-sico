# Ler o número inteiro N
N = int(input("Digite um número inteiro N: "))

# Inicializar a sequência
sequencia = []

# Construir a sequência até o N-ésimo termo
for i in range(N):
    if i % 2 == 0:  # Índices pares (0, 2, 4, ...)
        termo = -1 + (i // 2) * 6
    print(termo)
    else:  # Índices ímpares (1, 3, 5, ...)
        termo = 0 + (i // 2) * 6
    print(termo)

# O N-ésimo termo está no índice N-1 (pois os índices começam em 0)
print(f"O {N}-ésimo termo da sequência é: {sequencia[N-1]}")
