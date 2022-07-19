from re import search
from re import compile
from re import I

def extract_persons(text):

	name = compile(r'([A,E,I,O,U]{1}[a-z]{2}|[A-Z]{1}[a-z]{3,}){1} ([A,E,I,O,U]{1}[a-z]{2}|[A-Z]{1}[a-z]{3,}){1} [A-Z]{1}[a-z]{3,} [A-Z]{1}[a-z]{3,}|([A,E,I,O,U]{1}[a-z]{2}|[A-Z]{1}[a-z]{3,}) [A-Z]{1}[a-z]{3,}( [A-Z]{1}[a-z]{3,})?')
	start = 0
	end = 0
	n = len(text)
	names = []
	
	while(end < n):
		text = text[end:]
		name_found = name.search(text, I)
		if(name_found == None):
			return names
		else:
			names.append(name_found.group())
			start, end = name_found.span()
	return names


if  __name__ == "__main__":
	# Los nombres pueden comenzar con una vocal pero no tiene mas de tres letras
	# (para no confudirlos con Las, Los, etc).
	# [A,E,I,O,U]{1}[a-z]{2}
	print(extract_persons("Ana"))
	print(extract_persons("hola Ana"))
	print(extract_persons("hola Los"))

	# Los nombres pueden comenzar con cualquier letra pero deben tener a lo menos cuatro letras.
	# [A-Z]{1}[a-z]{3,}
	print(extract_persons("hola Jose"))
	print(extract_persons("hola Maria"))

	# Cualquiera de ambos casos anteriores es posible.
	# [A,E,I,O,U]{1}[a-z]{2}|[A-Z]{1}[a-z]{3,}

	# Todos los nombres tienen apellidos, pero los apellidos vienen después de los nombres
	# (Para no confudirlos con Los Rios, San Juan, etc), además los apellidos tienen a lo menos cuatro
	# letras y hay un espacio en blanco entre el nombre y el apellido.
	# [A,E,I,O,U]{1}[a-z]{2} [A-Z]{1}[a-z]{3,}|[A-Z]{1}[a-z]{3,} [A-Z]{1}[a-z]{3,}
	print(extract_persons("hola Ana Soto"))
	print(extract_persons("hola Maria Soto"))
	print(extract_persons("hola Ana como esta Juan"))
	print(extract_persons("hola Ana Soto como esta Juan Soto"))
	print(extract_persons("hola Los Rios como esta San Jose"))

	# Tambien una persona podria aparecer con un apellido o dos apellidos.
	# ([A,E,I,O,U]{1}[a-z]{2}|[A-Z]{1}[a-z]{3,}) [A-Z]{1}[a-z]{3,}( [A-Z]{1}[a-z]{3,})?
	print(extract_persons("hola Ana Soto Corral"))
	print(extract_persons("hola Ana Maria Soto"))

	# También podria tener dos nombres y dos apellidos, pero no dos nombres y un apellido
	# ([A,E,I,O,U]{1}[a-z]{2}|[A-Z]{1}[a-z]{3,}){1} ([A,E,I,O,U]{1}[a-z]{2}|[A-Z]{1}[a-z]{3,}){1} [A-Z]{1}[a-z]{3,} [A-Z]{1}[a-z]{3,}|([A,E,I,O,U]{1}[a-z]{2}|[A-Z]{1}[a-z]{3,}) [A-Z]{1}[a-z]{3,}( [A-Z]{1}[a-z]{3,})?')
	print(extract_persons("hola Ana Maria Soto Corral"))
