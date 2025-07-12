// Scrabble pset1
#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

int points[26] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

int main(void)
{
    // Getting input from user for which words
    string word1 = get_string("Player 1: ");
    string word2 = get_string("Player 2: ");

    // Calculate score of each word but also uppercase all letters before
    // Use a for loop to extract the characters from words[i]
    int score1 = 0;
    char CharWord1[strlen(word1)];
    strcpy(CharWord1, word1);
    for (int i = 0; i < strlen(word1); i++)
    {
        CharWord1[i] = toupper(word1[i]);
        if (isalpha(CharWord1[i]))
        {
            score1 += points[CharWord1[i] - 'A'];
        }
    }

    // same thing for char2
    int score2 = 0;
    char CharWord2[strlen(word2)];
    strcpy(CharWord2, word2);

    for (int i = 0; i < strlen(word2); i++)
    {
        CharWord2[i] = toupper(word2[i]);
        if (isalpha(CharWord2[i])) // This checks if it alphabetical
        {
            score2 += points[CharWord2[i] - 'A'];
        }
    }

    // Print the winner
    if (score1 == score2)
    {
        printf("Tie!\n");
    }
    else if (score1 > score2)
    {
        printf("Player 1 Wins!\n");
    }
    else
    {
        printf("Player 2 Wins!\n");
    }
}
