//change string all to upercase

#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    string s = get_string("Before: ");
    printf("After: ");
    for (int i = 0, n = strlen(s); i < n; i++)
    {
        //if the current character is greater than or equal to lower case 'a' && less or equal to lower case 'z'.
        if(s[i] >= 'a' && s[i] <= 'z')
        {
            printf("%c", s[i] - 32); //convert to uppercase. asciichart.com note the difference between the number value of uppercase and its corrresponding lowercase/
        }
        else
        {
            printf("%c", s[i]);
        }
    }
    printf("\n");
}