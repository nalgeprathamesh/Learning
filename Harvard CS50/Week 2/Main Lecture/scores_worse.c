#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int N = 3;
    int scores[N];
    scores[0] = 23;
    scores[1] = 32;
    scores[2] = 21;
    printf("The average of following numbers is %f.\n",(scores[0]+scores[1]+scores[2])/(float) N);
}
