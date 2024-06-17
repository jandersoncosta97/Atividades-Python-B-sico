num = int(input("Digite um número: "))
soma = 0
for i in range(1, num, 1):
    if num%i == 0:
        soma += i
if soma == num:
    print("O número",num,"é perfeito.")
else:
    print("O número",num,"não é perfeito.")
