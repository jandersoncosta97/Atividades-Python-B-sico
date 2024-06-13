soma = 0
qtd = 3
for i in range(qtd):
    a = float(input("Digite o número: "))
    print(f"{i+1}° número: {a}")
    soma += a
media = soma/qtd
print(f"A média é: {media}")
