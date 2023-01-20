print("Tablas de Multiplicar")

num = int(input("Ingresa el número que deseas para la tabla: "))

tablas = [1,2,3,4,5,6,7,8,9,10]

for val in tablas:
    valor = num * val
    print("{} X {} = {}" .format(num,val,valor))