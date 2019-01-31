# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 16:59:54 2019

@author: Yamabushi
"""
# tema 6 ejercicio 7
# función entrada de edades
def edades(edad,*años):
    total=0
    if edad>=18:
        total=total+1
    for x in range(len(años)):
        if años[x]>=18:
            total=total+1
    return total

# bloque principal,carga de edades 
print("Han superado la mayoría de edad :",edades(17,19,35,41,9))
print("Han superado la mayoría de edad :",edades(21,14,27,18,10,63))
print("Han superado la mayoría de edad :",edades(31,12,28,23,16,4))
