#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    string s = get_string("Before: ");
    printf("After:  ");
    for (int i = 0, n = strlen(s); i < n; i++)
    {
        if (s[i] >= 'a' && s[i] <= 'z') // This is the syntax to check if string elements are in
                                        // certain range of ASCII Codes
        {
            // Change s[i] to uppercase
            printf("%c", s[i] - ('a' - 'A')); // We have used ASCII reference here bcz small and
                                              // capital words are at difference of 32 numbers
            // But we have tried to automate the 32 number to more human readable code
        }
        else
        {
            printf("%c", s[i]); // Print the letters which were already capital
        }
    }
    printf("\n");
}
// Styled using style50
