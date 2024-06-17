n1 = int(input("N1: "))
while n1 < 1:
    n1 = int(input("N1: "))
n2 = int(input("N2: "))
while n2 < 1:
    n2 = int(input("N2: "))

mdc = n1
if n2 < mdc:
    mdc = n2

while ((n1 % mdc) != 0) or ((n2 % mdc) != 0):
    mdc -= 1

print("MDC=", mdc)
