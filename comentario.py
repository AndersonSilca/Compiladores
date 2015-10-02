

elif caracter == "@" and marcador2 == 0

	token.append(caracter)
	estado = 0
	marcador2 = 1


elif caracter == "@" and marcador2 == 1:

	token.append(caracter)
	estado = 1
	marcador2 = 2


elif caracter.isalpha() and marcador2 == 2:

	token.append(caracter)
	estado = 1
	marcador2 = 2

elif caracter == "/" and marcador3 == 0

	token.append(caracter)
	estado = 0
	marcador3 = 1


elif caracter == "/" and marcador3 == 1:

	token.append(caracter)
	estado = 1
	marcador3 = 2


elif caracter.isalpha() and marcador2 == 2:

	token.append(caracter)
	estado = 1
	marcador2 = 2

elif caracter == "/" and marcador2 == 2:

	token.append(caracter)
	estado = 0
	marcador2 = 3

elif caracter == "/" and marcador2 == 3:

	token.append(caracter)
	estado = 1
	marcador2 = 0			




