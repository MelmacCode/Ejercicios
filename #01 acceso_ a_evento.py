#Acceso a  evento (Operadores logicos y relacionales)

edad = 16
boleto_valido = True

acceso_permitido = (edad >= 18 and boleto_valido) or (edad >=65)

if acceso_permitido:
    print ("Acceso Permitido")
else:
    print("Acceeo Negado")