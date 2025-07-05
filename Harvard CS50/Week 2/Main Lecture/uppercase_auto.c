#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h> //We have used this library to automate Capitalization(here)

int main(void)
{
    string s = get_string("Before: ");
    printf("After:  ");
    for (int i = 0, n = strlen(s); i < n; i++)
    {
        printf("%c", toupper(s[i]));
    }
    printf("\n");
}
// Styled using style50
