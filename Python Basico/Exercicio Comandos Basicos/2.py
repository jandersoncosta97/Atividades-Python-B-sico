num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))

if num2 != 0:
    if num1%num2 == 0:
        print(num1)
    else:
        print((num1%num2)**2)
else:
    print("Não é possível dividir por zero")
