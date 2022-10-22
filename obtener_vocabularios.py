from asyncore import read
from mailbox import linesep
import os
os.chdir("C:/Users/doni_/Desktop/Semestre 9/Recuperacion/")

import string
from nltk.corpus import stopwords
import re
from nltk.stem.snowball import SnowballStemmer

#lectura del archivo de documentos
filename = "documentos_preprocesados.txt"
f = open(filename, 'r')
docs = []
a = 0
vocabulario = []


while(True):
    linea = f.readline().split()       
    #print(list(linea[0])[0])   
    j=1
    #print(len(linea))
    #linea = f.readline().split()
    for j in range(len(linea)):   # Revisará cada palabra de la línea leída.
        if(not list(linea[j])[0].isnumeric() and not linea[j].endswith("|")):  # si la palabra actual no empieza con numero y no termina con |
            if(linea[j]!="|"):      #si la palabra actual no es diferente |
                if(linea[j] not in vocabulario):  #si la palabra no esta en el vocabulario
                    vocabulario.append(f"{linea[j]}")            #entonces añadimos al arreglo
        j+=1
    if not linea: #si ya no hay mas lineas 
        break

f.close()
#print(vocabulario)

def escribir(nom, datos):
    file = open(nom, "w+")
    a=0
    # Saving the array in a text file
    for i in datos:
        file.write("%s\n" % i)
        a+=1
    file.write("\nNúmero de palabras: %s" %a)   
    file.close()

frecuencias = []
filename = "documentos_preprocesados.txt"

vocabulario2 = []
#reduccion 1
for i in vocabulario:
    if(len(i) > 1):
        vocabulario2.append(i)

vocabulario.sort()
vocabulario2.sort()

escribir("vocabulario.txt", vocabulario)
#escribir("vocabulario_reducido.txt", vocabulario2)

#reduccion 2 - eliminar palabras compuestas
array=[]
for f in vocabulario2:
    contador=0
    #print("1: "+f)
    for b in vocabulario2:        
        if(b.startswith(f)):
            contador+=1
            if(contador>1 and f!=b and len(b)>3 and len(f)>3):
                array.append(b)   

array2=[]
array3=[]
for t in vocabulario2:    
    conta1=0
    #print("1: "+f)
    for r in vocabulario2:        
        if(t.endswith(r)):
            conta1+=1
            if(conta1>1 and t!=r and len(r)>3 and len(t)>3):        
                array2.append(t)

for r in array:
    for y in array2:
        if(r==y):
            array3.append(r)

array3.sort()
vocabulario3 = []
for word in vocabulario2:
    if not word in array3:
        vocabulario3.append(word)

escribir("vocabulario_reducido.txt", vocabulario3)