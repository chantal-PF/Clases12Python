# Escribe un programa que solicite al usuario ingresar la cantidad de 
# kilómetros recorridos por una motocicleta y la cantidad de litros de 
# combustible que consumió durante ese recorrido.
# Mostrar el consumo de combustible por kilómetro.

kilometro = float(input("Ingrese la cantidad en kilometros: "))
litros = float(input("Ingrese la cantidad en litros "))

consumo = litros / kilometro
print(consumo)