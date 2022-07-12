//double value by 2 forever.
#include <cs50.h>
#include <stdio.h>
#include <unistd.h>

int main(void)
{
    for(int i = 1; true; i *= 2)
    {
        printf("%i\n", i);
        sleep(1);               //function is in unistd library.
    }
}

//hardwre is finite. integers work with 32bits.
//overflow is to lose the carried one when counting because you can't stored more info. There aren't enoguh bits. 