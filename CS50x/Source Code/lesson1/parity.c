#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int n = get_int("n: ");
    
    if(n % 2 == 0)  // remainder operation. divide n by 2 and if the remainder is equal 0, execute.
    {
        printf("even\n");
    }
    else
    {
        printf("odd\n");
    }
}