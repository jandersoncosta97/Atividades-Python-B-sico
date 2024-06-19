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
            dezena_ = 5
        if dezena >= dezena_:
            if dezena-dezena_ == 4:
                romano += 'XC'
            elif dezena-dezena_ <= 3:
                romano += 'L'
                romano += 'X'*(dezena-dezena_)
        else:
            if dezena == 4:
                romano += 'XL'
            else:
                romano += 'X'*dezena
            
    if dezena <= 3:
        romano += 'I'*i
    elif dezena == 4:
        romano += 'IV'
    elif dezena >= 5:
        i_ = 5
        if dezena == 5:
            romano += 'V'
        elif dezena-i_ == 4:
            romano += 'IX'
        elif dezena-i_ <= 3:
            romano += 'V'
            romano += 'I'*(dezena-i_)

    print(f'O número {x} em algarismo romano é {romano}')
    