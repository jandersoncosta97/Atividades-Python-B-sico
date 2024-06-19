N = int(input("Digite um número inteiro positivo: "))
while N <= 0:
    N = int(input("O número precisa ser inteiro e positivo: "))

for i in range(N):
    x = int(input("range: (0 < x < 4000). x = "))
    while x <= 0 or x > 4000:
        x = int(input("Valor fora do range (0 < x < 4000). x = "))
    milar = x // 1000
    centena = (x % 1000) // 100
    dezena = (x % 100) // 10
    unidade = x % 10

    romano = ""
    for i in [milar, centena, dezena, unidade]:
        if i == milar:
            if i == 1:
                romano += 'M'*i
            elif i == 2:
                romano += 'M'*i
            elif i == 3:
                romano += 'M'*i
        if i == centena:
            i_ = 5
            if i >= i_:
                if i-i_ == 4:
                    romano += 'CM'
                elif (i-i_) <= 3:
                    romano += 'D'
                    romano += 'C'*(i-i_)
            else:
                if i == 4:
                    romano += 'CD'
                else:
                    romano += 'C'*i
        if i == dezena:
            c = dezena
            c_ = 5
            if c >= c_:
                if b-b_ == 4:
                    romano += 'XC'
                elif b-b_ <= 3:
                    romano += 'L'
                    romano += 'X'*(b-b_)
            else:
                if c == 4:
                    romano += 'XL'
                else:
                    romano += 'X'*c
        if i == unidade:
            d = unidade
            if d <= 3:
                romano += 'I'*d
            elif d == 4:
                romano += 'IV'
            elif d >= 5:
                d_ = 5
                if d == 5:
                    romano += 'V'
                elif d-d_ == 4:
                    romano += 'IX'
                elif d-d_ <= 3:
                    romano += 'V'
                    romano += 'I'*(d-d_)

    print(f'O número {x} em algarismo romano é {romano}')
    