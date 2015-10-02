#!/usr/bin/env python
# -*- coding: utf-8 -*-

cont = 0
status = 0
token = []
arq = open('C:\Compiladores\identificadores.txt', 'r')

conteudo = arq.read()
numero = len(conteudo)
contagem = 1
tipo = ""


while cont < numero:

	#Identificardor------------------------------------
	if conteudo[0] == "*":
		print conteudo[cont]
		token.append(conteudo[0])
		cont = cont + 1
		status = 0		

		if conteudo[cont].isalpha():

			token.append(conteudo[cont])
			status =1
			cont = cont + 1
			
			
			if conteudo[cont] == "_":

				token.append(conteudo[cont])
				status = 0
				cont = cont + 1
				

				if conteudo[cont].isalpha():

					token.append(conteudo[cont])
					status = 1
					cont = cont + 1
					
					#print "Cont" + str(cont)
					#print
					#print "Numero" + str(numero)


					while cont < numero:

						
						if conteudo[cont].isalpha():

							token.append(conteudo[cont])
							status = 1
							cont = cont + 1
							
						elif conteudo[cont] == " ":
		
							break;		

						elif conteudo[cont] == '\n':

							token.append(conteudo[cont])
							print "Cont" + str(cont)
							print
							print "Numero" + str(numero)
							cont = cont + 1
							
			
							break;
							
						else:

							token.append(conteudo[cont])
							status = 0
							cont = cont + 1							
							break;

				elif conteudo[cont] == " ":
		
					break;					

				elif conteudo[cont] == '\n':

					token.append(conteudo[cont])
		
					break;	

				else:

					token.append(conteudo[cont])
					status = 0
					cont = cont + 1
					
					break;	


			elif conteudo[cont].isalpha():
			
				token.append(conteudo[cont])
				status = 1
				cont = cont +1
				

				while cont < numero:

					if conteudo[cont].isalpha():

						token.append(conteudo[cont])
						status = 1
						cont = cont + 1
						
						print "Cont" + str(cont)
						print
						print "Numero" + str(numero)

					elif conteudo[cont] == " ":
		
						break;		

					elif conteudo[cont] == '\n':
		
						token.append(conteudo[cont])
						cont = cont + 1
						
						break;
						
					else:

						token.append(conteudo[cont])
						status = 0
						cont = cont + 1
						
						break;

			elif conteudo[cont] == " ":
		
				break;				

			elif conteudo[cont] == '\n':
		
				token.append(conteudo[cont])
				break;
						
			else:

				token.append(conteudo[cont])
				status = 0
				cont = cont + 1
				
				break;
		

		elif conteudo[cont] == " ":
		
			break;	
				
		elif conteudo[cont] == '\n':
		
			token.append(conteudo[cont])
			break;
						
		else:
		
			token.append(conteudo[cont])
			status = 0	
			cont = cont + 1
			
			break;

		tipo = "identificador"		

		#------fim identificador-------------------

	#Palavra Reservada------------------------------------------------------	
		
	elif conteudo[0].isalpha():
	
		token.append(conteudo[cont])
		status = 1	
		cont = cont + 1
		print "Primeiro: " + str(token)

		while cont < numero:

			if conteudo[cont].isalpha():

				token.append(conteudo[cont])
				status = 1
				cont = cont + 1

			elif conteudo[cont] == "_":

				token.append(conteudo[cont])
				status = 0
				cont = cont + 1
				print "hifen: " + str(token)

				if conteudo[cont].isalpha():

					token.append(conteudo[cont])
					status = 1
					cont = cont + 1

					while cont < numero:

						if conteudo[cont].isalpha():

							token.append(conteudo[cont])
							status = 1
							cont = cont + 1

						elif conteudo[cont] == " ":

							break;		

						elif conteudo[cont] == '\n':

							token.append(conteudo[cont])
							cont = cont + 1				
							break;
							
						else:

							token.append(conteudo[cont])
							status = 0
							cont = cont + 1
							
							break;		

				elif conteudo[cont] == " ":

					break;		

				elif conteudo[cont] == '\n':

					token.append(conteudo[cont])
					cont = cont + 1

					break;
					
				else:

					token.append(conteudo[cont])
					status = 0
					cont = cont + 1	
					print "numero: " + str(token)	
					break;				

			elif conteudo[cont] == " ":

				break;		

			elif conteudo[cont] == '\n':

				
				token.append(conteudo[cont])
				cont = cont + 1				
				break;
				
			else:

				token.append(conteudo[cont])

				status = 0
				cont = cont + 1				
				break;

		if conteudo[cont-1] == " ":

			break;		

		elif conteudo[cont-1] == '\n':

			token.append(conteudo[cont])
			cont = cont + 1				
			break;
			
		else:

			token.append(conteudo[cont])
			status = 0
			cont = cont + 1
			
			break;				

		tipo = "PalavraRes"			


	elif conteudo[cont] == " ":
		
		break;		

	elif conteudo[cont] == '\n':

		token.append(conteudo[cont])
		break;

	else:

		token.append(conteudo[cont])
		status = 0
		cont = cont + 1	
		break;	

#conteudo = ""
						
	
if status == 1 and tipo == "identificador":

	print "Reconhece - Identificador"
	print
	print "Token" + str(token)

elif status == 1 and tipo == "PalavraRes":

	print "Reconhece - Palavra Reservada"
	print
	print "Token" + str(token)

else:

	print "Nao reconhece"
	print
	print "Token" + str(token)

	


