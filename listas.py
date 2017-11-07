 #!usr/bin/python
 #-*- coding: utf-8 -*-  

list1 = [2,3,1,4,5]
list2 = ["A","B","C","D"]
list3 = ["MATEMATICAS","HISTORIA", "1999", 8983]
list4 = [list1, list2, list3]

'''

print(list1)
print(list2)
print(list3)
print(list4)

frutas = ['naranja','manzana','kiwi','banana','pera']

print(frutas)

frutas.append('uva')
print(frutas)

frutas.extend(list2)
print(frutas)

frutas.insert(0,'melon')
print(frutas)


'''


palabras = int(input("¿Cuántas palabras tiene la lista? \n"))

if palabras < 1:
	print("Imposible!")

else:

	List = []

	for i in range(1 , palabras+1):

		palabras1 = input("Escribe la palabra " + str (i) + ": ")
		List.append(palabras1)

	print("La lista es " , List)

	'''

print("Ejercicio #2") #Ejercicio 2 

palabras2 = input("¿Qué palabra quieres buscar? \n")

cuentaPalabras = List.count(palabras2)

print("La palabra " , str(palabras2) , "aparece " , str(cuentaPalabras) ,  " en la lista.")


palabras3 = input("¿Qué palabra quieres buscar? \n") #Ejercicio 3

palabras4 = input("¿Por qué palabra la quieres reemplazar? \n")


for palabra in List:
	if palabra == palabras3:
		indice = List.index(palabra)
		List[indice] = palabras4
print("La lista actual es " , List)

'''

palabras5 = input("¿Qué palabra quieres quitar? \n")

for palabra in List:
	if palabra == palabras5:
		List.remove(palabras5)

print(List)









