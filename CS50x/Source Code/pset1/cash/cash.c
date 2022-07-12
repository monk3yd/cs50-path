#include <math.h>
#include <cs50.h>
#include <stdio.h>

int main(void)
{
    float dollars;
    do
    {
        dollars = get_float("Change owed: ");
    }
    while (dollars <= 0);
    
    int cents = round(dollars * 100); //takes a floating point number and rounds it to the nearest integer.
    
    
    //int rco = 0;        //ramaining changed owed = rco      
    int coins = 0;
    
    while (cents > 0)
    {

        if (cents >= 25)
        {
            cents = cents - 25;
            coins++;
        }
        else if (cents < 25 && cents >= 10)
        {
            cents = cents - 10;
            coins++;
        }
        else if (cents < 10 && cents >= 5)
        {
            cents = cents - 5;
            coins++;
        }
        else
        {
            cents = cents - 1;
            coins++;
        }
    }
    //printf("%i\n", cents);
    printf("%i\n", coins);
}
