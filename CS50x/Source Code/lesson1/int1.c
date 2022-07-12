#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int age = get_int("What's your age?\n");  //Best design imo. Strictly speaking isn't necessary either inflection point example see int2.c
    printf("You are at least %i days old\n", age * 365);
}