#include <cs50.h>
#include <stdio.h>

void meow(int n); // Declaring this function early so that it can be used inside the main function
int get_positive_number(void);

int main(void)
{
    // We will use while loop here
    //  int i = 0;
    //  while (i < 3)
    //  {
    //      printf("Meow\n");
    //      i++;
    //  }
    // For permanently printing 'cat' we can use while loop
    //  while (true)
    //  {
    //      printf("cat\n");
    //  }

    // We can use for loop in the following way
    //  for(int i=0; i<3; i++)
    //  {
    //      printf("Meow\n");
    //  }

    // We can also use an function that we can call eventually
    // int x = get_int("Enter the number: ");

    // We can also use do-while loop to prompt user to enter positive value only
    // int x; //We have declared the variable early so that it's scope is global inside the main
    // func() do
    // {
    //     x = get_int("Enter the number: ");
    // }
    // while (x < 1);
    int times = get_positive_number();
    meow(times);
}

int get_positive_number(void)
{
    int x;
    do
    {
        x = get_int("Enter the number: ");
    }
    while (x < 1);
    return x;
}

void meow(int n) // We have initialzed a function here
{
    for (int i = 0; i < n; i++)
    {
        printf("meow\n");
    }
    // meow(1);   Tried to call a recursive function but recieved an error
}

// Formatted using style50
