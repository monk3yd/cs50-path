//Abstraction and scope

#include <cs50.h>
#include <stdio.h>

int get_positive_int(void);

int main(void)
{
    int i = get_positive_int();
    printf("%i\n", i);
}

// prompt user for positive integer
int get_positive_int(void)      //first value represent output value type, (represent input value type if any)
{
    int n; //garbage value. variable n isn't assigned yet to any value.
    do
    {
        n = get_int("Positive Integer: ");
    }
    while(n < 1);
    return n;
}