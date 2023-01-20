#Tipo de dato parecido a las listas con la diferencia que no es editable
#Tupla de 3 elementos
tupla = (1,2,3)

print(tupla)
print(type(tupla))
tupla2 = (7,"Roberto", True, 23.8, 16+7j)

print(tupla2)

print(tupla2[1])

print(tupla2[4])
print(tupla2[-1])
print(tupla2[0:3])
print(tupla2[3:])

#Se le asocia una variable a cada elemento de la tupla
a,b,c = tupla

print(a)
print(c)

tuplaN = tupla + tupla2
print(tuplaN)

#cuanta el total de apariciones de un elemento
print(tupla.count(2))

