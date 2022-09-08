# Ingresar un número entero y determine si es un número positivo de 4 dígitos

print("------------------------------------")
print("---NúMERO ENTERO Y DE CUTRO DIGITOS ")
print("------------------------------------")

# input

x = int(input("Digite el valor del numero: "))

#   Processing 
if 999 < x < 10000:
    msj = (" El numero digitado tiene cuatro digitos")
else:
    msj = (" El numero digitado no tiene 4 digitos ")

# output

print("El numero es " + str(x) + msj)