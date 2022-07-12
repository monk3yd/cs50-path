// http://valgrind.org/docs/manual/quick-start.html#quick-start.prepare //online valgrind manual

#include <stdlib.h>

void f(void)
{
    int *x = malloc(10 * sizeof(int));  // allocating memory of 40 bytes. array of memory you can store 40 integers in. Dynamic way of allocating. You could put the number of bytes depending on data type but it would require you learning how much memory each one uses.
    x[9] = 0;   // x[10] = 0;  //buffer (array) overflow because they are 0 index.
    free(x);
}

int main(void)
{
    f();
    return 0;
}