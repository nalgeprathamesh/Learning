#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int x = get_int("Enter x: ");
    int y = get_int("Enter y: ");

    printf("%.50f\n", (float) x/y);  //We have used %.xf here where x is number of digits i want after decimal
}
