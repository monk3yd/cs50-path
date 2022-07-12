#include <cs50.h>
#include <stdio.h>

int main(int argc, string argv[])
{
    if (argc == 2) //means human has typed two words at their prompt.
    {
        printf("hello, %s\n", argv[1]);
    }
    else
    {
        printf("hello, world\n");
    }
}
// ./argv Juan for running.