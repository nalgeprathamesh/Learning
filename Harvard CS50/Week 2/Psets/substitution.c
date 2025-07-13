#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, string argv[])
{
    // Check if the key is provided as a command-line argument
    // If not, print "Usage: ./substitution key" and exit with code 1
    string pre_key; // declared it here to make it accessible everywhere
    if (argc == 2)
    {
        pre_key = argv[1];
        // printf("%s\n", pre_key); Was for debugging
    }
    else
    {
        printf("Usage: ./substitution key\n");
        exit(1);
    }

    // Validate the key:
    // - Must contain exactly 26 characters
    if (strlen(pre_key) == 26)
    {
        // Continue
    }
    else
    {
        printf("Key must contain 26 characters.\n");
        exit(1); // Tried to enter custom exit code(26)(to check using echo $?) but check50 throwed
                 // an error... so removed it
    }
    // - No repeated letters (case-insensitive)
    for (int i = 0; i < strlen(pre_key); i++)
    {
        for (int j = i + 1; j < strlen(pre_key); j++)
        {
            if (tolower(pre_key[i]) ==
                tolower(pre_key[j])) // YThis will check all the possibilities one by one
            {
                printf("Key must not contain repeated characters.\n");
                exit(1);
            }
            else
            {
                // Continue
            }
        }
    }

    // - All characters must be alphabetic
    for (int i = 0; i < strlen(pre_key); i++)
    {
        if (isalpha(pre_key[i]))
        {
            // Continue
        }
        else
        {
            printf("Enter Alphabetical Characters only.");
            exit(1);
        }
    }

    // Get the user input
    string user_input = get_string("plaintext: ");

    // Convert plaintext to ciphertext:
    //- For each character:
    //- Find it;s index from 0 to 25 using char from user input - 'A' which will give the value
    //- Use the index to get the substitute from the key
    //- Make different cases for uppercase/lowercase stuff
    //- If it's not a letter leave it as it is

    printf("ciphertext: "); // Check50 throwed error for writing 'Ciphertext'
    for (int i = 0; i < strlen(user_input); i++)
    {
        char c = user_input[i];

        if (isupper(c))
        {
            int pos =
                c - 'A'; // gives value 0 to 25 which we can use to access position from pre_key
            char substitute = toupper(pre_key[pos]); // access any number from 0 to 25 using pos
            printf("%c", substitute);
        }
        else if (islower(c))
        {
            int pos = c - 'a';
            char substitute = tolower(pre_key[pos]);
            printf("%c", substitute);
        }
        else
        {
            // for non-alphabetical character print as it was.
            printf("%c", c);
        }
    }

    printf("\n");

    // Print "ciphertext: " followed by the encrypted text
    // Did this above only
}
// Styled using style50
// Solved under 2hrs
// Used some pseudocode from cs50 advice section
