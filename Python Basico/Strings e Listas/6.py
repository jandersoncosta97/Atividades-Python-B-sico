N = int(input("Digite o valor de N: "))
lista1 = [None]*N
lista2 = []
lista3 = []

for i in range(N):
    num = int(input(f"Digite o {i+1}° número inteiro: "))
    lista1[i] = num
    if num%2 == 0:
        lista2.append(num)
    elif num%2 == 1:
        lista3.append(num)

print(f"Lista original: {lista1}\nLista com números pares: {lista2}\nLista com números ímpares: {lista3}")
