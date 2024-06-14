# solução usando for
N = int(input("Digite o número de termos: "))

soma = 0
i = 1
for a in range(38, (38-N), -1):
    soma += ((a-1)*a)/i
    i += 1
print(f"A soma da sequência é {soma}")


# solução usando while
N = int(input("Digite o número de termos: "))

soma = 0
i = 1
a = 38
while a > 38-N:
    soma += ((a-1)*a/i)
    i += 1
    a -= 1
print(f"A soma da sequência é {soma}")
