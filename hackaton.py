'''
def prime_numbers(n):
  numerosP =  ([2] + [x for x in range(3, n+1, 2) if not [y for y in range(3, int(x**0.5)+1, 2) if (float(x) / y).is_integer()]]) if n >= 2 else []
  return numerosP

def problema1(numerosPrimos):

	numerosPrimosSplit = numerosPrimos.split(",")

	listaPrimos = []

	for n in numerosPrimosSplit:

		listaPrimos.append(int(n))
	r = prime_numbers(100)

	if r == listaPrimos:
		return True 
	else:
		return False
'''

#termina problema 1 y esta resuelta por la función problema1 y el parametro numerosPrimos espera una string de numeros separados por comas

print ("Escribe la palabra más larga y la más corta de la siguiente lista de palabras \n")
larga = input("Palabra más larga \n")
corta = input("Palabra más larga \n")

def find_longest_word(listaPalabras):  
    longest_word =  max(listaPalabras, key=len)
    return longest_word
 

#Que el problema2 lo haga con checkbox y espera string