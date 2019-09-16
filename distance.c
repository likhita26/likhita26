//Perpendicular(shortest) distance between a point and a Plane in 3 D.
#include <stdio.h>
#include <math.h>


// Function to find distance
void shortest_distance(float x1, float y1,  
                       float z1, float a,
                       float b, float c,  
                       float d)
{
    d = fabs((a * x1 + b * y1 + c * z1 + d));
    float e = sqrt(a * a + b * b + c * c);
    printf("Perpendicular distance is %f" , d / e);
        return;
}
 
 

// Driver Code
int main()
{
    float x1 = 3;
    float y1 = 1;
    float z1 = 1;
    float a = -1;
    float b = -6;
    float c = 2;
    float d = 7;
 
    // Function call
    shortest_distance(x1, y1, z1, a, b, c, d);
} 
