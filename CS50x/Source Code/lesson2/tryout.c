#include <cs50.h>
#include <stdio.h>

int main(void)
{
    string s[3];
    s[0] = "H";
    s[1] = "I";
    s[2] = "!";
    //printf("%c %c %c\n", c1, c2, c3); //chars are technically numbers.
    //printf("%i %i %i\n", (int) c1, (int) c2, (int) c3); // CAST verb describing the act of converting one data type to another.
    printf("%s %s %s\n", s[0], s[1], s[2]); // implicit cast. Clang understands and treats c like a int because of %i placeholder.
}