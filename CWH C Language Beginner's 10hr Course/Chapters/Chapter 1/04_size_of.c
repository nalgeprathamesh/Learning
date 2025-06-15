#include <stdio.h>

int main()
{
    printf("Size of int is: %zu bytes\n", sizeof(int));
    printf("Size of float is: %zu bytes\n", sizeof(float));
    printf("Size of char is: %zu byte\n", sizeof(char));
    return 0;
}

// sizeof is a reserved keyword in c. There are about 32 reserved keywords in c