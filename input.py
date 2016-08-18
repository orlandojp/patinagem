import sys
from operator import itemgetter
from decimal import *
from collections import defaultdict

listaSaida = []
listaInicial = []
lista = []
juizes = 3

# Le o ficheiro de atletas para determinar qual foi a ultima atleta que actuou
def atletasCompetiram (fname):
    with open(fname) as file:
        atletas = file.readlines()
        if len(atletas) > 0:
            ultima = atletas[-1].split('\t')
        else:
            ultima = [0]
        return ultima[0]

# Carrega o ficheiro dos atletas que ja competiram
def carregaAtletas():
    file = open( "atletas.txt", "r" )
    for line in file:
        atleta = line.rstrip().split("\t")
        listaInicial.append((atleta[0], atleta[1], atleta[2], atleta[3], Decimal(atleta[4]) + Decimal(atleta[5]) + Decimal(atleta[6]), Decimal(atleta[7]) + Decimal(atleta[8]) + Decimal(atleta[9]), Decimal(atleta[7]), Decimal(atleta[8]), Decimal(atleta[9])))
    file.close()

# Le o ficheiro com a ordem de saida dos atletas para receber as notas 
def leOrdemSaida():
    file = open( "ordem.txt", "r" )
    for line in file:
        no = line.rstrip().split("\t")
        # listaSaida contem a ordem de saida dos atletas
        listaSaida.append((no[0],no[1], no[2], no[3]))
       # listaSaida.append((int(no[0]),no[2], Decimal(no[4]) + Decimal(no[7]) + Decimal(no[5]) + Decimal(no[8]) + Decimal(no[6]) + Decimal(no[9]),
       #     Decimal(no[4]) + Decimal(no[7]),Decimal(no[5]) + Decimal(no[8]), Decimal(no[6]) + Decimal(no[9]), Decimal(no[7]), Decimal(no[8]), Decimal(no[9])))
    file.close()

# Converte as notas lidas que nao esteja no sistema com decimas para a nota correspondente
def converteNota ( nota ):
    if nota > 10:
        nota = Decimal(nota)/Decimal(10)
    return nota

def leNota( ultimo ):
    novoAtleta = True
    i = int(ultimo)
    while novoAtleta:
        file = open ("atletas.txt", "a")
        print 'Atleta: ', listaSaida[i][2], listaSaida[i][3]
        print 'Nota A'
        nota1 = Decimal(input("Juiz 1: "))
        nota1 = converteNota (nota1)
        nota2 = Decimal(raw_input("Juiz 2: "))
        nota2 = converteNota (nota2)
        nota3 = Decimal(raw_input("Juiz 3: "))
        nota3 = converteNota (nota3)
        print 'Nota B'
        nota4 = Decimal(input("Juiz 1: "))
        nota4 = converteNota (nota4)
        nota5 = Decimal(raw_input("Juiz 2: "))
        nota5 = converteNota (nota5)
        nota6 = Decimal(raw_input("Juiz 3: "))
        nota6 = converteNota (nota6)
        # listaInicial composta por num, num da fpp, nome, clube, soma notas A, somas notas B, notas B discriminadas
        listaInicial.append(( listaSaida[i][0], listaSaida[i][1], listaSaida[i][2], listaSaida[i][3], nota1 + nota2 + nota3, nota4 + nota5 + nota6, nota4, nota5, nota6 ))
        texto = listaSaida[i][0] + '\t' + listaSaida[i][1] + '\t' + listaSaida[i][2] + '\t' + listaSaida[i][3] + '\t' + str(nota1) + '\t' + str(nota2) + '\t' + str(nota3) + '\t' + str(nota4) + '\t' + str(nota5) + '\t' + str(nota6) + '\n'
        print texto
        file.write(texto)
        i += 1
        file.close()
        continuar = raw_input("Novo atleta? ")
        if continuar != 's':
            novoAtleta = False

    print listaInicial

ultimo = atletasCompetiram("atletas.txt")
if ultimo != 0:
    carregaAtletas()
leOrdemSaida()
print ultimo
leNota( ultimo )
