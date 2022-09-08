# Ejercicio No 9 :  Negocio y clientes


print("---------------------------------------")
print("----------RECARGO-O-DESCUENTO----------")
print("---------------------------------------")
print("")

#input
print("------------------MENU-----------------")
print("--------1.CLIENTE-GENERAL--------------")
print("--------2.CLIENTE-AFILIADO--------------")

c = int(input("determine cual opción quiere: "))

#process
if c == 1:
    print("--------1.CONTADO--------------")
    print("--------2.PLAZOS---------------")
    p = input("metodo de pago elija una opción 1 o 2: ")
    if p == 1:
        d = int(input("Digite el valor de la compra: "))
        d1 = d *0.15
        d2 = d + d1
    else:
        d = int(input("Digite el valor de la compra: "))
        d1 = d *0.10
        d2 = d - d1
else:
    print("--------1.CONTADO--------------")
    print("--------2.PLAZOS---------------")
    p = input("Para el metodo de pago elija 1 para al contado o 2 para plazos: ")
    if p == 2:
        d = int(input("Digite el valor de la compra realizada: "))
        d1 = d *0.5
        d2 = d + d1
    else:
        d = int(input("Digite el valor de la compra: "))
        d1 = d *0.20
        d2 = d - d1

#output
print("---------------------")
print("------RESULTADOS-----")
print("---------------------")

print("El valor total a pagar es ",d2)