"""
def serie (n):
    num1 = 3
    num2 = 5
    den = 1
    res = 0
    for i in range(1, n+1):
        if (i % 2) == 1:
            res = res + num1/den
            num1 = num1*5
        else:
            res = res - num2/den
            num2 = num2*6
        den = den*(i+1)
    return res

num = int(input("Número = "))
while num > 0:
    r = serie(num)
    print(f'Série com {num} termos é {r}')
    num = int(input("Número = "))
"""
    
# Usando recursão

def serieR(n, num1 = 3, num2 = -5, den = 1, pm = 2):
    if n == 1:
        if (pm%2) == 0:
            res = num1/den
        else:
            res = num2/den
    else:
        if (pm % 2) == 0:
            res = num1/den + serieR(n-1, num1*5, num2, den*pm, pm+1)
        else:
            res = num2/den + serieR(n-1, num1, num2*6, den*pm, pm+1)
    return res            

num = int(input("Número = "))
while num < 1:
    num = int(input("Número = "))
    
while num > 0:
    r = serieR(num)
    print("A soma da série com", num, "termos é", r)
    num = int(input("Número = "))
    