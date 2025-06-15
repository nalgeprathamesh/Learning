// Write a program to convert celsius to farnheit

#include <stdio.h>

int main(){
    printf("Enter the temperature in celsius: ");
    float celsius;
    scanf("%f", &celsius);
    printf("%f degree celsius in farnheit is %f degrees\n" , celsius, ((celsius*1.8)+32));
    return 0;
}