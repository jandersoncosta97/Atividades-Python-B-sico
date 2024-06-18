"""
def contagem(nu):
    l = []
    total = 0
    str_nu = str(nu)
    for i in range(100, int(str_nu)+1, 1):
        i = str(i)
        if (i[::-1]) == (i):
            l.append(i)
            total += 1
    return total, l

num = int(input("N = "))
while num < 100:
    num = int(input("N = "))
while num > 100:
    print(contagem(num))
    num = int(input("N = "))
    while num < 100:
        num = int(input("N = "))
""" 
    
def separa(num):
    l = []
    while num > 0:
        v = num % 10
        num = num // 10
        l.insert(0, v)
        print("Desmembrando: ", num, l)
    return l

def contagem(nu, numero = 9):
    li = separa(nu)
    r = 0
    for e in li:
        if e == numero:
            r = r + 1
    return r

n = int(input("Digite um número inteiro positivo (0 < num < 99999): "))
while n > 99999:
    n = int(input("Digite um número inteiro positivo (0 < num < 99999): "))
while n > 0:
    res = contagem(n)
    print(n, res)
    n = int(input("Digite um número inteiro positivo (0 < num < 99999): "))
    while n > 99999:
        n = int(input("Digite um número inteiro positivo (0 < num < 99999): "))
    