#Escribe un programa que pida al usuario dos números enteros y determine:
#Si el primero es mayor que el segundo.
#Si son iguales.
#Si el primero es menor o igual que el segundo.
#Imprime los resultados con mensajes descriptivos.

num1 = (input("Ingrese un primer numero: "))
num2 = (input("Ingrese un segundo nunero: "))

resultado = (num1 > num2)
if resultado:
    print("El primer numero es mayor que el segundo")
elif num1 == num2:
    print("Los numeros son iguales")
else:
    print("El primer numero es menor que elsegundo")