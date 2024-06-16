
N = int(input("Digite um número inteiro N: "))



for i in range(N):
    if i % 2 == 0:
        termo = -1 + (i // 2) * 6
    else:
        termo = 0 + (i // 2) * 6
    print(termo)


