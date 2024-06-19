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

    if milar == 1:
        romano += 'M'*milar
    elif milar == 2:
        romano += 'M'*milar
    elif milar == 3:
        romano += 'M'*milar
        
    centena_ = 5
    if centena >= centena_:
        if centena-centena_ == 4:
            romano += 'CM'
        elif (centena-centena_) <= 3:
            romano += 'D'
            romano += 'C'*(centena-centena_)
        else:
            if centena == 4:
                romano += 'CD'
            else:
                romano += 'C'*centena
        if i == dezena:
            i_ = 5
            if i >= i_:
                if i-i_ == 4:
                    romano += 'XC'
                elif i-i_ <= 3:
                    romano += 'L'
                    romano += 'X'*(i-i_)
            else:
                if i == 4:
                    romano += 'XL'
                else:
                    romano += 'X'*i
        if i == unidade:
            if i <= 3:
                romano += 'I'*i
            elif i == 4:
                romano += 'IV'
            elif i >= 5:
                i_ = 5
                if i == 5:
                    romano += 'V'
                elif i-i_ == 4:
                    romano += 'IX'
                elif i-i_ <= 3:
                    romano += 'V'
                    romano += 'I'*(i-i_)

    print(f'O número {x} em algarismo romano é {romano}')
    