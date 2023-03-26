from random import randint
from functools import reduce

print( )
print("Metoda nr 1")
print( )

# n = wysokosc tablicy galtona , r = ilosc pileczek

def galton(n, r):
    pudelka = [0] * (n + 1)
    for i in range(r):
        nr = 0
        for i in range(0, n): 
            wybor = randint(0, 1)
            if wybor == 1:
                nr += 1
        pudelka[nr] = pudelka[nr] + 1
    return pudelka

def wizual_galton(dane):
    for x in dane:
        for i in range(0, x):
            print('-', end='')
        print(x)

wizual_galton(galton(10, 200))

print( )
print("Metoda nr 2")
print( )

#drugi sposob (nie losowy)

def silnia(n):
    x = 1
    for i in range(1, n+1):
        x *=i
    return x

def sum(a, b):
    return a + b

def galton2(n, r):
    w = []
    o = []
    oo = []
    for a in range(n+1):
        for i in range(n+1):
            sn = silnia(n) // (silnia(i) * silnia(n-i))
            w.append(sn)
        wyn = w[a]
        o.append(wyn)
        oo.append(round(w[a]/2**n * r))        #2 do n-tej patrz trojkt pascala
    return oo                               



def wizual_galton2(dane):
    for x in dane:
        for i in range(0, x):
            print('-', end='')
        print(x)

wizual_galton2(galton2(10, 200)) 

print( )
print("Metoda nr 3")
print( )

def galton3(n):
    w = []
    o = []
    oo = []
    for a in range(n+1):
        for i in range(n+1):
            sn = silnia(n) // (silnia(i) * silnia(n-i))
            w.append(sn)
        wyn = w[a]
        o.append(wyn)
        oo.append(w[a])       
    return oo 

#print('galton3', galton3(10))

def sumowanie(d):
    w = reduce(sum, d)
    return w
#print('s', sumowanie(galton3(10)))  

def f(g, s, r):
    f = []
    for i in range(len(g)):
        f.append(g[i]/s*r)
    return f


#print('f', f(galton3(10), sumowanie(galton3(10)), 100))


def wizual_galton3(dane):
    for x in dane:
        for i in range(0, round(x)):  #round bo wartosci sa float a w wizualizacji nie mozna wyswietlic np 0.9765 myslnika
            print('-', end='')
        print(x)

wizual_galton3(f(galton3(10), sumowanie(galton3(10)), 200))


import matplotlib.pyplot as plt
import numpy as np

x1 = galton(10, 200)
x2 = galton2(10, 200)
x3 = f(galton3(10), sumowanie(galton3(10)), 200)
f, axs = plt.subplots(2, 2)


for row in axs:
    for plot in row:
        plot.set(xlim=(-1,11), xticks=np.arange(0,11),
       ylim=(0, 55), yticks=np.arange(0, 55, 10))


axs[0][0].bar(range(11), x1)
axs[0][1].bar(range(11), x2)
axs[1][0].bar(range(11), x3)


plt.show()

#test chi sprawdz czy sie nie wyklucza