"""
Universidad Simon Bolivar
Artificial Intelligence II - CI5438
Authors:
	David Cabeza 1310191
	Rafael Blanco 1310156
	Fabiola Martinez 1310838
"""

import math # useful for mathematical operators
import sys 
import random # useful for random function
import matplotlib.pyplot as plt # useful for tools for graphics.
import matplotlib.patches as mpatches # useful tools for graphics.
import numpy as np # useful for arrays
from project_1 import * # main file

"""
Description: graphics a scatter and a plot with some details.

Parameters:
	@param x_1: abscissa's values.
	@param y_1: ordinates's values.
	@param xlabel: label for the first coordinate.
	@param ylabel: label for the second coordinate.
	@param title: name of the graphic.
	@param x_2: abscissa's values for made a line.
	@param y_2: ordinates's values for made a line.
"""
def plotScatter(x_1,y_1,xlabel,ylabel,title,x_2,y_2):
	plt.scatter(x_1, y_1)
	plt.plot(x_2, y_2, c="#A4243B")
	plt.xlabel(xlabel)
	plt.ylabel(ylabel)
	plt.title(title)
	plt.show()

"""
Description: graphics a scatter and a plot with some details.

Parameters:
	@param x: abscissa's values for made a line.
	@param y: ordinates's values for made a line..
	@param xlabel: label for the first coordinate.
	@param ylabel: label for the second coordinate.
	@param title: name of the graphic.
	@param color: color of the line.

"""
def plotNormal(x,y,xlabel,ylabel,title, color):
	plt.xlabel(xlabel)
	plt.ylabel(ylabel)
	plt.title(title)
	plt.plot(x,y,c=color)

# # 2.1) ------------------------------------------------------------------------

filename1 = "x01.txt"
read_dataset(filename1)

# # Without normalized the data -------------------------------------------------

results1 = []
results1 = gradient_descent(0.001)

# # # # Question a) -----------------------------------------------------------------

iterations = np.arange(len(jota))
plotNormal(iterations, normV(jota),"Iteraciones", "J()", "Curva de Convergencia","#0174DF")
plt.show()

# # Normalized data -------------------------------------------------------------

norm()
results2 = []
results2 = gradient_descent(0.001)

# # Question a) -----------------------------------------------------------------

# iterations = np.arange(len(jota))

plotNormal(iterations, jota,"Iteraciones", "J()", "Curva de Convergencia","#0174DF")
plt.show()

# # Question b) -----------------------------------------------------------------

x_1 = []

x_2 = [-1,7]

for i in range(len(x)):
	x_1.append(x[i][1])

y_2=[results2[0]+results2[1]*-1,results2[0]+results2[1]*7]

plotScatter(x_1,y,"Brain Weight", "Body Weight", "Exercise 2.1.b", x_2,y_2)

# 2.2) ------------------------------------------------------------------------

filename2 = "x08.txt"
read_dataset(filename2)

# Question a) -----------------------------------------------------------------

gradient_descent(0.001)
iterations = np.arange(len(jota))

for i in range(0,len(jota)):
	print(jota[i])

plotNormal(iterations, jota,"Iteraciones", "J()", "Curva de Convergencia","#0174DF")
plt.show()

# Question b) -----------------------------------------------------------------

norm()
c = 0
alphas = [0.001,0.005,0.01,0.05,0.1,1]
colors = ["#A4243B","#0174DF","#6A0888","#74DF00","#FF8000","#FFFF00"]

for i in range(0,len(alphas)):
	gradient_descent(alphas[i])
	iterations = np.arange(len(jota))
	plotNormal(iterations, jota,"Iteraciones", "J()", "Curva de Convergencia",colors[c])
	c += 1

legend1 = mpatches.Patch(color=colors[0],label=alphas[0])
legend2 = mpatches.Patch(color=colors[1],label=alphas[1])
legend3 = mpatches.Patch(color=colors[2],label=alphas[2])
legend4 = mpatches.Patch(color=colors[3],label=alphas[3])
legend5 = mpatches.Patch(color=colors[4],label=alphas[4])
legend6 = mpatches.Patch(color=colors[5],label=alphas[5])
plt.legend(handles=[legend1, legend2,legend3,legend4,legend5,legend6])
plt.show()
