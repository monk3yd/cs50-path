#include <stdio.h>

int main(void)
{
   int n = 50;  //variable name n of type int that stores the value 50.
   int *p = &n; // variable name p of type * (pointer) that has the address to an int value called n.
   printf("%p\n", p);   //prints address in memory of variable n. rarely used
   printf("%i\n", *p);  //print the integer at p.*(goto)
}