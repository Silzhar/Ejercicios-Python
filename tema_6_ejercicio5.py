# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 17:39:30 2019

@author: Yamabushi
"""

# tema 6, ejercicio 5
def tabla():
    pos=[]
    neg=[]
    tot=int(input('Total de valores a ingresar :'))
    for x in range(tot):
        numero=float(input('Ingrese número :'))
        if numero<0:
            neg.append(numero)
        else:
            pos.append(numero)
    print('Números positivos ingresados :',pos)
    print('Números negativos ingresados :',neg)
    return[pos,neg]
    
# bloque de carga  
tabla()


