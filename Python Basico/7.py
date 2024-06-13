lim1 = int(input("Digite o número inteiro: "))
lim2 = int(input("Digite o número inteiro: "))

if lim1 < lim2:
    if lim1%2 == 0:
        lim1 = lim1+1
    if lim2%2 == 0:
        lim2 = lim2-1
    else:
        lim1 = lim1
        lim2 = lim2
 
elif lim1 > lim2:
    lim1, lim2 = lim2, lim1
    if lim1%2 == 0:
        lim1 = lim1+1
    if lim2%2 == 0:
        lim2 = lim2-1
    else:
        lim1 = lim1
        lim2 = lim2
    
else:
    print("Os limites são iguais")

for i in range(lim1, lim2+1, 2):
    print(i)
