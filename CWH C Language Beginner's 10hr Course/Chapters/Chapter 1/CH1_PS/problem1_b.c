// Write a c program to calculate area of rectangle
// b)Using user input
#include <stdio.h>

int main()
{
    int length;
    scanf("%d", &length);  //Dont forget the address(&) of operator
    int breadth;
    scanf("%d", &breadth);

    int area;
    area = length*breadth;
    printf("The area of the rectangle is %d \n", area);
    // We can just directly do this
    printf("The area of the rectangle is %d \n", length*breadth);
    return 0;
}