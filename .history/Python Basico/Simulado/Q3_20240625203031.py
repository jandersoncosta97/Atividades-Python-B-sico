def MelhoresClientes(nome, base):
    qtd = 0
    media = 0.0
    try:
        arqEntrada = open(nome+'.txt', 'r')
        arqSaida = open(nome+'.Melhores.txt', 'w')
        
        for cliente in arqEntrada:
            mat = int(cliente[0:5])
            sexo = cliente[6]
            numPontos = cliente[8:15]
            nome = cliente[16:51]
            if int(numPontos) > base:
                arqSaida.write(mat, numPontos)
                qtd = qtd + 1
                media = media + int(numPontos) 
        arqEntrada.close()
        arqSaida.close()
        print('Gravado arquivo da empresa', nome)
        if qtd == 0:
            print('Nenhum cliente selecionado')
        else:
            med = med/qtd
            print('Gravados', qtd, 'Clientes com média', med)
    except IOError:
        print("Erro no arquivo da empresa", nome)        
    
n = int(input("Número de empresas: "))
while n < 1:
    n = int(input("Número de empresas: "))

for i in range(n):
    nomeEmp = input("Empresa: ")
    pontos = int(input("Base de pontos: "))
    while pontos < 0:
        pontos = int(input("Pontos: "))
    MelhoresClientes(nomeEmp, pontos)
    