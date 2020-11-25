# This Python file uses the following encoding: utf-8

import math

def leArquivo (altura):
    """Lê um arquivo e devolve um vetor com cada linha em uma posição.
    Recebe: arquivo em txt.
    Retorna: vetor com dados do arquivo.
    """
    tempo=[]
   
    tempo.append(float(altura.readline()))
    tempo.append(float(altura.readline()))
    tempo.append(float(altura.readline()))
    tempo.append(float(altura.readline()))
    tempo.append(float(altura.readline()))

    return tempo


def valorMedio(tempo):
    """
    Calcula o valor médio entre 5 medidas de tempos.
    Recebe: cinco números reais.
    Retorna: o valor médio.
    """
    soma = 0.0

    for x in tempo:
        soma+=x

    return float(soma/5)

def desvioPadrao(tempos,valormedio):
    """
    Calcula o desvio padrão para cada altura.
    Recebe: cinco números reais, o valor médio.
    Retorna: o desvio padrão.
    """

    desvio = 0.0
    soma = 0.0
    variancia = 0.0

    for x in tempos:
        desvio = abs(valormedio-x)
        soma += math.pow(desvio,2)

    variancia = soma/5

    return math.sqrt(variancia)


def leArquivoString (dados):
    """Lê um arquivo e devolve um vetor com cada linha em uma posição.
    Recebe: arquivo em txt.
    Retorna: vetor com dados do arquivo.
    """
    tabela=[] 
    tabela.append(dados.readline()) #lê linha por linha do arquivo e armazena em um vetor
    tabela.append(dados.readline())
    tabela.append(dados.readline())
    tabela.append(dados.readline())
    tabela.append(dados.readline())

    return tabela


def organizaDados (tabela):
    """Organiza os dados do arquivo recebidos em 3 vetores.
    Recebe: vetor com cada dado da linha por posição do vetor.
    Retorna: 3 vetores com dados separados.
    """
    vetorAltura = []
    vetorMedia = []
    vetorDesvio = []
    linha = 0

    for y in tabela:
        auxpipe = 0
        auxprimeirocaracter = True
        for x in y:
            if x != '|':
                if auxpipe == 0:
                    if auxprimeirocaracter == True:
                        vetorAltura.append(x)
                        auxprimeirocaracter = False
                    else:
                        vetorAltura[linha] += x
                if auxpipe == 1:
                    if auxprimeirocaracter == True:
                        vetorMedia.append(x)
                        auxprimeirocaracter = False
                    else:
                        vetorMedia[linha] += x
                if auxpipe == 2:
                    if auxprimeirocaracter == True:
                        vetorDesvio.append(x)
                        auxprimeirocaracter = False
                    else:
                        vetorDesvio[linha] += x
            elif x == '|':
                auxpipe += 1
                auxprimeirocaracter = True
        linha += 1
    contador = 0
    for i in vetorDesvio:
        vetorDesvio[contador] = i.replace('\n', '')
        contador += 1
    return vetorAltura, vetorMedia, vetorDesvio

def tempQueda (pos):
    """
    Calcula o tempo de queda livre para dada posição.

    Recebe: posição inicial.

    Retorna: tempo de queda.
    """
    return (2*pos/9.81)**(1/2)