#include <stdio.h>
#include <cs50.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

//check that number of arguments in command line are equal to 1

int main(int argc, string argv[])
{
     if (argc != 2)
     {
         printf("Usage: ./caesar key\n");
         return 1;
     }

//iterate through argument and check if all characters are digits.

    for (int i = 0, n = strlen(argv[1]); i < n; i++)
    {
        if (argv[1][i] < '0' || argv[1][i] > '9')
        {
            printf("Usage: ./caesar key\n");
            return 1;
        }
    }

//convert command-line argument from a string to an int

    int k = atoi(argv[1]);

//get and store plaintext by prompting the user

    string plaintext = get_string("plaintext: ");
    printf("ciphertext: ");

    //har letters[] = {'A','B','C'

//iterare over each character of plaintext

    for (int j = 0, m = strlen(plaintext); j < m; j++)
    {
        if (plaintext[j] >= 'A' && plaintext[j] <= 'Z')
        {
//If it is an uppercase letter, rotate it, preserving case, then print out the rotated character
            printf("%c", plaintext[j] + k);
        }
        else if (plaintext[j] >= 'a' && plaintext[j] <= 'z')
        {
//If it is a lowercase letter, rotate it, preserving case, then print out the rotated character
            printf("%c", plaintext[j] + k);
        }
        else
        {
//If it is neither, print out the character as is
            printf("%c", plaintext[j]);
        }
    }
//print newline
    printf("\n");
    return 0;
}