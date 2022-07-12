//includes
#include <stdio.h>
#include <cs50.h>

//declare functions
int add_two_ints(int a, int b);

int main()
{
    //ask user for input
    int x = get_int("Give me and integer: ");
    int y = get_int("Give me another integer: ");

    //add two numbers together via function call
    int z = add_two_ints(x, y);

    //output the results
    printf("The sum of %i and %i is %i!\n", x, y, z);
}

//definition of function add_two_ints()
int add_two_ints(int a, int b)
{
    int sum = a + b;
    return sum;
}