// Prints an n-by-n grid of bricks with a loop

#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int x;
    do
    {
        x = get_int("size: ");
    }
    while(x < 1);
    //syntax for saying "do the following n times"
    for(int i = 0; i < x; i++) //function prints n number of rows, executing inner loop for each one.
    {
        for(int j = 0; j < x; j++) //function prints n number of # in each row
        {
            printf("#"); //print # for the rows
        }
        printf("\n");   //print newline
    }
    
}

