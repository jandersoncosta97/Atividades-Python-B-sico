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
    
def separa(num1):
    l = []
    while num1 > 0:
        v = num1 % 10
        num1 = num1 // 10
        l.insert(0, v)
        print("Desmembrando: ", num1, l)
    return l


def juntar(lista):
    a = 1
    v = 0
    for i in lista:
        v += i*(10**(len(lista)-a))
        a += 1
    return v

def listar_numeros(nu):
    numero = 0
    numeros = []
    for i in range(100, nu+1, 1):
        lista = separa(i)
        if lista == lista[::-1]:
            numero = juntar(lista)
            numeros.append(numero)
    return numeros

n = int(input("Digite um número inteiro positivo (0 < num < 99999): "))
while n > 99999:
    n = int(input("Digite um número inteiro positivo (0 < num < 99999): "))
while n > 0:
    res = listar_numeros(n)
    print("Lista palíndromos entre 100 e", n, ":" ,res)
    n = int(input("Digite um número inteiro positivo (0 < num < 99999): "))
    while n > 99999:
        n = int(input("Digite um número inteiro positivo (0 < num < 99999): "))
    