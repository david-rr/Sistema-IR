from cmath import log10
import os
import numpy as np
os.chdir("C:/Users/doni_/Desktop/Semestre 9/Recuperacion/")

def leer(archivo):
    # Se lee archivo que tiene el vocabulario para ponerlo en una matriz
    v = open(archivo, 'r')
    vocabulario = []
    while(True):
        linea1=v.readline().split()
        if not linea1:
            break     
        vocabulario.append(f"{linea1[0]}")
    v.close()
    return vocabulario

def matrizFrecuencias(archivo, vocab):
    f = open(archivo, 'r')
    lineas = f.readlines()
    f.close()

    #creacion de matriz
    matriz = []
    for i in range(len(lineas)):
        aux = []
        for j in range(len(vocab)):
            aux.append(0)
        matriz.append(aux)

    lista = np.array(vocab)
    doc = 0
    for linea in lineas:
        palabras = linea.split()
        for i in range(2, len(palabras)):
            if palabras[i] == '|':
                continue #si es igual a '|' salta a la siguiente palabra si existe
            if not palabras[i] in vocab:
                continue
            term = np.where(lista == palabras[i])
            pos = int(term[0][0])
            matriz[doc][pos] += 1
        doc += 1

    return matriz

def calcularIDF(matriz, vocab):
    arreglo_idf = []
    
    for j in range(len(vocab)):
        conta = 0
        for i in range(len(matriz)):
            if(matriz[i][j] > 0):
                conta += 1
        idf = round(np.log10(len(matriz)/conta), 4) + 1
        arreglo_idf.append(idf)
        # if(vocab[j] == "algebra"):
        #     print(f"{idf} algebra {conta} ")

    return arreglo_idf

def matrizIDF(matriz, arreglo_idf, vocab):
    matriz_idf = []
    for i in range(len(matriz)):
        aux = []
        for j in range(len(vocab)):
            res = matriz[i][j] * arreglo_idf[j]
            aux.append(res)
        matriz_idf.append(aux)

    return matriz_idf

vocabulario = leer("vocabulario.txt")
vocabulario2 = leer("vocabulario_reducido.txt")

matrizDocumentos = matrizFrecuencias("documentos_preprocesados.txt", vocabulario)
matrizConsultas = matrizFrecuencias("consultas_preprocesados.txt", vocabulario)

arreglo_idf = calcularIDF(matrizDocumentos, vocabulario)

matriz_idf_documentos = matrizIDF(matrizDocumentos, arreglo_idf, vocabulario)
matriz_idf_consultas = matrizIDF(matrizConsultas, arreglo_idf, vocabulario)

#vocabulario reducido 
matrizDocumentos2 = matrizFrecuencias("documentos_preprocesados.txt", vocabulario2)
matrizConsultas2 = matrizFrecuencias("consultas_preprocesados.txt", vocabulario2)

arreglo_idf2 = calcularIDF(matrizDocumentos2, vocabulario2)

matriz_idf_documentos2 = matrizIDF(matrizDocumentos2, arreglo_idf2, vocabulario2)
matriz_idf_consultas2 = matrizIDF(matrizConsultas2, arreglo_idf2, vocabulario2)



def escribirEnDoc(nombre,matriz,x,y):
    file = open(nombre, "w+")    
    for f in range(x):
        r=f+1
        file.write("%s | " %r)
        for t in range(y):
            file.write("  %s" %matriz[f][t])
        file.write("\n")

#print(len(matrizConsultas))
#print(len(matrizConsultas[0]))
escribirEnDoc("consultasTF_V1.txt",matrizConsultas,len(matrizConsultas),len(matrizConsultas[0]))
escribirEnDoc("consultasTF_V2.txt",matrizConsultas2,len(matrizConsultas2),len(matrizConsultas2[0]))

escribirEnDoc("documentosTF_V1.txt",matrizDocumentos,len(matrizDocumentos),len(matrizDocumentos[0]))
escribirEnDoc("documentosTF_V2.txt",matrizDocumentos2,len(matrizDocumentos2),len(matrizDocumentos2[0]))

escribirEnDoc("consultasIDF_V1.txt",matriz_idf_consultas,len(matriz_idf_consultas),len(matriz_idf_consultas[0]))
escribirEnDoc("consultasIDF_V2.txt",matriz_idf_consultas2,len(matriz_idf_consultas2),len(matriz_idf_consultas2[0]))

escribirEnDoc("documentosIDF_V1.txt",matriz_idf_documentos,len(matriz_idf_documentos),len(matriz_idf_documentos[0]))
escribirEnDoc("documentosIDF_V2.txt",matriz_idf_documentos2,len(matriz_idf_documentos2),len(matriz_idf_documentos2[0]))

# def escribirMatrices(archivo, matriz):
#     Array = np.array(matriz)
#     np.savetxt(archivo, Array, fmt='%2.3f')
    

# escribirMatrices("matrizTFDoc.txt", matrizDocumentos)
# escribirMatrices("matrizTFDoc2.txt", matrizDocumentos2)
# escribirMatrices("matrizTFCons.txt", matrizConsultas)
# escribirMatrices("matrizTFCons2.txt", matrizConsultas2)
# escribirMatrices("matrizTF-IDFDocs.txt", matriz_idf_documentos)
# escribirMatrices("matrizTF-IDFDocs2.txt", matriz_idf_documentos2)
# escribirMatrices("matrizTF-IDFCons.txt", matriz_idf_consultas)
# escribirMatrices("matrizTF-IDFCons2.txt", matriz_idf_consultas2)
