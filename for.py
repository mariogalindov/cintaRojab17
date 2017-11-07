'''
var = "HOLA"

for i in var:
	print("La letra que toma i es" + i)

for i in range(52,1000):
	print(i)
print("ACABO")



print("Multiplo de dos")
cuenta = 0
for i in range(1,100):
	if i % 2 == 0:
		cuenta = cuenta + 1 

print(cuenta)



print("Acumulador")

suma = 0 
for i in range(1,5):
	suma = suma + i
print(suma)



for i in range(1,1001):
	print(i)



print("Numeros pares del 1 al 1000")

pares = 0 
for i in range(1,1001):
	if i % 2 == 0:
		pares = pares + 1

print(pares)



var = "ELEFANTE"
pos = 0 
es = 0 
for i in var:
	pos = pos + 1
	if i == "E":
		es += 1
		if es == 3:
			print("Encontre la 3 E en la posición", pos)

'''

precio = 300
print("El precio del articulo 'x' es de ", precio)
cantidad = int(input("Indique la cantidad del articulo 'x' que desea \n"))
if cantidad > 5: 
	print("El total de tu compra es " ,(precio * cantidad) *.95)
else:
	print("El total de tu compra es ", (precio *cantidad))








