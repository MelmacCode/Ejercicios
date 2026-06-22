#EJERCICIO 2: APROBACION DE CREDITO BANCARIO

#Problema: El banco aprueba un crédito si el cliente tiene ingresos mayores a 2500 Y un buen historial crediticio.
#También se aprueba si no tiene ingresos suficientes pero cuenta con un aval financiero, siempre y cuando 
#NO esté en la lista negra de deudores.

#Solución:
ingresos = 1500
historial_crediticio = True
aval_financiero = True
lista_negra = True

credito_aprobado = (ingresos >= 2500) and (historial_crediticio == True) or (aval_financiero == True) and (lista_negra == False)
if credito_aprobado:
    print("Crédito aprobado")
else:
    print("Crédito no aprobado")

