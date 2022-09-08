# Ejercicio 1: cantidad a pagar de una llamada 

print("---------------------------.--------")
print("------TOTAL A PAGAR DE LLAMADA------")
print("------------------------------------")

# input
T =int(input("digite el valor del tiempo en minutos: "))

# proccesing

if T <= 3:
    print("El valor de la llamada es $300" )
elif T > 3:
    M = int((T - 3))
    p = (300 + M * 50)
    print("El total a pagar por minitos de la llamada es: " + str(p) )

