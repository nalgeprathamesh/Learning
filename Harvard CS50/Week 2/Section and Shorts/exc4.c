// Using a function verify is the triangle is valid or not
#include <cs50.h>
#include <stdio.h>

bool valid_triangle(int a, int b, int c);

int main(void)
{
    int side1, side2, side3;
    // Check whether the value is positive and if so check if its valid triangle
    do
    {
        side1 = get_int("Enter the 1st length: ");
        side2 = get_int("Enter the 2nd length: ");
        side3 = get_int("Enter the 3rd length: ");
        bool ans = valid_triangle(side1, side2, side3);
        if (ans == 1) // bool returns 1 if it is true
        {
            printf("This triangle is Valid\n");
        }
        else
        {
            printf("This triangle is not Valid\n");
            break;
        }
    }
    while (side1 < 0 || side2 < 0 || side3 < 0);
}

// bool is an cs50 library function so it wont work elsewhere directly
// but we can use stdbool.h anyways
bool valid_triangle(int a, int b, int c)
{
    bool valid;
    if (a + b > c && b + c > a && c + a > b)
    {
        valid = true; // True does not work it is case sensitive
    }
    else
    {
        valid = false;
    }
    return valid; // Returns 0 or 1
}
