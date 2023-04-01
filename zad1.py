#Zadanie 1. Napisz funkcję obliczającą i zwracającą ilość potrzebnych opakowań paneli
# w danym pomieszczeniu, zakładając prostokątną podłogę i prostokątne panele.
# Dane wejściowe to długość i szerokość podłogi,
# (do powierzchni pomieszczenia należy dodać 10%)
# długość i szerokość panela oraz ilość paneli w opakowaniu. (10%)

import math

def zad1(dlugoscPodlogi, szerokoscPodlogi, dlugoscPanela, szerokoscPanela, iloscPaneli):
    powierzchniaPomieszczenia = dlugoscPodlogi*szerokoscPodlogi*1.1
    powierzchniaPanela = dlugoscPanela*szerokoscPanela

    paneleNaPomieszczenie =  powierzchniaPomieszczenia/powierzchniaPanela
    iloscOpakowan =  math.ceil(paneleNaPomieszczenie/iloscPaneli)

    return iloscOpakowan

print(zad1(4,4,0.20,1,10))