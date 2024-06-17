n1 = int(input("N1: "))
while n1 < 1:
    n1 = int(input("N1: "))
n2 = int(input("N2: "))
while n2 < 1:
    n2 = int(input("N2: "))
if n1 > n2:
    n1, n2 = n2, n1
mmc = n2

while ((mmc % n1) != 0):
    mmc += n2

print("mmc=", mmc)
