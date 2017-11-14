import requests 

def peticionLibros():

	BASE_URL = "https://goodreads-devf-aaron.herokuapp.com/"
	URI_AUTORES = "api/v1/authors/"
	URL = BASE_URL + URI_AUTORES
	response = requests.get(URL)
	diccionario = response.json()
	nombre = diccionario[0]['name']
	apellido = diccionario[0]['last_name']
	nacionalidad = diccionario[0]['nacionalidad']
	biografia = diccionario[0]['biography']

	return [nombre, apellido, nacionalidad, biografia]

print(peticionLibros())
