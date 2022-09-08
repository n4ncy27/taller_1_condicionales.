#EJERCICIO 4: .  programa que lea un número entero y que determine si si último dígito es un número par.


print("--------------------------------------")
print("------ULTIMO_DIGITO_PAR---------------")
print("--------------------------------------")

# Input

x = int(input("DIGITE EL VALOR DE NUMERO ENTER0 N: "))

# proccesing

ultimo_digito = x % 10 
r = ultimo_digito % 2

if r == 0:
    print("El ultimo digito de " + str(x) + "ES PAR" )

if r!= 0:
    print("El ultimo digito de " + str(x) + "ES IMPAR")