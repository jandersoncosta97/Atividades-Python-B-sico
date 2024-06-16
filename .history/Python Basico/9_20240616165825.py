
N = int(input("Digite um número inteiro N: "))



for i in range(N):
    if i % 2 == 0:
        termo = -1 + (i // 2) * 6
    else:
        termo = 0 + (i // 2) * 6

print(f"O n-ésimo termo da sequência [-1, 0, 5, 6, 11, 12, 17, 18, ...] é {termo}")
