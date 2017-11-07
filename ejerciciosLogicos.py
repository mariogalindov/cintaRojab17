 #!usr/bin/python
 #-*- coding: utf-8 -*-  
 

x = int(input("Escriba un número X \n"))
y = int(input("Escriba un número Y \n"))
resultado = x / y

print(resultado)
if x % y == 0:
	print("Tu division es un numero exacto")
else:
	print("Tu division no es un numero exacto")

a = int(input("Escribe un numero X \n"))
b = int(input("Escribe un numero Y \n"))

if a > b:
	print(str(a) + " es mayor que " + str(b))
elif a == b:
	print(str(a) + " y " + str(b) + " son numeros iguales")
else:
	print(str(b) + " es mayor que " + str(a))



c = int(input("Escribe el año actual \n"))
d = int(input("Escribe un año X \n"))

if d >= c:
	print("Faltan " + str((d-c)) + " años para el año que escribiste")
else:
	print("Han pasado " + str((c-d)) + " años desde el año que escribiste")


e = int(input("Escribe un numero X \n"))
f = int(input("Escribe un numero Y \n"))
g = int(input("Escribe un numero Z \n"))

if e == f == g:
	print(str(e) + ", " + str(f) + " y " + str(g) + " son iguales!")
elif e == f or e == g or f == g:
	print("Tienes dos numeros iguales")
else:
	print("Todos tus numeros son diferentes")

'''

h = int(input("Escribe un numero X \n"))
i = int(input("Escribe un numero Y \n"))
j = int(input("Escribe un numero Z \n"))

if h > i > j:
	print(str(h) + " es el mayor de todos")
elif i > h > j:
	print(str(i) + " es el mayor de todos")
else:
	print(str(j) + " es el mayor de todos")





