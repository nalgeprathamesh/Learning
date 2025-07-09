#include <stdio.h>

float multiply_two_floats(float a, float b);

int main(void)
{
    float mul = multiply_two_floats(1.5,3.0);
    printf("%f\n", mul);
}

float multiply_two_floats(float a, float b)
{
    return a*b;
}
