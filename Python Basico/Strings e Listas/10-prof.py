lim = 1000
lista = [0]*1000
qtd = 0
tamanho = 0

num = int(input("Número: "))
while (num < 0):
    num = int(input("Número: "))
    
while num >= 0 and (tamanho < lim):
    tamanho += 1
    if (num > 9) and (num < 100):
        lista[qtd] = num
        qtd += 1     
    num = int(input("Número: "))
if num >= 0:
    print('qtd máxima atingida! Removemos o último número digitado.')

tamanho = len(lista)
for i in range(qtd-1,-1, -1):
    print(lista[i])
    
# Não poderemos usar inversão de lista. A maneira de inverter lista usando o for, como por exemplo acima, é permitida
