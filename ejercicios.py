# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 16:44:08 2018

@author: Yamabushi
"""

lista=[]
mayor=0
menor=0
total=int(input('Total de números :'))
for x in range(total):
    n=int(input('Número :'))
    lista.append(n)
    if n>mayor:
        mayor=n
    else:
        if n<mayor:
            menor=n
            
lista.sort()
print(lista)
print('El número mayor es :',mayor)
print('El número menor es :',menor)
        


          
    
    
                




   
    


    