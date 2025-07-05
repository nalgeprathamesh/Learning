#include <stdio.h>
#include <cs50.h>

int main(void)
{
    string name = get_string("Enter your name: ");

    int n = 0;
    while(name[n] != '\0') // \0 is basically the last word after string ends . it is basically called NUL in ASCII and it marks end of string
    {
        n++;
    }
    printf("%i\n", n);
}
