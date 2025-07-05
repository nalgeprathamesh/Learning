#include <stdio.h>
#include <cs50.h>
#include <string.h>

int main(void)
{
    string name = get_name("Name: ");
    int length = strlen(name); // strlen is used by string.h
    printf("%i\n", length);
}
