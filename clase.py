class Auto:

	def __init__(self,nombre_cons,color,motor):#Esta es la sintaxis del constructor (un constructor es como la fábrica con los elementos escenciales de un objeto)
		#Atributos
		self.nombre = nombre_cons
		self.color = color
		self.ruedas = "4" #se queda como constante
		self.motor = motor
		print("CREANDO UN AUTO NUEVO")


	#Métodos
	def arranca(self):
		print("RUUUUUUN el " + self.nombre)

	def frena(self):
		print("FRENANDO el " + self.nombre)

	def get_color(self):
		print(self.color)

	def set_color(self,new_color):
		self.color = new_color

#SELF ES UNA VARIABLE QUE SE CREA POR CONVENCION SIEMPRE QUE SE VA A INSTANCIAR ESA CLASE

