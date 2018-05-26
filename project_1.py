"""
Universidad Simon Bolivar
Artificial Intelligence II - CI5438
Authors:
	David Cabeza 1310191
	Rafael Blanco
	Fabiola Martinez 1310838
"""
import math
import sys

theta = [0,0]
features = []
x = []
y = []
columns=0

def read_dataset(filename):
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
				# print(rows)
					
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

	for i in range(len(x)):	
		for j in range (1,columns-1):
			print(x[i][j], end=' ')
		print(y[i])
	print(" ")

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

	for i in range(len(x)):	
		#print(columns)
		for j in range (len(x[i])):
			print(x[i][j], end=' ')
		print(y[i])
	print(" ")


def h(theta, x):
	#print (float(theta[1])*float(x[1]))
	return (theta[0] + theta[1]*x[1])

def j(theta, x, y):
	plus=0
	for i in range (0, len(x)):
		plus += (h(theta, x[i]) - y[i])**2
	return (1/(2*n))*plus

def norm2(x):
	plus=0
	for i in range (0, len(x)):
		plus += x[i]**2
	#print(math.sqrt(plus))
	return math.sqrt(plus)

def sub_vec(a,b):
	c=[]
	for i in range (0,len(a)):
		c.append(a[i]-b[i])
	return c

def gradient_descent(alpha):
	theta_old=[0,0]
	theta_new=[10,10]
	epsilon=10**-5
	k=0
	#print(x[1][1]*x[1][0])
	while(norm2(sub_vec(theta_new,theta_old))>epsilon): #condicion de convergencia
		theta_old[0]=theta_new[0]
		theta_old[1]=theta_new[1]
		for i in range (0, len(theta_old)):
			plus=0
			for j in range (0, len(x)):
				#print(x[j][i])
				plus+=(h(theta_old, x[j])-y[j])*x[j][i]
				#plus+=(h(theta_old, x[j])-y[j])
			#print(alpha*(1/len(x))*plus)
			theta_new[i]=theta_old[i]-(alpha*(1/len(x))*plus)
		k+=1
		#print("theta old", theta_old[0], theta_old[1])
		#print("theta new", theta_new[0], theta_new[1])
	print(theta_new[0], theta_new[1], k)



filename = "x01.txt"
read_dataset(filename)
norm()
gradient_descent(0.001)

#import matplotlib.pyplot as plt
#t=[]
#for i in range (len(x)):
#	t.append(x[i][1])
#plt.plot(t)
#plt.ylabel('some numbers')
#plt.show()