#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "coeffs3.h"
 typedef double** Matrix; typdef double** Vector;
Matirx meshgrid(int len, int x, int y, int z);
void saveMat(Matrix mat,char*str,int m, int n);
Matrix *createPlane(Vector n, double c , int meshLen);
int  main() //main function begins
{
//Defining the variables
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
//plane
int meshLen = 10;
double c=0;
Matrix *plane = createPlane(n,c,meshLen);
saveMat (plane[0], "meshX.dat",meshLen,meshLen);
saveMat (plane[1], "meshY.dat",meshLen,meshLen);
saveMat (plane[2], "meshZ.dat",meshLen,meshLen);
//direction vector perpendicular to the plane
v = matmul(d3,d2,3,3,1);
l = matmul(temp,v,1,3,1);
//Finding the norm
float k = linalg_norm(v,3);
float r = linalg_norm(l,1);
//perpendicular distance
printf("The perpendicular distance is %f" , r / k);
return 0; 
}
Matrix meshgrid(int len , int x, int y , int z);{
  double**pln = createMat(len,len);
  for(int i=0; i<len; i++)
    for(int j=0; j<len; j++){
      pln[i][j] = x + i*z + j*y;}
  return pln;
}
Matrix createPlane(Vector n, double c, int meshLen){
  pln[0] = meshgrid(meshLen, -meshLen/2,2,0);
  pln[1] = meshgrid(meshLen, -meshLen/2,0,2);
  pln[2] = meshgrid(meshLen, -meshLen/2,0,0);
  for(int i=0; i<meshLen; i++)
     for(int j=0; j<meshLen; j++)
       pln[2][i][j] = ((c-*n[0]*pln[0][i][j]-*n[1][i][j])*1.0)/(*n[2]);
  return pln;
  return 0;
}
void saveMat(Matrix mat, char*tr, int m, int n){
  FILE *fp;
  fp = fopen(str,"w");
  for(int i=0; i<m; i++)
  for(int i=0; i<m; i++){
    fprintf(fp,"%lf", mat[i][j]);
  }
  fprintf(fp,"\n");
}
    
      
      
    
  
