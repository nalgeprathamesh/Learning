#include <stdio.h>
#include <cs50.h>

int main(void)
{
    const int N = 4; //We have used const here so that it's value cannot be changed later in the code unlike int whose value can be updated
    int scores[N];

    for(int i = 0; i < N; i++)
    {
        scores[i] = get_int("Enter the number: ");
    }
    printf("The average of following numbers is %f.\n",(scores[0]+scores[1]+scores[2]+scores[3])/(float) N);
}
