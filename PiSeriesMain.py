# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 17:18:53 2018

@author: Gabriel E. Rodriguez
"""

from PiSeriesFunctions import *
import matplotlib.pyplot as plt

print("================ Aproximacion de Pi con series ================")

errorPorcentual = float(input("Error porcentual dispuesto a aceptar: "))
print(" ")

term1, estimate1, relativeError1, estimateVector1, errorVector1 = PiSeries1(errorPorcentual)
term2, estimate2, relativeError2, estimateVector2, errorVector2 = PiSeries2(errorPorcentual)
term3, estimate3, relativeError3, estimateVector3, errorVector3 = PiSeries3(errorPorcentual)

print("Primera Ecuacion: ")
print("Terminos: " + str(term1) + "\t\tValor estimado: " + str(estimate1) + "\t\tError asociado: " + str(relativeError1))
print(" ")

print("Segunda Ecuacion: ")
print("Terminos: " + str(term2) + "\t\tValor estimado: " + str(estimate2) + "\t\tError asociado: " + str(relativeError2))
print(" ")

print("Tercera Ecuacion: ")
print("Terminos: " + str(term3) + "\t\tValor estimado: " + str(estimate3) + "\t\tError asociado: " + str(relativeError3))

ax1 = plt.subplot(211)

plt.plot(list(range(1,len(estimateVector1)+1)), estimateVector1,'k-')
plt.plot(list(range(1,len(estimateVector2)+1)), estimateVector2,'co')
plt.plot(list(range(1,len(estimateVector3)+1)), estimateVector3,'r--')

plt.ylabel('Estimado')
plt.title('Aproximacion de Pi con series')
plt.grid(True)

ax2 = plt.subplot(212, sharex = ax1)

plt.plot(list(range(1,len(estimateVector1)+1)), errorVector1,'k-')
plt.plot(list(range(1,len(estimateVector2)+1)), errorVector2,'co')
plt.plot(list(range(1,len(estimateVector3)+1)), errorVector3,'r--')

plt.grid(True)
plt.xlabel('Numero de Terminos')
plt.ylabel('Error')

plt.show()
