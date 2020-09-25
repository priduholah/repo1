#!/bin/python3
import sys
for i in range(20):
	for j in range(20):
		if(abs(abs(i-10)+abs(j-10))<10):
			print(chr(1200+i*j),end="")
		else:
			print(" ",end="")
	print("")
print("\n\n  E P I P S Y C H I D I O N \n \n")

if(len(sys.argv)!=3):
	print("Numero incorrecto de argumentos")
	sys.exit()
else:
	g=sys.argv[0]
	print (g)
	
