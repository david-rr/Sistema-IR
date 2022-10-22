import os
os.chdir("C:/Users/doni_/desktop/semestre 9/recuperacion/")

import string
from nltk.corpus import stopwords
import re
from nltk.stem.snowball import SnowballStemmer

#lectura del archivo de documentos
filename = "cacm/cacm.all"
f = open(filename, 'r')
docs = []
a = 0
while(True):
    linea = f.readline().strip('\n')
    if(linea == ".T"): #lectura del titulo
        a = a + 1
        titulo = f.readline().strip('\n') 
        aux = f.readline().strip('\n')
        while(True):
            if(aux != '.B' and aux !='.W'):
                titulo += f" {aux}"
                aux = f.readline().strip('\n')
            else:
                break
        if(aux == ".W"): #extraccion de texto
            texto = ""
            while(True):
                linea = f.readline().strip('\n')
                if(linea == ".B"):
                    break
                texto += f"{linea} "
            docs.append(f"{a} | {titulo} | {texto}")
        else:    
            docs.append(f"{a} | {titulo} |")
            
    if not linea: #si ya no hay mas lineas
        break
f.close()

#lectura del archivo de consultas
filename = "cacm/query.text"
f = open(filename, 'r')
cons = []
a = 0
while(True):
    linea = f.readline()
    if(linea == ".W\n"): #extraccion de texto
        a += 1
        texto = ""
        while(True):
            linea = f.readline().strip('\n')
            if(linea == ".N" or linea == ".A"):
                break
            texto += f"{linea} "
        cons.append(f"{a} | {texto}")

    if not linea:
        break
f.close()

def escribir(nom, datos):
    file = open(nom, "w+")
    # Saving the array in a text file
    for i in datos:
        file.write("%s\n" % i)
    file.close()

escribir("documentos.txt", docs)
escribir("consultas.txt", cons)

#preprocesamiento de los archivos generados
def preprocesar(filename): #funcion que retorna lista de palabras preprocesadas de un archivo
    #lectura del archivo
    file = open(filename, 'rt', encoding='utf-8')
    text = file.read()
    file.close()
    #recupera las primeras 100 palabras sin formatear
    words = text.split()
    #recupera las primeras 100 palabras eliminando los signos de puntuacion v2
    re_punc = re.compile('[%s]' % re.escape(string.punctuation))
    stripped = [re_punc.sub('', w) for w in words]
    #convierte a minusculas
    minus = [word.lower() for word in stripped]
    #lista de palabras vacias en ingles
    stop_words = stopwords.words('english')
    #elimina las palabras vacias de todo el documento v2, funciona más rapido ya que copia y no elimina
    lista_nueva = [ i for i in minus if i not in stop_words ]

    sn = SnowballStemmer(language="english")
    snowball = [sn.stem(word) for word in lista_nueva]

    return snowball

lista_docs = preprocesar("documentos.txt")
lista_cons = preprocesar("consultas.txt")

def escribir_preprocesado(nom, datos):
    contador = 1
    aux = ""
    file = open(nom, "w+")
    # Saving the array in a text file
    for i in datos:
        if(i == str(contador)):
            if(aux != ""):
                file.write("%s\n" % aux) 
            aux = f"{contador} "
            contador += 1
            a = 1
        else:
            if(i == '' and a <= 2):
                aux += "| "
                a += 1
            aux += f"{i} "
    file.write("%s\n" % aux)
    file.close()


escribir_preprocesado("documentos_preprocesados.txt", lista_docs)
escribir_preprocesado("consultas_preprocesados.txt", lista_cons)

print(docs[100])
print()
print(lista_docs[:500])