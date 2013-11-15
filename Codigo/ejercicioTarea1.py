import re #Libreria de expresiones regulares
f = open('sowpods.txt','r')

#Se declara el alfabeto que se utilizara para el programa. En este caso 
#es el alfabeto del idioma ingles.
alfabeto = ["A","B","C","D","E","F","G","H","I","J","K","L","M",
			"N","O","P","Q","R","S","T","U","V","X","Y","Z"]
#Se analizara cada linea del archivo
for line in f:
	#Si el alfabeto es vacio, salir del ciclo (No hay nada que revisar)
	if(alfabeto == {}):
		break
	#Iterar sobre los elementos del alfabeto
	for i in alfabeto[:]:
		#Se construye un patron que consta de la letra del alfabeto 
		#repetida de forma consecutiva
		pattern = i + i
		#Se busca en la linea obtenida anteriormente el patron
		result = re.search(r'%s'%pattern, line)
		#Si encuentra el patron, la letra "i" no forma parte de
		#la solucion. Eliminar este elemento de la lista
		if(result):
			alfabeto.remove(i)
print "Las letras que nunca salen repetidas de forma consecutiva son:"
#Imprimir el alfabeto resultante
for letra in alfabeto:
	print letra


	
