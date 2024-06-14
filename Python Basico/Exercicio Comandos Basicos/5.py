num = int(input("Digite o número para o cálculo de seu fatorial: "))
fatorial = num
for i in range(num-1, 1, -1):
    fatorial = fatorial*i

if num == 0:
    fatorial = 1
print(f"O fatorial de {num} é {fatorial}")



num = int(input("Digite o número para o cálculo de seu fatorial: "))
fatorial = num
i = num
while i >= 2:
    i -= 1
    fatorial = fatorial*i

if num == 0:
    fatorial = 1

print(f"O fatorial de {num} é {fatorial}")
