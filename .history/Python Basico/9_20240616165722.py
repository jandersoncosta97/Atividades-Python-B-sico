
N = int(input("Digite um número inteiro N: "))


sequencia = []

for i in range(N):
    if i % 2 == 0:  # Índices pares (0, 2, 4, ...)
        termo = -1 + (i // 2) * 6
    else:  # Índices ímpares (1, 3, 5, ...)
        termo = 0 + (i // 2) * 6
    print(termo)


