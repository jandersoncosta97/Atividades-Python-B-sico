nome_completo = input("Digite o nome completo do usuário: ")
lista = nome_completo.split(" ")
nome_exibido = ""
for i in lista:
    if lista.index(i) == 0 or lista.index(i) == len(lista)-1:
        nome_exibido += i.upper()+" "
print(nome_exibido)
