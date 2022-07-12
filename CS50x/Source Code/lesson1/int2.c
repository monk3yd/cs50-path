#include <cs50.h>
#include <stdio.h>

int main(void)
{
//design decision:
//for designs sake version int1.c may be a little bit better, because you can read the code more easily or intuitivly.
    printf("You are at least %i days old\n", get_int("What's your age?\n") * 365);
}