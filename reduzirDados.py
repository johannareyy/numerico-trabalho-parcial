# This Python file uses the following encoding: utf-8

import bib

#abre os arquivos
altura1 = open('altura1.txt', 'r')
altura2 = open('altura2.txt', 'r')
altura3 = open('altura3.txt', 'r')
altura4 = open('altura4.txt', 'r')
altura5 = open('altura5.txt', 'r')

tempo1=[] 
tempo2=[]
tempo3=[]
tempo4=[]
tempo5=[]

#lê os 5 arquivos
#1.0
tempo1 = bib.leArquivo(altura1)
#1.25
tempo2 = bib.leArquivo(altura2)
#1.50
tempo3 = bib.leArquivo(altura3)
#1.75
tempo4 = bib.leArquivo(altura4)
#2.0
tempo5 = bib.leArquivo(altura5)

#conferir se ta lendo td certo
print('Tempos para cara altura')
print(tempo1)
print(tempo2)
print(tempo3)
print(tempo4)
print(tempo5)

# #obtem as 5 médias
media1 = bib.valorMedio(tempo1) #média da altura 1
media2 = bib.valorMedio(tempo2) #média da altura 2
media3 = bib.valorMedio(tempo3) #média da altura 3
media4 = bib.valorMedio(tempo4) #média da altura 4
media5 = bib.valorMedio(tempo5) #média da altura 5

#conferir se ta calculando certo
print('Valor Médio')
print(media1)
print(media2)
print(media3)
print(media4)
print(media5)

# #obtem os 5 desvios
desvio1 = bib.desvioPadrao(tempo1, media1) #altura 1
desvio2 = bib.desvioPadrao(tempo2, media2) #altura 2
desvio3 = bib.desvioPadrao(tempo3, media3) #altura 3
desvio4 = bib.desvioPadrao(tempo4, media4) #altura 4
desvio5 = bib.desvioPadrao(tempo5, media5) #altura 5

#conferir se o desvio ta certo
print('Desvio Padrão')
print(desvio1)
print(desvio2)
print(desvio3)
print(desvio4)
print(desvio5)