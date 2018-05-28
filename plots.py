"""
Universidad Simon Bolivar
Artificial Intelligence II - CI5438
Authors:
	David Cabeza 1310191
	Rafael Blanco 1310156
	Fabiola Martinez 1310838
"""

import math
import sys
import random
import matplotlib.pyplot as plt
import numpy as np 
from project_1 import *

def plotScatter(x_1,y_1,xlabel,ylabel,title,x_2,y_2):
	plt.scatter(x_1, y_1)
	plt.plot(x_2, y_2, c="#A4243B")
	plt.xlabel(xlabel)
	plt.ylabel(ylabel)
	plt.title(title)
	plt.show()

def plotNormal(x,y,xlabel,ylabel,title):
	plt.plot(x,y)
	plt.xlabel(xlabel)
	plt.ylabel(ylabel)
	plt.title(title)
	plt.show()

# 2.1) ------------------------------------------------------------------------

filename1 = "x01.txt"
read_dataset(filename1)

# Without normalized the data -------------------------------------------------

# Question a) -----------------------------------------------------------------

# Question b) -----------------------------------------------------------------

# Normalized data -------------------------------------------------------------

norm()
results = []
results = gradient_descent(0.001)
x_2 = []

# Question a) -----------------------------------------------------------------

iterations = np.arange(len(jota))
plotNormal(iterations, jota,"Iteraciones", "J()", "Curva de Convergencia")

# Question b) -----------------------------------------------------------------

x_1 = []
y_1 = []

for i in range(0, len(y)):
	print(y[i])

for i in range(len(x)):
	x_1.append(x[i][1])
	y_1.append(results[0] + results[1]*x[i][1])

plotScatter(x_1,y,"Brain Weight", "Body Weight", "Exercise 2.1.b", x_1,y_1)

# 2.2) ------------------------------------------------------------------------

filename1 = "x08.txt"
read_dataset(filename1)