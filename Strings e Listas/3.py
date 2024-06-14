string1 = input("Digite a primeira string: ")
string2 = input("Digite a segunda string: ")

cont = 0
res = string2.find(string1)
while res != -1:
    cont += 1 
    res = string2.find(string1, res+1)
    

print(f"A string '{string1}' aparece {cont}x na string '{string2}'")
