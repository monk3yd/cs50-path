//fails to swap two integers

#include <stdio.h>

void swap(int *a, int *b);

int main(void)
{
    int x = 1;
    int y = 2;

    printf("x is %i, y is %i\n", x, y);
    swap(&x, &y);
    printf("x is %i, y is %i\n", x, y);
}

void swap(int *a, int *b) // int *a, in this context means: swap() takes in pointers. that accept the address of an int and call it a.
{
    int tmp = *a; //follow the arrow to whatever a is pointing. it points to the value of x (1). store value in variable tmp
    *a = *b;     //follow the arrow to whatever b is pointing. it points to the value  of y (2). store value (y) in the value a is pointing (x)
    *b = tmp;   //take temp (number 1) and put it on the address in b.
}