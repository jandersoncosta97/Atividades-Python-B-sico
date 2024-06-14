menor = float(input(f"1° número: "))
qtd = 3
for i in range(1, qtd):
    num = float(input(f"{i+1}° número: "))
    if num < menor:
        menor = num
    else:
        menor = menor
print(f"Menor número: {menor}")

