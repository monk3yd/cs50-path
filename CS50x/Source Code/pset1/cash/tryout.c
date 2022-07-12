#include <math.h>
#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int quarters = 25;
    int dimes = 10;
    int nickels = 5;
    int pennies = 1;
    
    int x = quarters / nickels;
    
    printf("%i\n", x);
}
