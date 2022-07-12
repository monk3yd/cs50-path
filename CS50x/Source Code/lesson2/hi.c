#include <stdio.h>

int main(void)
{
    char c1 = 'H';
    char c2 = 'I';
    char c3 = '!';
    //printf("%c %c %c\n", c1, c2, c3); //chars are technically numbers.
    //printf("%i %i %i\n", (int) c1, (int) c2, (int) c3); // CAST verb describing the act of converting one data type to another.
    //printf("%i %i %i\n", c1, c2, c3); // implicit cast. Clang understands and treats c like a int because of %i placeholder.
}