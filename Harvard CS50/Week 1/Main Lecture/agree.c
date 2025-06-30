#include <cs50.h>
#include <stdio.h>

int main()
{
    char decision = get_char("Do you agree(y/n)? ");
    if (decision == 'y' || decision == 'Y')
    { // The || is used for the logical OR operator
        printf("You Agreed\n");
    }
    else if (decision == 'n' || decision == 'N')
    {
        printf("You Disagreed\n");
    }
    else
    {
        printf("Invalid Decision\n");
    }
}
