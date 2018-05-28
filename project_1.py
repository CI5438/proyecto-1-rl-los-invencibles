"""
Universidad Simon Bolivar
Artificial Intelligence II - CI5438
Authors:
	David Cabeza 1310191
	Rafael Blanco 1310156
	Fabiola Martinez 1310838

Description: linear regression algorithm.

"""
import math
import sys
import random
import matplotlib.pyplot as plt

theta = [0,0]
features = []
x = []
y = []
global jota
jota = []
columns = 0
k = 0
max_it=20000

"""
Description: gets information about dataset.

Parameters:
	@param filename: name of de dataset file.
"""
def read_dataset(filename):
	del x[:]
	del y[:]
	dataset = open(filename, "r")

	i=0
	#columns=0

	for line in dataset:
		word = line.split()
		
		if word[0][0] != "#":
			i+=1
			if i == 1:
				columns = int(word[0])
				# print(columns)
			elif i == 2:
				rows = int(word[0])
				#print(rows)
					
				for j in range(columns):
					line = next(dataset)
					features.append(line.split())
			else:
				aux=[]
				for j in range(columns-1):
					if j==0:
						aux.append(1)
					else:
						aux.append(float(word[j]))
				x.append(aux)
				y.append(float(word[columns-1]))

	# for i in range(len(x)):	
	# 	for j in range (1,columns-1):
	# 		print(x[i][j], end=' ')
	# 	print(y[i])
	# print(" ")

"""
Description: normalizes the data.
"""
def norm():
	media=[1]
	for i in range(1,len(x[0])):
		aux=0
		for j in range(len(x)):
			aux+=x[j][i]
		media.append(aux/len(x))
	print("Media: ", media[1])
	varianza=[1]
	for i in range(1,len(x[0])):
		aux=0
		for j in range(len(x)):
			aux+=(x[j][i]-media[i])**2
		varianza.append((aux/(len(x)-1))**(1/2))

	print("varianza: ", varianza[1])
	for i in range(1,len(x[0])):
		for j in range(len(x)):
			x[j][i]=(x[j][i]-media[i])/varianza[i]

	# for i in range(len(x)):	
	# 	#print(columns)
	# 	for j in range (len(x[i])):
	# 		print(x[i][j], end=' ')
	# 	print(y[i])
	# print(" ")

"""
Description: gets information about dataset.

Parameters:
	@param theta: array with theta values.
	@param x: values of dataset variable.
"""
def h(theta, x):
	#print (float(theta[1])*float(x[1]))
	aux=0
	for i in range(len(theta)):
		aux+=theta[i]*x[i]
	return aux

"""
Description: calculates the cost function.

Parameters:
	@param theta: array with theta values.
	@param x: values of dataset variable.
	@param y: values of dataset variable.
"""
def jfunc(theta):
	plus=0
	for i in range(0, len(x)):
		plus += (h(theta, x[i]) - y[i])**2
	return (1/(2*len(x)))*plus

"""
Description: calculates the norm of a vector.

Parameters:
	@param x: values of dataset variable.
"""
def norm2(x):
	plus=0
	for i in range (0, len(x)):
		plus += x[i]**2
	#print(math.sqrt(plus))
	return math.sqrt(plus)

"""
Description: subtracts two vectors.

Parameters:
	@param a: a vector.
	@param b: a vector.
"""
def sub_vec(a,b):
	c=[]
	for i in range (0,len(a)):
		c.append(a[i]-b[i])
	return c

"""
Description: subtracts two vectors.

Parameters:
	@param a: a vector.
	@param b: a vector.
"""
def gradient_descent(alpha):
	theta_old=[]
	theta_new=[]
	epsilon=10**-3
	k=0
	del jota[:]

	for i in range(len(x[0])):
		theta_old.append(random.random()*100)
		theta_new.append(random.random()*100)

	jota.append(jfunc(theta_new))
	while(norm2(sub_vec(theta_new,theta_old))>epsilon and k<max_it): #condicion de convergencia
		
		for i in range(len(x[0])):
			theta_old[i] = theta_new[i]
			
		for i in range (0, len(theta_old)):
			plus=0
			for j in range (0, len(x)):
				#print(x[j][i])
				plus+=(h(theta_old, x[j])-y[j])*x[j][i]
				#plus+=(h(theta_old, x[j])-y[j])
			#print(alpha*(1/len(x))*plus)
			theta_new[i]=theta_old[i]-(alpha*(1/len(x))*plus)
		jota.append(jfunc(theta_new))
		k+=1
		#print("theta old", theta_old[0], theta_old[1])
		#print("theta new", theta_new[0], theta_new[1])

	for i in range(len(theta_new)):
		print("Theta ", i, ": ", theta_new[i])
	print("k: ", k)

	return theta_new


# filename = "x01.txt"
# read_dataset(filename)
# norm()
# theta_1 = gradient_descent(0.001)
# for i in range (len(x)):
# 	t.append(x[i][1])
# plt.plot(t)
# plt.ylabel('some numbers')
# plt.show()

