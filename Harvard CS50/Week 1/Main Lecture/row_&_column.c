#include <cs50.h>
#include <stdio.h>

int main(void)
{
    for (int row = 0; row < 3; row++) // This prints a row
    {
        for (int column = 0; column < 3;
             column++) // This prints a column and is inside another for loop
        {
            printf("#");
        }
        printf("\n"); // Generate a new line to make new rows
    }
}

//We could have also used a function like generate_row and used it but it was not needed since it was a simple example.
//Style50 was used to format
