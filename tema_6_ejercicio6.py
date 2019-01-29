# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 18:15:06 2019

@author: Yamabushi
"""
# cargar tabla de multiplicar
def tabla(num1,num2=10):
    tabla_multiplicar=[]
    for x in range(num2):
        multiplicar=num1*x
        tabla_multiplicar.append(multiplicar)
    print('la tabla de multiplicar es :',tabla_multiplicar)
    return tabla_multiplicar


   
# bloque principal y llamada de la función
tabla(num1=int(input('Ingresar número a multiplicar :')))
tabla(num1=int(input('Ingresar número a multiplicar :')),num2=14)

