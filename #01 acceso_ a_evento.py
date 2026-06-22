#Acceso a  evento (Operadores logicos y relacionales)
#Para entrar a un concierto se deben cumplir ambas condiciones:
#Tener 18 años o más.
#Tener un boleto válido (True o False).
#Además, hay una excepción: si la persona es mayor de 65 años, no necesita boleto (acceso libre).
#Escribe un programa que, dada la edad y si tiene boleto, imprima "Acceso permitido" o "Acceso denegado".

edad = 16
boleto_valido = True

acceso_permitido = (edad >= 18 and boleto_valido) or (edad >=65)

if acceso_permitido:
    print ("Acceso Permitido")
else:
    print("Acceeo Negado")