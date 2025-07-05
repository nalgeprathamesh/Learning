#include <cs50.h>
#include <stdio.h>

float average(int length, int array[]); // Prototype

int main(void)
{
    const int N = get_int(
        "Enter how many numbers you want to calculate average of : "); // Pre declaring const
    // We cant get input outside of function
    int scores[N];

    for (int i = 0; i < N; i++)
    {
        scores[i] = get_int("Enter the number: ");
    }
    printf("The average of following numbers is %f.\n", average(N, scores));
}

float average(int length, int array[])
{
    int sum = 0;
    for (int i = 0; i < length; i++)
    {
        sum += array[i];
    }
    return sum / (float) length;
}
