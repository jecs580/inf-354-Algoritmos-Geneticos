import json


lista= [1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0]
cadena=json.dumps(lista)  # Convertimos la lista en una cadena
newstring=cadena.replace("[","")  # eliminamos el corchete de entrada
new2=newstring.replace("]","")  # eliminamos el corchete de salida
new3=new2.replace(",","")  # eliminamos las comas
new4=new3.replace(" ","")   # eliminamos los espacios en blanco
numerofinal=int(new4,2)   # Convertimos la cadena a un numero decimal indicando que la cadena es un numero en base 2.
print(numerofinal)
numerofinal=int("".join(map(str,lista)),2)  # Hacemos todo el trabajo de convetir el numero en una sola linea
print("nuevo numero final",numerofinal)