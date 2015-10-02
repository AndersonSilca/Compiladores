#!/usr/bin/env python
# -*- coding: utf-8 -*-

arq = open('C:\Compiladores\identificadores.txt', 'r')

texto = arq.readlines()
token = []
cont = 0
estado = 0
marcador = 0
marcador2 = 0
marcador3 = 0
situacao = 0
marcador1 = 0
modo = ""

def enviaToken(token,estado,modo):
	result = ""
	palavra = []
	palavra = token
	
	print "palavra: " + str(palavra)

	if estado == 1:
		result = "Reconhece" + " " + modo

	else:
	
		result = "Nao Reconhece"

	print result
	print	
	


for linha in texto :

	for caracter in linha:

		if caracter == " ":

			enviaToken(token,estado,modo)
			token = []
			cont = 0
			estado = 0
			marcador = 0
			marcador2 = 0
			marcador3 = 0
			situacao = 0
			marcador1 = 0
			modo = ""
			

		#elif caracter == '\n':
			#break;			
		

		elif caracter.isalpha() and situacao == 0:
				
			estado = 1
			situacao = 0
			marcador1 = 1
			modo = "Palavra Reservada"
			token.append(caracter)
			#print "Entrei"
			
		elif caracter == "_" and marcador1 == 1:

			estado = 0
			situacao = 1	
			token.append(caracter)

		
		elif (caracter == ";") or (caracter == ",") or (caracter == ".") or (caracter == "-") or (caracter == "*") or (caracter == "(") or (caracter == ")") or (caracter == "/") or (caracter == "@"): 

			if marcador == 0:
				print caracter
				print "LALALALA	"
				token.append(caracter)
				estado = 1
				marcador = 10
				modo = "Simbolos Especiais"
				

			else:
				#print "oii"
				estado = 0
				token.append(caracter)
				

		elif (caracter == "<") or (caracter == "+"): 

			if marcador == 0:

				token.append(caracter)
				estado = 1
				marcador = 1
				print "Entrei"
				modo = "Simbolos Especiais"

			else:
			
				estado = 0
				token.append(caracter)
				

		elif (caracter == ">") or (caracter == "="):

			if marcador== 1:

				token.append(caracter)
				estado = 1
				modo = "Simbolos Especiais"
				marcador = 3
				
			else:
				print "SOASASSSSS"
				estado = 0
				token.append(caracter)
				


		elif (caracter == ":") or (caracter == ">"): 

			if marcador == 0:

				token.append(caracter)
				estado = 1
				marcador = 4
				modo = "Simbolos Especiais"

			else:	

				estado = 0
				token.append(caracter)				

		elif caracter == "=" and marcador == 4:
			
			token.append(caracter)
			estado = 1
			marcador = 40
			modo = "Simbolos Especiais"

		elif caracter == "!" and marcador2 == 0:

			token.append(caracter)
			estado = 0
			marcador2 = 1

		elif caracter.isalpha() and marcador2 == 1:
		
			token.append(caracter)
			estado = 1
			marcador2 = 2
			modo = "Identificador"	

		elif caracter == "_" and marcador2 == 2:
		
			token.append(caracter)
			estado = 0
			marcador2 = 3

		elif caracter.isalpha() and marcador2 == 3:
		
			token.append(caracter)
			estado = 1
			marcador2 = 3
			modo = "Identificador"


		elif caracter.isalpha() and marcador2 == 2:
		
			token.append(caracter)
			estado = 1
			marcador2 = 3
			modo = "Identificador"				

		else:
			print "oioioi"
			token.append(caracter)
			estado = 0
			

	
			
	#print token
	#token = []
	enviaToken(token,estado,modo)
	token = []	

#marcador = 0							



arq.close()	

#if estado == 1:

	#print"Reconhece"

#else:

	#print"Nao reconhece"	


#def indentifica(palavra):


#def pal_reserva(palavra):


#def comentario(palavra):



