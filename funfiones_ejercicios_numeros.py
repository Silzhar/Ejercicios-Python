# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 14:09:53 2019

@author: Yamabushi
"""
# función carga de números
def numero():
    n=int(input('Número :'))
    return n

# función suma
def suma():
    suma=n1+n2+n3+n4
    print('La suma total es :',suma)
    
# función resta
def resta():
    resta=n1-n2-n3-n4
    print('La resta de los cuatro números es :',resta)
    
# función para mostrar valores
def muestra():
    print('Los valores utilizados han sido :',str(n1)+" "+str(n2)+" "+str(n3)+" y "+str(n4))

# bloque de carga 
n1=numero()
n2=numero()
n3=numero()
n4=numero()

#bloque llamada funciones
suma()
resta()
muestra()

