//change string all to upercase

#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main(void)
{
    string s = get_string("Before: ");
    printf("After: ");
    for (int i = 0, n = strlen(s); i < n; i++) //you declare once if both variables are the same type.
    {
        printf("%c", toupper(s[i])); // I can pass in the current character s[i] to toupper, and if it's lowercase, it's going to return in uppercase, and if it's not a lowercase letter, it's just going to return it unchanged.
    }
    printf("\n");
}