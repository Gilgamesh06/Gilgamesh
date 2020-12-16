#!/usr/bin/env python

'''
Programa complilador c++
version 0.01

Gilgamesh 06

'''

import os

programa = input()
rango = len(programa)-4
cwd = os.getcwd()
direccion = ""
ejecutable = ""
dato = 0

for i in range(len(cwd)):
	if(dato != 3):
		direccion += cwd[i]
		if('/' == cwd[i]):
			dato +=1

for i in range(rango):
	ejecutable = programa[i]

url = direccion+"laincpp"
eje = "g++ -o "+ejecutable+" "+programa
sal = "./"+ejecutable
mover = 'mv '+ejecutable+' '+url

if(os.path.isdir(url)):
	os.system(eje)
	os.system(sal)
	os.system(mover)
else:
	os.mkdir(url)
	os.system(eje)
	os.system(sal)
	os.system(mover)
