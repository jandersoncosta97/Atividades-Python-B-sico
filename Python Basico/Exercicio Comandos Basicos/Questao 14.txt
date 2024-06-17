from math import sqrt
n = int(input("N1: "))
while n < 2:
    n = int(input("N1: "))

raiz = int(sqrt(n))
d = 2
while (d <= raiz) and ((n % d) != 0):
    d += 1

if d > raiz:
    print(n, "é primo")
else:
    print(n, "não é primo.", d, "é um divisor.")
