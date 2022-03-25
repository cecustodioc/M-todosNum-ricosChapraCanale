#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 00:39:00 2021
Compara los cálculos de un método analítico y uno numérico para el cálculo de la velocidad límite de un paracaidísta y los gráfica.
Problema 1.1 del libro Métodos Numéricos para Ingenieros de Chapra y Canale.
@author: cecustodioc
"""
# Se importan las librerias de gráficos
import matplotlib.pyplot as plt

# Se crean las variables y se les asignan los valores
a = 9.8  # Fuerza de gravedad en m/s
w = 68.1  # Peso del objeto en kgs
r = 12.5  # Resistencia del aire al objeto
e = 2.71828  # Constante de Napier
t = 0  # Tiempo inicial en segundos
i = 2  # Intervalo de tiempo en segundos
# Variables de control
v1 = 0; v2 = 1; vi = 0; vct = 1

# Vectores para guardar los cálculos 1 analíticos, 2 numéricos.
tc1 = []; vc1 = []; tc2 = []; vc2 = []

def vc (a, w, r, i, vi):  # Función numérica
    return vi+(a-(r/w)*vi)*i

def vt (a, w, r, t, e):  # Función analítica
    return ((a*w)/r)*(1-e**-((r/w)*t))

def ca (a, w, r, t, e, i, v1, v2): # Cálculos análiticos
    while v1 != v2:
        v1 = vt (a, w, r, t, e)
        vc1.append(v1)
        tc1.append(t)
        t = t + i
        v2 = vt (a, w, r, t, e)

def cn (a, w, r, t, i, vi, vct):  # Cálculos numéricos
    vc2.append(0)
    tc2.append(0)
    while vi != vct:
        vi = vc (a, w, r, i, vi)
        vc2.append(vi)
        t = t + i
        tc2.append(t)
        vct = vc(a, w, r, i, vi)

def graficar (vc1,vc2,tc1,tc2):
    # Grafica los valores tabulados que tienen equivalentes
    marcas = tc2[0::3]
    mapeado = range(len(marcas))
    plt.xticks(mapeado, marcas, rotation =270)
    plt.title('Comparación velocidades cálculadas')
    plt.ylabel('velocidad')
    plt.xlabel('tiempo')
    plt.xlim(0, len(marcas))
    plt.ylim(vc1[0], vc1[-1]+5)
    plt.plot(tc1, vc1, label="Analítico", marker = "o", color="blue", ls="-", lw="1")
    plt.plot(tc2, vc2, label="Numérico", marker = "x", color="red", ls="-.", lw="1")
    plt.legend()
    plt.show()
    
def tabla (vc1, tc1, vc2, tc2):
    # Tabula los valores calculados que tienen equivalentes
    nf = 0
    i = 0
    if len(tc1) < len(tc2):
        nf = len(tc1)
    else:
        nf = len(tc2)
    print ('cálculos --> analíticos: {} numéricos: {}'.format(len(tc1),len(tc2)))
    print('tiempo analí­tico numérico ')
    while i < nf:
        print('{0:6d} {1:3.4f} {2:3.4f}'.format(tc1[i], vc1[i], vc2[i]))  # Se da formato a la salida para facilitar su lectura
        i = i + 1

#Se invocan las funciones de cálculo analítico y numérico
ca (a,w,r,t,e,i,v1,v2)  # Calcular analí­ticamente
cn (a, w, r, t, i, vi, vct)  # Calcular numéricamente

# Se invoca la función que nos presenta la tabla comparativa.
tabla (vc1, tc1, vc2, tc2)

# Se crea una gráfica basada en la tabla comparativa
graficar (vc1, vc2, tc1, tc2)