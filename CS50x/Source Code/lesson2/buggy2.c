//Buggy example for printf and debug50

#include <stdio.h>

int main(void)
{
                    //fix i < 10 so that i doesn't count through 10.
    for (int i = 0; i <= 10; i++)
    {
        // this is not the goal of the program, is just a temporary diagnostic meesage for detecting the bug in this program.
        //printf("i is now %i: ", i); //see in real-time the value of i.
        printf("#\n");
    }
}