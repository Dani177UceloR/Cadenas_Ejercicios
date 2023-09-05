"Ejercicio8.py"
Precio=input("Ingrese el precio del producto con dos decimales:" )
print(Precio[:Precio.find('.')], 'euros y', Precio[Precio.find('.')+1:], 'Centimos')