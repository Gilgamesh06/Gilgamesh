#!/usr/bin/env python

'''
Limpia los ejecutables

'''

import os

cwd = os.getcwd()
direccion = ""

dato = 0

for i in range(len(cwd)):
	if(dato != 3):
		direccion += cwd[i]
		if('/' == cwd[i]):
			dato +=1


url=direccion+"/laincpp"
borrar = "cd "+url+" && rm *"

cantidad = len(os.listdir(url))

if(cantidad > 0):
	os.system(borrar)
	print("Se borro exitosamente")
else:
	print("No hay ningun ejecutable")