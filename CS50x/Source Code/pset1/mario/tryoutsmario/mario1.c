#include <cs50.h>
#include <stdio.h>

int main(void)
{
    //prompt user for input until valid data is entered.
    int x;
    do
    {
        x = get_int("Height: ");
    }
    while(x < 1 || x > 8);

    for (int i = 0; i < x; i++)
    {
        for (int j = 0; j <= i; j++)
        {
            for(int k = 7; k >= j; k--)
            {
              printf(".");
            }
            printf("#");
        }
        printf("\n");
    }
}