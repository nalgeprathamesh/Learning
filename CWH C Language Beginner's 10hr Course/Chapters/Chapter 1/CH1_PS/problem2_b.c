// Calculate the area b)Cylinder
#include <stdio.h>

int main(){
    printf("Enter the Radius: ");
    int radius;
    scanf("%d", &radius);   //Dont forget &
    printf("Enter the Height: ");
    int height;
    scanf("%d", &height);
    printf("The area of the cylinder is %f\n", radius*radius*(3.14)*height);
    return 0;
}