#include <cs50.h>
#include <stdio.h>
void pattern(int x);

int main(void)
{
    int height;
    do
    {
        height = get_int("Height: ");
    }
    while (height < 1 || height > 8);
    // printf("%i\n", height); // For debugging
    pattern(height);
    return 0;
}

void pattern(int x)
{
    // To print the pyramid pattern
    for (int i = 1; i <= x; i++)
    {
        // The formula would be something like this - " "*(8-i) + "#" * (i) + "  " + "#"*i
        // We cant use like the formula directly as in python apparently.
        // We must use nested loops like in cs50 example of pattern
        for (int spaces = 0; spaces < x - i; spaces++)
            printf(" ");

        for (int hash1 = 0; hash1 < i; hash1++)
            printf("#");

        printf("  ");

        for (int hash2 = 0; hash2 < i; hash2++)
            printf("#");

        printf("\n");

        // This technically acted like string concatenation from python
    }
}

// Formatted using style50
