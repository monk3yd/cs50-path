#include <stdio.h>

int main(void)
{
    int n = 50;
    //printf("%i\n", n);        50
    //printf("%p\n", &n);       %p format code to print address : 0x7ffefbbc939c
    printf("%i\n", *&n);    //  50
}