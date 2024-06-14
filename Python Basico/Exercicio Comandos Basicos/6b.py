# # letra b
# # --------------------- Ajustar o valor da soma ------------------
# # Usando for

r = -10
N = int(input("Digite o número de termos para a sequência: "))

soma = 0
numerador = 2
for denominador in range(500, 500+r*(N-1)-1, r):
    if denominador != 0:
        soma += numerador/denominador
        print(f"{numerador}/{denominador}")
        if numerador == 2:
            numerador = -5
        else:
            numerador = 2



print("A soma da sequência é", soma)



# usando while

N = int(input("Digite o número de termos para a sequência: "))
soma = 0
denominador = 500
numerador = 2

while denominador >= 500+r*(N-1):
    if denominador != 0:
        soma += numerador/denominador
        print(f"{numerador}/{denominador}")
        if numerador == 2:
            numerador = -5
        else:
            numerador = 2
    denominador += r

print("A soma da sequência é", soma)
            