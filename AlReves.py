numero = int(input("Ingreasr un numero: "))
num = range(numero, 0, -1)
num2 = " ".join(str(indice) for indice in num)
print(num2)