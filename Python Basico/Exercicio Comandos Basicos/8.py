intervalo_superior = int(input("Digite o intervalo superior (Fahrenheit): "))
intervalo_inferior = int(input("Digite o intervalo inferior (Fahrenheit): "))


print(f"T (°C) | T (°F)")

for i in range(intervalo_inferior, intervalo_superior + 1, 1):
    C = (i - 32)*(5/9)
    print(f"{float(C):,.2f} | {i}")
print("----------------")

