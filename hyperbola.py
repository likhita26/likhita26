#Program to plot the required hyperbola
import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA

#if using termux
import subprocess
import shlex
#end if

#setting up plot
fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal')
len = 1000
theta = np.linspace(-5,5,len)

#Given hyperbola parameters
#Eqn : x.T@V@x = F
V = np.array(([3,0],[0,-4]))
F = 72

eigval,eigvec = LA.eig(V)

D = np.diag(eigval)
P = eigvec
print("D=\n",D)
print("P=\n",P)


#Generating points on the hyperbola at origin
y = np.zeros((2,len))
y[0,:] = 1/eigval[0]*np.cosh(theta)
y[1,:] = 1/eigval[1]*np.sinh(theta)

#Standard hyperbola : y.T@D@y=1
y1 = np.linspace(-2,2,len)
y2 = np.sqrt((1-D[0,0]*np.power(y1,2))/(D[1,1]))
y3 = -1*np.sqrt((1-D[0,0]*np.power(y1,2))/(D[1,1]))
y = np.hstack((np.vstack((y1,y2)),np.vstack((y1,y3))))

#Affine Transformation
#Equation : y = P.T@(x-c)/(K**0.5)
x = (P @ (y)) * F**0.5

#Plotting required hyperbola
plt.plot(x[0,:len],x[1,:len],color='r',label='Hyperbola')
plt.plot(x[0,len+1:],x[1,len+1:],color='r')

#Plotting the Normal
P = np.array([0,7*np.sqrt(3)]) 
A = np.array([3.5*np.sqrt(15),0])
C = np.array([np.sqrt(60),np.sqrt(27)])
D = np.array([-np.sqrt(60),np.sqrt(27)]) 
O = np.array([0,0])
len =10

x_PA= np.zeros((2,len))
lam = np.linspace(-1,1,len)
for i in range(len):
  temp1 = P + lam[i]*(P-A)
  x_PA[:,i]= temp1.T
  
  
#Plotting the Normal
P = np.array([0,7*np.sqrt(3)]) 
B = np.array([-3.5*np.sqrt(15),0]) 
len =10

x_PB= np.zeros((2,len))
lam = np.linspace(-1,1,len)
for i in range(len):
  temp1 = P + lam[i]*(P-B)
  x_PB[:,i]= temp1.T


#PLotting the point on the hyperbola 
plt.plot(C[0], C[1], 'o')
plt.text(C[0] * (1 + 0.1), C[1] * (1 - 0.1) , 'C') 
plt.plot(D[0], D[1], 'o')
plt.text(D[0] * (1 + 0.1), D[1] * (1 - 0.1) , 'D') 
plt.plot(O[0], O[1], 'o')
plt.text(O[0] * (1 + 0.1), O[1] * (1 - 0.1) , 'O') 

#Plotting the axes
X = np.array([50,0])
V = np.array([-50,0])
N = np.array([0,50])
K = np.array([0,-50])

x_XV= np.zeros((2,len))
lam = np.linspace(-1,1,len)
for i in range(len):
  temp1 = X + lam[i]*(X-V)
  x_XV[:,i]= temp1.T
x_NK= np.zeros((2,len))
lam = np.linspace(-1,1,len)
for i in range(len):
  temp1 = N + lam[i]*(N-K)
  x_NK[:,i]= temp1.T

plt.plot(x_XV[0,:],x_XV[1,:],label='$X-AXIS$')
plt.plot(x_NK[0,:],x_NK[1,:],label='$Y-AXIS$')

 
#PLotting the Lines on the hyperbola
plt.plot(x_PA[0,:],x_PA[1,:],label='$Normal1$')
plt.plot(x_PB[0,:],x_PB[1,:],label='$Normal2$')

plt.grid() 
ax.plot()
plt.xlabel('$x$');plt.ylabel('$y$')
plt.legend(loc='best')
plt.axis('equal')

# #if using termux
#plt.savefig('../figs/hyperbola.pdf')
#plt.savefig('../figs/hyperbola.eps')
#subprocess.run(shlex.split("termux-open ../figs/hyperbola.pdf"))
#else

plt.show()
