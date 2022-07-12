#include <cs50.h>
#include <stdio.h>

int main(void)
{
    //prompt user for input until valid data is entered.
    int  h;
    do
    {
        h = get_int("Height: ");
    }
    while(h < 1 || h > 8);

    for (int i = 0; i < h; i++)
    {
        for (int j = 0; j <= i; j++)
        {
            for(int k = h - 1; k > i; k--)
            {
                    printf("."); 
            }
            printf("#"); //j++
        }
        printf("\n"); //i++
    }
}