// Create an array for 5 elements and each double the previous one and the first starting with one

#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int numbers[5] = {1,2,3,4,5};

    numbers[0] = 1;

    for(int i = 1; i < 5; i++)
    {
        numbers[i] = numbers[i-1]*2;
    }
    // printf(numbers[0]);

    for(int j = 0; j < 5; j++)
    {
        printf("%d\n",numbers[j]);
    }
}




