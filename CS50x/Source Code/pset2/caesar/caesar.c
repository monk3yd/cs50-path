#include <stdio.h>
#include <cs50.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

const int A = 65;
const int B = 97;

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

    string text = get_string("plaintext: ");
    printf("ciphertext: ");

//alphabetical index

    //string index = "ABCDEFGHJKLMNOPQRSTUVWXYZ";

//iterare over each character of plaintext

    for (int j = 0, m = strlen(text); j < m; j++)
    {
//If it is an uppercase letter,
        if (isalpha(text[j]) && isupper(text[j]))
        {
//rotate it, preserving case, then print out the rotated character
            int x = text[j] - A; //pass ascii to alphabetical
            int c = (x + k) % 26;
            printf("%c", c + A);
        }
        else if (isalpha(text[j]) && islower(text[j]))
        {
//If it is a lowercase letter, rotate it, preserving case, then print out the rotated character
            int y = text[j] - B; //pass ascii to alphabetical
            int d = (y + k) % 26;
            printf("%c", d + B);
        }
        else
        {
//If it is neither, print out the character as is
            printf("%c", text[j]);
        }
    }
//print newline
    printf("\n");
    return 0;
}