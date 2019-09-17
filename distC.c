#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "coeffs3.h"

int  main() //main function begins
{
//Defining the variables
//integers
double **A, **B, **P, **d2, **d3,  **x1, **temp, **v, **l;

//Given points
A = loadtxt("./data/A.dat",3,1);
B = loadtxt("./data/B.dat",3,1);
P = loadtxt("./data/P.dat",3,1);

//Matrix equation
d3 = loadtxt("./data/d3.dat",3,3);
x1 = linalg_sub(P,A,3,1);
temp = transpose(x1,3,1);

//direction vector in the plane 
d2 = linalg_sub(P,B,3,1);

//direction vector perpendicular to the plane
v = matmul(d3,d2,3,3,1);
l = matmul(temp,v,1,1,0);

//Finding the norm
float r = linalg_norm(v,3);
float k = linalg_norm(l,1);
//perpendicular distance
printf("The perpendicular distance is %f" , r / k);
return 0; 
}
