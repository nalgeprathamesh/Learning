// Write a c program to calculate area of rectangle
// a)Using hard coded input
#include <stdio.h>

int main()
{
    int length;
    length = 2;
    int breadth;
    breadth = 5;

    int area;
    area = length*breadth;
    printf("The area of the rectangle is %d \n", area);
    // We can just directly do this
    printf("The area of the rectangle is %d \n", length*breadth);
    return 0;
}