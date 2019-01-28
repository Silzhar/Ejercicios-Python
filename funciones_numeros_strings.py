# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 17:57:56 2019

@author: Yamabushi

"""
# ejercicio 4 ,tema 6
# carga de artículo y precio
def pieza():
    articulo=[]
    precio=[]
    for x in range(5):
        art=input('Artículo :')
        pre=float(input('Precio :'))
        articulo.append(art)
        precio.append(pre)
    return[articulo,precio]
    
# imprimir artículo y precio
def mostrar(articulo,precio):
    print(' - '*len(articulo))
    print('Listado de artículos y precios ')
    for x in range(len(articulo)):
        print('El artículo '+articulo[x]+' tiene un valor de :'+str(precio[x]))
        
# precio mayor
def mayor():
    mas=0
    print(' - '*len(articulo))
    print('El mayor precio  es : ',mas)
    for x in range(precio):
        if mas<precio[x]:
            mas=precio[x]
    
# objetos inferiores a precio por definir 
def rango():
    print(' - '*len(articulo))
    print('Objetos inferiores al siguiente rango')
    maximo=float(input('Precio maximo :'))
    for x in range(precio):
        if precio[x]<maximo:
            print(articulo[x]+' - '+str(precio[x])
    
# bloque de carga
articulos,precios=pieza()
mostrar(articulo,precio)
mayor(articulo,precio)
rango(articulo,precio)




        
    
    


        
        
    
