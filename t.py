import sys
from operator import itemgetter
from decimal import *
from collections import defaultdict

listaInicial = []
lista = []
juizes = 3

def regra6 ( atleta ):
    listaDesempate = [0 for x in range(len(atleta))]
    for x in range(len(atleta)):
        for y in range(len(atleta)):
            vit = Decimal(0)
            if x != y and y > x: 
                if listaInicial[atleta[x]-1][3] > listaInicial[atleta[y]-1][3] or (listaInicial[atleta[x]-1][3] == listaInicial[atleta[y]-1][3] and listaInicial[atleta[x]-1][6] > listaInicial[atleta[y]-1][6]):
                    vit += 1
                if (listaInicial[atleta[x]-1][3] == listaInicial[atleta[y]-1][3] and listaInicial[atleta[x]-1][6] == listaInicial[atleta[y]-1][6]):                        
                    vit += Decimal(0.5)
                if listaInicial[atleta[x]-1][4] > listaInicial[atleta[y]-1][4] or (listaInicial[atleta[x]-1][4] == listaInicial[atleta[y]-1][4] and listaInicial[atleta[x]-1][7] > listaInicial[atleta[y]-1][7]):
                    vit += Decimal(1)
                if (listaInicial[atleta[x]-1][4] == listaInicial[atleta[y]-1][4] and listaInicial[atleta[x]-1][7] == listaInicial[atleta[y]-1][7]):
                    vit += Decimal(0.5)
                if listaInicial[atleta[x]-1][5] > listaInicial[atleta[y]-1][5] or (listaInicial[atleta[x]-1][5] == listaInicial[atleta[y]-1][5] and listaInicial[atleta[x]-1][8] > listaInicial[atleta[y]-1][8]):
                    vit += Decimal(1)
                if (listaInicial[atleta[x]-1][5] == listaInicial[atleta[y]-1][5] and listaInicial[atleta[x]-1][8] == listaInicial[atleta[y]-1][8]):
                    vit += Decimal(0.5)
                if vit > (Decimal(juizes) / 2):
                    listaDesempate[x] += Decimal(1)
                elif vit == (Decimal(juizes) / 2):
                    listaDesempate[x] += Decimal(0.5)
                    listaDesempate[x] += Decimal(0.5)
                else:
                    listaDesempate[y] += Decimal(1)
    return listaDesempate

def regra7b10a( atleta ):
    listaDesempate = [0 for x in range(len(atleta))]
    for x in range(len(atleta)):
        nota = Decimal(listaInicial[atleta[x]-1][6]) + Decimal(listaInicial[atleta[x]-1][7]) + Decimal(listaInicial[atleta[x]-1][8])
        listaDesempate[x] += nota
    return listaDesempate

for s in sys.stdin.readlines():
    no = s.rstrip().split("\t")
    listaInicial.append((int(no[0]),no[2], Decimal(no[4]) + Decimal(no[7]) + Decimal(no[5]) + Decimal(no[8]) + Decimal(no[6]) + Decimal(no[9]),
       Decimal(no[4]) + Decimal(no[7]),Decimal(no[5]) + Decimal(no[8]), Decimal(no[6]) + Decimal(no[9]), Decimal(no[7]), Decimal(no[8]), Decimal(no[9])))

for atleta in listaInicial:
    if atleta[2] != 0:
        lista.append(atleta)

Matrix = [[0 for x in range(len(lista))] for y in range(len(lista))]

for i in range(len(lista)):
    for j in range(len(lista)):
        vit = Decimal(0)
        if (i != j):
            if lista[i][3] > lista[j][3] or (lista[i][3] == lista[j][3] and lista[i][6] > lista[j][6]):
                vit += 1
            if (lista[i][3] == lista[j][3] and lista[i][6] == lista[j][6]):
                vit += Decimal(0.5)
            if lista[i][4] > lista[j][4] or (lista[i][4] == lista[j][4] and lista[i][7] > lista[j][7]):
                vit += Decimal(1)
            if (lista[i][4] == lista[j][4] and lista[i][7] == lista[j][7]):
                vit += Decimal(0.5)
            if lista[i][5] > lista[j][5] or (lista[i][5] == lista[j][5] and lista[i][8] > lista[j][8]):
                vit += Decimal(1)
            if (lista[i][5] == lista[j][5] and lista[i][8] == lista[j][8]):
                vit += Decimal(0.5)
        Matrix[i][j] = vit

mv = defaultdict(list)

for i in range(len(Matrix)):
    tot = Decimal(0)
    for j in range(len(Matrix)):
        if Matrix[i][j] > Decimal(1.5):
            tot += Decimal(1)
        if Matrix[i][j] == Decimal(1.5):
            tot += Decimal(0.5) 
    mv[tot].append(lista[i][0])

classif = []

i = len(lista)
while i > 0:
    atleta = mv.get(i)
    if atleta != None and len(atleta) == 1:
        x = mv.get(i)
        print listaInicial[x[0]-1][1], format(float(listaInicial[x[0]-1][2]),'.3f'), i
    if atleta != None and len(atleta) == 2:
        atletaA = atleta[0] - 1
        atletaB = atleta[1] - 1
        vitoriasA = Decimal(0)
        if listaInicial[atletaA][3] > listaInicial[atletaB][3] or (listaInicial[atletaA][3] == listaInicial[atletaB][3] and listaInicial[atletaA][6] > listaInicial[atletaB][6]):
            vitoriasA += 1
        if (listaInicial[atletaA][3] == listaInicial[atletaB][3] and listaInicial[atletaA][6] == listaInicial[atletaB][6]):
            vitoriasA += Decimal(0.5)
        if listaInicial[atletaA][4] > listaInicial[atletaB][4] or (listaInicial[atletaA][4] == listaInicial[atletaB][4] and listaInicial[atletaA][7] > listaInicial[atletaB][7]):
            vitoriasA += 1
        if (listaInicial[atletaA][4] == listaInicial[atletaB][4] and listaInicial[atletaA][7] == listaInicial[atletaB][7]):
            vitoriasA += Decimal(0.5)
        if listaInicial[atletaA][5] > listaInicial[atletaB][5] or (listaInicial[atletaA][5] == listaInicial[atletaB][5] and listaInicial[atletaA][8] > listaInicial[atletaB][8]):
            vitoriasA += 1
        if (listaInicial[atletaA][5] == listaInicial[atletaB][5] and listaInicial[atletaA][8] == listaInicial[atletaB][8]):
            vitoriasA += Decimal(0.5)
        if vitoriasA >= 2:
            print listaInicial[atletaA][1], format(float(listaInicial[atletaA][2]),'.3f'), i
            print listaInicial[atletaB][1], format(float(listaInicial[atletaB][2]),'.3f'), i
        else:
            print listaInicial[atletaB][1], format(float(listaInicial[atletaB][2]),'.3f'), i
            print listaInicial[atletaA][1], format(float(listaInicial[atletaA][2]),'.3f'), i

    if atleta != None and len(atleta) > 2:
        desemp = regra6(atleta)
        if max(desemp) < (Decimal(juizes) / 2):
            novoDesemp = regra7b10a(atleta)
            while len(novoDesemp) > 0:
                valorImp = novoDesemp.index(max(novoDesemp))
                print listaInicial[atleta[valorImp] - 1 ][1], format(float(listaInicial[atleta[valorImp] - 1][2]),'.3f'), i
                novoDesemp.remove(max(novoDesemp))

    i -= 0.5

listf1 = []
listf2 = []
listf3 = []
listfinal = []
list1 = []

for atleta in lista:
    list1.append(atleta)

#print list1

list1.sort(key=itemgetter(2), reverse=True)

#print list1
i = 1
for atleta in list1:
    listf1.append([atleta[0], atleta[1], i])
    i += 1

list1.sort(key=itemgetter(3), reverse=True)
i = 1
for atleta in list1:
    listf2.append([atleta[0], atleta[1],i])
    i += 1

list1.sort(key=itemgetter(4), reverse=True)
i = 1
for atleta in list1:
    listf3.append([atleta[0], atleta[1],i])
    i += 1

listf1.sort(key=itemgetter(0))
listf2.sort(key=itemgetter(0))
listf3.sort(key=itemgetter(0))

for i in range(len(list1)):
    listfinal.append((i+1,lista[i][1],listf1[i][2],listf2[i][2],listf3[i][2]))
