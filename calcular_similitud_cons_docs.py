import os
from operator import itemgetter
os.chdir("C:/Users/doni_/Desktop/Semestre 9/Recuperacion/")



def leer(archivo):

    # Se lee archivo que tiene el vocabulario para ponerlo en una matriz
    v = open(archivo, 'r')
    matriz=[]

    # linea1=v.readline().split()
    linea1=v.readlines()    
    j=0    
    for line in linea1:
        r=0
        aux = []           
        for k in line.split():
            if(r>=2):
                aux.append(int(k))
            r+=1
        matriz.append(aux)
        j+=1 
    return matriz

matrizConsultas=leer("consultasTF_V1.txt")
matrizDocumentos=leer("documentosTF_V1.txt")


def calcular_normas(matriz):
    normas = []
    for i in range(len(matriz)):
        suma = 0
        for j in range(len(matriz[0])):
            if matriz[i][j] != 0 :
                suma += matriz[i][j] ** 2 # exponente 2
        suma = suma ** 0.5 # raiz
        normas.append(suma)
    return normas

norma_docs = calcular_normas(matrizDocumentos)
norma_cons = calcular_normas(matrizConsultas)

def calcular_sim(normaD, normaC, matrizD, matrizC):

    arreglo_cons_sim = []
    for w in range(len(matrizC)): # 64 veces
        arreglo_sim = []
        for i in range(len(matrizD)): # 3204 docs
            arrayI=[]  # arreglo que tendra la similitud y su numero de documento perteneciente
            ppunto = 0
            for j in range(len(matrizD[0])): # 6118 palabras
                if matrizD[i][j] != 0 and matrizC[w][j] != 0:
                    ppunto += matrizC[w][j] * matrizD[i][j]
            sim = ppunto / (normaC[w] * normaD[i])
            #print(sim)
            arrayI.append(sim)
            arrayI.append(i)
            arreglo_sim.append(arrayI)
        arreglo_cons_sim.append(arreglo_sim)

    return arreglo_cons_sim


def ordenarSim(arreglo_cons_sim):
    final=[]
    for i in range(len(arreglo_cons_sim)):
        b=[]
        b=sorted(arreglo_cons_sim[i],key=itemgetter(0),reverse=True)
        final.append(b)
    print(final[0][:100])
    return final

arreglo=calcular_sim(norma_docs,norma_cons,matrizDocumentos,matrizConsultas)

print("Sin ordenar: \n")
print(arreglo[0][:100])
print("Ordenado : \n")
cosenos=ordenarSim(arreglo)

def escribirEnDoc(matriz,nombre):
    file = open(nombre, "w+")    
    for f in range(len(matriz)):
        for i in range(len(matriz[0])):
            if(matriz[f][i][0]>0):
                file.write("%s"%str(f)+"\t%s"%str(matriz[f][i][1])+"\t%s" %str(matriz[f][i][0]))   #consulta, documento , coseno      
                file.write("\n")


escribirEnDoc(cosenos,"CACM_TF_rels.txt")
















# ########## Cálculo de Producto punto ##############

# def productoPunto(consultas,documentos):
#     matrizPunto = []
    
#     for x in range(len(consultas)):
#         aux = []
#         for x1 in range(len(consultas[0])):
#             if(int(consultas[x][x1])>0):
#                 for r in range(len(documentos)):
#                     if(int(documentos[r][x1])):
#                         print("h")
#             else:            
#                 aux.append(consultas[x][x1])            

# productoPunto(matrizConsultas,matrizDocumentos)






