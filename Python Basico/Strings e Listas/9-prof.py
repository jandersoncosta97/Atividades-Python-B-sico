lista = []

num = int(input("Número: "))
while num < 0:
    num = int(input("Número: "))
    
while num >= 0:
    if (num > 9) and (num < 100):
        lista.append(num)        
    num = int(input("Número: "))

tamanho = len(lista)
for i in range(tamanho-1,- 1, -1):
    print(lista[i])
    
# Não poderemos usar inversão de lista. A maneira de inverter lista usando o for, como por exemplo acima, é permitida
