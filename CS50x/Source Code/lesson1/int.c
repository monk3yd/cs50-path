#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int age = get_int("What's your age?\n");
    int days = age * 365;               //strictly speaking you don't need this. see int1.c
    printf("You are at least %i days old\n", days);
}