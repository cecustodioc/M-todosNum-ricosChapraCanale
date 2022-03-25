#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 03:26:33 2021
Aproximadamente, 60% del peso total del cuerpo corresponde al agua. Si
se supone que es posible separarla en seis regiones, los porcentajes
serían los que siguen. Al plasma corresponde 4.5% del peso corporal y
7.5% del total del agua en el cuerpo. Los tejidos conectivos densos y
los cartílagos ocupan 4.5% del peso total del cuerpo y 7.5% del total de
agua. La linfa intersticial equivale a 12% del peso del cuerpo y 20% del
total de agua en éste. El agua inaccesible en los huesos es
aproximadamente 7.5% del total de agua corporal y 4.5% del peso del
cuerpo. Si el agua intracelular equivale a 33% del peso total del cuerpo
y el agua transcelular ocupa 2.5% del total de agua en el cuerpo. ¿qué
porcentaje del peso total corporal debe corresponder al agua
transcelular? ¿qué porcentaje del total de agua del cuerpo debe ser el
del agua intracelular?
@author: cecustodioc
"""
# Para resolver este problema primero debemos establecer las constantes del problema (datos conocidos)
PCT_PESO_AGUA = .60
PCT_PESO_OTROS = .40
PCT_PESO_PLASMA = .045
PCT_AGUA_PLASMA = .075
PCT_PESO_TEJIDOS_CONECTIVOS_CARTILAGOS = .045
PCT_AGUA_TEJIDOS_CONECTIVOS_CARTILAGOS = .075
PCT_PESO_LINFA_INTERSTICIAL = .12
PCT_AGUA_LINFA_INTERSTICIAL = .20
PCT_PESO_AGUA_INACCESIBLE_HUESOS =.045
PCT_AGUA_INACCESIBLE_HUESOS = 0.075
pct_peso_agua_transcelular = 0  # Valor a calcular
PCT_AGUA_TRANSCELULAR = 0.025
PCT_PESO_AGUA_INTRACELULAR = 0.33
pct_agua_intracelular = 0  # Valor a calcular

# para conocer los valores faltantes debemos de calcular la relación entre peso del agua y porcentaje de agua.

pct_peso_agua_transcelular = PCT_PESO_AGUA - PCT_PESO_PLASMA - PCT_PESO_TEJIDOS_CONECTIVOS_CARTILAGOS - PCT_PESO_LINFA_INTERSTICIAL - PCT_PESO_AGUA_INACCESIBLE_HUESOS - PCT_PESO_AGUA_INTRACELULAR

pct_agua_intracelular = 1.0 - PCT_AGUA_PLASMA - PCT_AGUA_TEJIDOS_CONECTIVOS_CARTILAGOS - PCT_AGUA_LINFA_INTERSTICIAL - PCT_AGUA_INACCESIBLE_HUESOS - PCT_AGUA_TRANSCELULAR

# Se presentan los resultados de los cálculos
print('El agua transcelular representa un {0:1.1f}% del peso total, mientras que el agua intracelular representa un {1:1.1f}% del peso del agua'.format(pct_peso_agua_transcelular*100, pct_agua_intracelular*100))

# Imprimir el gráfico de la solución obtenida.

import matplotlib.pyplot as plt
figura = plt.figure(figsize=(7,5))

composicion_total = [PCT_PESO_PLASMA, PCT_PESO_TEJIDOS_CONECTIVOS_CARTILAGOS, PCT_PESO_LINFA_INTERSTICIAL, PCT_PESO_AGUA_INACCESIBLE_HUESOS, PCT_PESO_AGUA_INTRACELULAR, pct_peso_agua_transcelular, PCT_PESO_OTROS]
nombres_total = ["Plasma", "Tejidos conectivos y cartilagos", "Linfa Intersticial", "Inaccesible en los huesos", "Intracelular", "Transcelular", "Parte sólida"]
colores_total = ["cadetblue", "skyblue", "powderblue", "lightskyblue", "steelblue", "aqua", "burlywood"]
desfase = (0.01, 0.01, 0.01, 0.01, 0.01, 0.1, 0.01)
grafico1 = figura.add_subplot(2, 1, 1)
grafico1.set_title("PORCENTAJE DE PESO CORPORAL")
grafico1.pie(composicion_total, labels=nombres_total, autopct="%0.1f %%", colors=colores_total, explode=desfase)
grafico1.axis("equal")

composicion_agua = [PCT_AGUA_PLASMA, PCT_AGUA_TEJIDOS_CONECTIVOS_CARTILAGOS, PCT_AGUA_LINFA_INTERSTICIAL, PCT_AGUA_INACCESIBLE_HUESOS, pct_agua_intracelular, PCT_AGUA_TRANSCELULAR]
nombres_agua = ["Plasma", "Tejidos conectivos y cartilagos", "Linfa Intersticial", "Inaccesible en los huesos", "Intracelular", "Transcelular"]
colores_agua = ["cadetblue", "skyblue", "powderblue", "lightskyblue", "steelblue", "aqua"]
desfase = (0.01, 0.01, 0.01, 0.01, 0.1, 0.01)
grafico2 = figura.add_subplot(2, 1, 2)
grafico2.set_title("PORCENTAJE DE VOLUMEN DE AGUA")
grafico2.pie(composicion_agua, labels=nombres_agua, autopct="%0.1f %%", colors=colores_agua, explode=desfase)
grafico2.axis("equal")

figura.subplots_adjust(hspace=0.5, wspace=1)
figura.show()