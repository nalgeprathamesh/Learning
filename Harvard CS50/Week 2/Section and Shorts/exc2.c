// Check if a lowercase string's characters are in alphabetical order. If yes, print "yes". If no
// print "no"

#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    string order = get_string("Enter the String: ");
    char list[strlen(order) + 1];

    for (int i = 0; i < strlen(order); i++)
    {
        list[i] = order[i];
    }

    int VSum = 0;
    // Now check if they are in alphabetical order using ASCII
    for (int j = 1; j < strlen(order); j++)
    {
        if (list[j] > list[j - 1])
        {
            VSum += 1;
        }
        else
        {
            VSum -= 1;
        }
    }

    // printf("%i", VSum);
    if (VSum == (strlen(order) - 1))
    {
        printf("Yes\n");
    }
    else
    {
        printf("No\n");
    }
    // printf("%c\n%C\n%C\n%C\n%c", list[0], list[1], list[2], list[3],list[4]);
}

// A better version should have been use boolean and if last element is greater than current
// we can change the bool = false and then break.
