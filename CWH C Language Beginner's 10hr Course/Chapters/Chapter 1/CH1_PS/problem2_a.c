// Calculate the a) area of circle
#include <stdio.h>

int main(){
    int radius;
    scanf("%d", &radius);   //Dont forget &
    printf("The area of the circle is %f\n", radius*radius*(3.14));
    return 0;
}

// Note: we have used %f here bcz its a float