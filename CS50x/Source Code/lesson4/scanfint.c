#include <stdio.h>

int main(void)
{
    int x;
    printf("x: ");
    scanf("%i", &x); //get integer from the user. the input entered in prompt will get stored at the address of x. you can't only use x because you'll get a copy.
    printf("x: %i\n", x);
}