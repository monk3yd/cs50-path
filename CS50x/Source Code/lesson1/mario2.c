//Prints a row of n question marks with a loop

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int n;
    do
    {
        n = get_int("Width: ");
    }
    while(n < 1);
    for(int i = 0; i < n; i++) //softcode
    {
        printf("?"); // \n newline here makes ? go for the columns instead of the row
    }
    printf("\n"); // this newline makes prompt don't finish at the side of the ?.
}
