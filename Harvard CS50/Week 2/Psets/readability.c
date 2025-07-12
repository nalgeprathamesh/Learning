#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    // Input from user
    string text = get_string("Text: ");

    // Checking spaces
    int spaces = 0;
    for (int i = 0; i < strlen(text); i++)
    {
        if (isspace(text[i]))
        {
            spaces++;
        }
    }
    // printf("%i", spaces);

    // Breaking into words like words = spaces + 1
    int words = spaces + 1;
    // printf("%i", words);

    // finding total letters from left to right excluding numbers, spaces, etc and just adding
    // letter +=
    int letters = 0;
    for (int k = 0; k < strlen(text); k++)
    {
        if (isalpha(text[k])) // checks if it is only letters
        {
            letters++;
        }
    }
    // printf("%i", letters);

    // find total sentences by checking how many symbols like . and ! are there
    int sentences = 0;
    for (int j = 0; j < strlen(text); j++)
    {
        if (text[j] == '.' || text[j] == '!' ||
            text[j] == '?') // This checks if it contains .,! and ?
            sentences++;
    }

    // printf("%i\n", spaces);
    // printf("%i\n", words);
    // printf("%i\n", letters);
    // printf("%i\n", sentences);

    // Implement Coleman-Liau formula which is
    // index = 0.0588 * L - 0.296 * S - 15.8
    float S = ((float) sentences / words) * 100;
    float L = ((float) letters / words) * 100;
    float index = (0.0588 * L) - (0.296 * S) - 15.8;
    // printf("%f", index);

    // using if-else conditions check if the reading level is more than 16 or less than 1
    // Also round up or down the grade level
    int level = round(index);
    if (level < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (level > 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", level);
    }
}
