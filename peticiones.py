import requests 
'''
response = requests.get('http://api.open-notify.org/iss-now.json/bucket/:from')

print(response.status_code)
print(response.ok)
print(response.headers['content-type'])
print(type(response.text))
print("_____________")

diccionario = response.json()
print(diccionario)
print(diccionario['timestamp'])
print(diccionario['iss_position'])

response2 = requests.get('https://www.foaas.com/bus/mike/alfred?callback=?')

print(response2)



BASE_URL = "http://pokeapi.co/api/v2/"
URI_POKEMON_1 = "pokemon/1"

URL = BASE_URL + URI_POKEMON_1

response = requests.get(URL)

diccionario = response.json()
lista = diccionario['game_indices']
diccionario2 = lista[13]
print(diccionario2)
version = diccionario2['version']
name = version['name']

print(name)
'''


def nombrePokemon(nombre):

	BASE_URL = "http://pokeapi.co/api/v2/"
	URI_POKEMON_1 = "pokemon/" + str(nombre)
	URL = BASE_URL + URI_POKEMON_1
	response = requests.get(URL)
	diccionario = response.json()
	name = diccionario['name']
	tipo1 = diccionario['types'][0]
	tipo2 = tipo1['type']
	tipo3 = tipo2['name']
	moves = diccionario['moves']

	return [name, tipo3, moves] 



numeroPokemon = int(input("Escriba el número de pokemon \n"))

nombreReal = nombrePokemon(numeroPokemon)
	

print("Tu pokemon es " + nombreReal[0] + " y es de tipo " + nombreReal[1] + " y tiene " + str(len(nombreReal[2])) + " ataques.")

for ataques in nombreReal[2]:
	print(ataques['move']['name'])

		



