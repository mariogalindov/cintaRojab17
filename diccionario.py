diccionario = {'nombre' : 'Carlos' , 'edad' : 22 , 'cursos' : ['Python' , 'Flask']}
print(diccionario)
print(diccionario['nombre'])
print(diccionario['edad'])
print(diccionario['cursos'])
print(diccionario['cursos'] [0])

dic = dict(nombre='Nestor', apellido='Juarez', edad=22)

#print(dic['nombre'])      print(dic)

print("____________________________")

for key,value in diccionario.items():
	print(key + " : " + str(value))

print("____________________________")

#Devuelve el numero de elementos que tiene el diccionario
print(len(diccionario))

#Devuelve una lista con las llaves del diccionario
print(diccionario.keys())

#Devuelve una lista con los valores del diccionario
print(diccionario.values())

#Devuelve el valor del elementos con su clave, y si no lo encuentra trae un valor por default 
print(diccionario.get("nombree", "Juanito"))

#Inserta un elemento al diccionario con su clave:valor
diccionario['key'] = 'value'
print(diccionario)

#Elimina el elemento por la clave
diccionario.pop('key')
print(diccionario)

#Devuelve una copia del diccionario
diccionario2 = diccionario.copy()
print(diccionario2)

#Añade los elementos de un diccionario a otro
diccionario.update(dic)
print(diccionario)