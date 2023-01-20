nombres = ["Juan","Mario","Laura"]
numeros = [1,2,3,4,5]
datos = [1,2.5,"Mario",True]

nombres[0] = "Roberto"

print(nombres[:])
print(nombres[2])
print(nombres[:3])
print(nombres[1:])

#Agregar un elemento
nombres.append("Dario")
print(nombres)

#Agregar un elemento o remplazarlo
nombres.insert(2,"Maria")
print(nombres)

#Unir dos listas
nombres.extend(["checha",2,23,5])

print(nombres)

#Quitar un elemento
nombres.remove("checha")
print(nombres)

#Eliminar el ultimo elemento
nombres.pop()
print(nombres)

n = ["juam"]
n2 = n*5
print(n2)
print(nombres)

#Eliminar un elemento en especifico
del nombres[0]
print(nombres)
