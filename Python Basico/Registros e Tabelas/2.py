# usando dicionário

n = int(input("Digite o tamanho da tabela de pessoas: "))
while n < 1:
    n = int(input("O tamanho deve ser inteiro e positivo. Tente novamente: "))
    
tab = {}

for i in range(n):
    codPessoa = int(input("Digite o código da pessoa: "))
    while codPessoa < 1:
        codPessoa = int(input("O código deve ser inteiro e positivo. Tente novamente: "))
    nomePessoa = input("Digite o nome da pessoa: ")
    salarioPessoa = int(input("Digite o salário da pessoa: "))
    while salarioPessoa < 0:
        salarioPessoa = int(input("O salário deve ser maior ou igual a zero. Tente novamente: "))
    
    tab[codPessoa] = (nomePessoa, salarioPessoa)

print('Tabela com %d pessoas foi lida corretamente. ' %(n))
print('Tabela ->', tab)

valor_max = float(input('Digite o valor máximo do salário: '))
while valor_max < 0:
    valor_max = float(input('O valor máximo deve ser maior ou igual a zero. Tente novamente: '))
    
print('-----------Dados filtrados-----------')

qtd_menor_igual = 0
soma = 0
for i in tab:
    if i[codPessoa][1] <= valor_max:
        print(i[codPessoa][1], "é menor ou igual a", valor_max)
        qtd_menor_igual += 1
        soma += i[codPessoa][1]
media = soma/qtd_menor_igual
print('A média do salário dessas pessoas é', media)
print('Fim do Programa')
