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

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < height; j++) //need to change to height instead of i. keep the idea you must make a square but using different symbols.
        {
            if (j < (height - 1) - i) // formula you can discover with pattern. height minus 1, minus i is alwaays the N of dots of the row. 
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