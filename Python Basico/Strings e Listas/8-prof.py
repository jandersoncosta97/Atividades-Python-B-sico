rom = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
       (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
       (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]

num = aux = int(input("Número: "))
while (num < 1) or (num > 3999):
    num = aux = int(input("Erro. Número: "))
res = ''

for t in rom:
    while aux >= t[0]:
        res = res + t[1]
        aux = aux - t[0]

print(num, "em romanos é", res)
