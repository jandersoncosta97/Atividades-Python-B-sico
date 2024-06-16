# Usando for

N = int(input("Digite o valor de N: "))
r = 6

if N%2 == 0:
    a0 = -1
    for i in range(a0, a0+(r*(N+1))/2+1, 2):
        if i == a0+(r*(N+1)):
            print(i)
elif N%2 != 0:
    a0 = 0
    for i in range(a0, a0+(r*(N+1))/2+1, 2):
        if i == i == a0+(r*(N+1)):
            print(i)

# Usando while

if N%2 == 0:
    i = -1
    while i != i+(r*(N+1))/2:
        i += 6
    print(i)
    
elif N%2 != 0:
    i = 0
    while i != i+(r*(N+1))/2:
        i += 6
    print(i)