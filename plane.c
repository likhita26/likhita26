#include <stdio.h>
#include <stdlib.h>
#include <math.h>

//Function to find the equation of the plane
void equation_plane(float x1, float y1,  
                    float z1, float x2,
                    float y2, float z2,  
                    float x3, float y3, float z3)
{
    float a1 = x2 - x1;
    float b1 = y2 - y1;
    float c1 = z2 - z1;
    float a2 = x3 - x1;
    float b2 = y3 - y1;
    float c2 = z3 - z1;
    float a = b1 * c2 - b2 * c1;
    float b = a2 * c1 - a1 * c2;
    float c = a1 * b2 - b1 * a2;
    float d = (- a * x1 - b * y1 - c * z1);
    printf("equation of plane is %.2f x + %.2f"
        " y + %.2f z + %.2f = 0.",a,b,c,d);
    return;
} 
// Driver Code
int main()
{
    float x1 = 1;
    float y1 = 2;
    float z1 = 3;
    float x2 = 1;
    float y2 = 1;
    float z2 = 0;
    float x3 = 3;
    float y3 = 2;
    float z3 = 4;
    equation_plane(x1, y1, z1, x2, y2, z2, x3, y3, z3);
    return 0;
   
}
