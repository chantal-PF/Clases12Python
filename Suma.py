# Escribe un programa que solicite al usuario dos números y los almacene 
# en dos variables. En otra variable, almacená el resultado de la suma 
# de esos dos números y luego mostrá ese resultado en pantalla.
# A continuación, el programa debe solicitar al usuario que ingrese un 
# tercer número, el cual se debe almacenar en una nueva variable. 
# Por último, mostrá en pantalla el resultado de la multiplicación de 
# este nuevo número por el resultado de la suma anterior.

num1 = int(input("Escribe el primer numero: "))
num2 = int(input("Escribe el segundo numero: "))
suma = num1+ num2
print("La suma de los dos numero es:" , suma)
num3 = int(input("Escribe el tercero numero: "))
multi = suma * num3 
print("La multiplicacion de los dos numeros es:" , multi)