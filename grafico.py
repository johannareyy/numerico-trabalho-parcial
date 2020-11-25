# This Python file uses the following encoding: utf-8

from bib import leArquivoString, organizaDados, tempQueda
import matplotlib.pyplot as plt
import numpy as np

dados = open('dadosreduzidos.txt', 'r')

tabela = leArquivoString(dados)

vetorAltura, vetorMedia, vetorDesvio = organizaDados(tabela)

plt.plot([float(vetorAltura[0]), float(vetorAltura[1]), float(vetorAltura[2]), float(vetorAltura[3]), float(vetorAltura[4])], [float(vetorMedia[0]), float(vetorMedia[1]), float(vetorMedia[2]), float(vetorMedia[3]), float(vetorMedia[4])], "ro")
plt.errorbar(float(vetorAltura[0]), float(vetorMedia[0]), yerr=float(vetorDesvio[0]), color='red')
plt.errorbar(float(vetorAltura[1]), float(vetorMedia[1]), yerr=float(vetorDesvio[1]), color='red')
plt.errorbar(float(vetorAltura[2]), float(vetorMedia[2]), yerr=float(vetorDesvio[2]), color='red')
plt.errorbar(float(vetorAltura[3]), float(vetorMedia[3]), yerr=float(vetorDesvio[3]), color='red')
plt.errorbar(float(vetorAltura[4]), float(vetorMedia[4]), yerr=float(vetorDesvio[4]), color='red')

pos = np.linspace(0.5, 2.5, 100) 
plt.plot(pos, tempQueda(pos), "b-")

plt.ylabel('Tempo(s)') #descrição do y
plt.xlabel('Altura(m)') #descrição do x

plt.grid() 
plt.margins(0.1)
plt.show()
# plt.savefig("gráfico.png")