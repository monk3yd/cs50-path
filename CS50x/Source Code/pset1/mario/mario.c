#include <cs50.h>
#include <stdio.h>

int main(void)
{
    //prompt user for input until valid data is entered.
    int  height;
    do
    {
        height = get_int("Height: ");
    }
    while (height < 1 || height > 8);

    for (int i = 0; i <= height - 1; i++)
    {
        for (int j = 0; j <= (height + 2) + i; j++)
        {
            if (j < (height - 1) - i || (j >= height && j < height + 2))
            {
                printf(" "); //j++
            }
            else
            {
                printf("#"); //j++
            }
        }
        printf("\n"); //i++
    }
}