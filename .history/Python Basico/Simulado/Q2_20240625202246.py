ma = 5 # 150
qtd = 0
qtd2d = 0
lis = [0]*ma
maior7 = -9999999999999999999999999999999

num = int(input("Número = "))
while num >= 0:
    num = int(input("Número = "))
    
while (num != 0) and (qtd < ma):
    qtd = qtd + 1
    if ((num % 5) == 0) and (num < -9) and (num > -100):
        lis[qtd2d] = num
        qtd2d = qtd2d+1
    if ((num > maior7) and ((num%7)) != 0):
        maior7 = num
        
    num = int(input("Número: "))
    while num > 0:
        num = int(input("Número: "))
        
if qtd > ma:
    print('Capacidade de armazenamento esgotada. ')

if qtd2d == 0:
    print("Nenhum número de 2 digitos digitado.")
else:
    lis = lis[:qtd2d]  # Maneira pythônica. Também é possível fazer usando loop 'for' (inverter uma lista usando loop 'for')
    lis.reverse()
    print("Lista com os números digitados entre -10 e -99{lis}")
if maior7 == -9999999999999999999999999999999:
    print('Nenhum número não multiplo de 7 digitado')
else:
    print('Maior número digitado não multiplo de 7 é', maior7)
    