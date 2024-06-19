with open('discip.old', 'r') as f1:
    lista_linhas = f1.readlines()

creditos_alterados = 0
with open('discip.new', 'w', encoding='utf-8') as f2:
    f2.write(f"codigo        nome                            creditos       carga-horária\n")
    for i in lista_linhas:
        codigo = i[0:5]
        nome = i[6:42]
        creditos = i[42:44]
        if codigo != 'IF125' and codigo != 'IF380':
            if 'MA' in codigo:
                creditos_alterados += 1
                creditos = 5
            f2.write(f'{codigo}     {nome} {creditos}              {(int(creditos)*15)}\n')

f3 = open('discip.old', 'r', encoding='utf-8')
f4 = open('discip.new', 'r', encoding='utf-8')

numero_disciplinas_old = 0
numero_disciplinas_new = 0

for i in f3.readlines():
    numero_disciplinas_old += 1
for i in f4.readlines():
    numero_disciplinas_new += 1

    
f3.close()
f4.close()

print(f"O número de disciplinas do arquivo 'discip.old' é {numero_disciplinas_old} \
enquanto que o número de disciplinas do arquivo 'discip.new' é {numero_disciplinas_new-1} \ # -1 ocorre devido ao cabeçalho
e o número de disciplinas com crédito modificado é {creditos_alterados}")
