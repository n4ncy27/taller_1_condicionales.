# Ejercicio No. 10: Ordenar 3 numeros en ascendete


print("--------------------------------")
print("----ORDENAR-DE-MENOR-A-MAYOR----")
print("--------------------------------")
print("--------------------------------")

#input
n1 = int(input("Ingresa el primer valor: "))
n2 = int(input("Ingresa el segundo valor: "))
n3 = int(input("Ingresa el tercer valor:"))

#proceso y output
if n1 <= n2 and n1 <= n3:
    if n2 <= n3:
        print("El orden de los números de menor a mayor es: {} < {} < {}".format(n1,n2,n3))
    else:
        print("El orden de los números de menor a mayor es: {} < {} < {}".format(n1,n3,n2))

elif n2 <= n1 and n2 <= n3:
    if n1 <= n3:
        print("El orden de los números de menor a mayor es: {} < {} < {}".format(n2,n1,n3))
    else:
        print("El orden de los números de menor a mayor")

elif n3 <= n1 and n3 <= n2:
    if n1 <= n2:
        print("El orden de los números de menor a mayor es: {} < {} < {}".format(n3,n1,n2))
    else:
        print("El orden de los números de menor a mayor es: {} < {} < {}".format(n3,n2,n1))