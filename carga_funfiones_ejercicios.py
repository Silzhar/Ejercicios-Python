# -*- coding: utf-8 -*-
"""
Created on Fri Jan 25 14:09:53 2019

@author: Yamabushi
"""

def frase():
    return input('Frase :')

def vocales(frase):
    tot=0
    lista=['a','e','i','o','u']
    for x in range(len(frase)):
        for k in range(len(lista)):
            if frase[x]==lista[k]:
                tot=tot+1
    print('Total de vocales:',tot)

# bucle 

frase1=frase()
frase2=frase()
frase3=frase()

vocales(frase1)
vocales(frase2)
vocales(frase3)
