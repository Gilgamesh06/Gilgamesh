#!/usr/bin/env python

'''
Agrega el alias
'''

import os
import subprocess

cwd = os.getcwd()
direccion = ""
dato = 0
shell = ""
rc = "rc"
for i in range(len(cwd)):
	if(dato != 3):
		direccion += cwd[i]
		if('/' == cwd[i]):
			dato +=1


direct_output = subprocess.check_output('echo $SHELL', shell=True) 
l=direccion+"."
dato = 0

for i in range(len(direct_output)):
	if( 47 == direct_output[i]):
		dato +=1
	if((dato == 3) and (10 != direct_output[i]) and ( 47 != direct_output[i])): 
		shell += chr(direct_output[i])


fichero =str(l+shell+rc)
texto1 = '\n# edit PATH.\n\nexport PATH=$PATH:"'+direccion+'Gilgamesh"\n'
texto2 = '\n# Mis alias personalizados.\n\nalias laincpp="./laincpp.py"\n'
texto3 = '\nalias clscpp="./clear.py"'

ObjFichero1 = open( fichero, 'a' )
alias1 = texto1
ObjFichero1.write(alias1)

ObjFichero2 = open( fichero, 'a' )
alias2 = texto2
ObjFichero2.write(alias2)

ObjFichero4 = open( fichero, 'a' )
alias4 = texto3
ObjFichero4.write(alias4)

