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
        for (int j = 0; j < (2 * height) + (i - 1); j++)
        {
                                        //j > height - 1 
            if (j < (height - 1) - i || j > height - 1)//(j == varible dots medio || j == variable dots medio))  // formula you can discover with pattern. ***height minus 1, minus i is alwaays the N of dots of the row. 
            {
                printf("."); //j++
            }
            else
            {
                printf("#"); //j++
            }
        }
        printf("\n"); //i++
    }
}