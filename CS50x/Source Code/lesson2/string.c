#include <cs50.h>
#include <stdio.h>
#include <string.h>
//permits strlen() string length function.

int main(void)
{
    string s = get_string("Input: ");
    printf("Output: ");

            // s[i] != '\0'
            //i < length of s
//1. for (int i = 0; i < strlen(s); i++)
// remember in for loops that the condition in the middle is a boolean expression that you ask on each iteration of the loop. Why are we asking the same question again and again? the answer is not going to change emma's name isn't shrinking or growing, is just emma.

// FIX
//2. declare a variable for storing the question:
//int n = strlen(s);
//for (int i = 0; i < n); i++)


//3. turns out there is special syntax for this too. If you know in a loop that you want to ask a question once and remeber the answer, you can actually use this:
//      intialize i to 0, n to strlen; condition; increment
    for (int i = 0, n = strlen(s); i < n; i++)
    {
        printf("%c", s[i]);
    }
    printf("\n");
}