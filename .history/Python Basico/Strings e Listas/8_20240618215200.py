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
        
    if unidade <= 3:
        romano += 'I'*unidade
    elif unidade == 4:
        romano += 'IV'
    elif unidade >= 5:
        unidade_ = 5
        if unidade == 5:
            romano += 'V'
        elif unidade-unidade_ == 4:
            romano += 'IX'
        elif unidade-unidade_ <= 3:
            romano += 'V'
            romano += 'I'*(unidade-unidade_)

    print(f'O número {x} em algarismo romano é {romano}')
    