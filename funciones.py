def mi_funcion():
	#Todo el bloque de código que se ejecuta cuando se llame la función
	print("Hola, soy una función")

# mi_funcion()


#Parametro y parametro con un valor por default
def suma_de_dos_numeros(num1,num2,num4=None):
	print(num4)
	suma = num1 + num2
	print(str(suma))

#Tienes que mandar llamar la función
#        suma_de_dos_numeros(3,5)

def funcion_return(num1,num2):
	suma = num1 + num2
	return suma 

sumar = funcion_return(2,2)
#print(sumar)

def return_mult(num1,num2,num3):
	if num1 == 2:
		return "Numero 2"
	else:
		return num3

multiple = return_mult(3,2,999)
print(multiple)