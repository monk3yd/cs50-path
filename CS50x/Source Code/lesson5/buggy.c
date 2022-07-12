int main(void)
{
    int *x;     //declares a variable pointer called x.
    int *y;     //declares a variable pointer called y.

    x = malloc(sizeof(int));    //point to a chunk of memory with pointer variable x.

    *x = 42;    //dereference memory pointed by x and store 42 in it.
    //*y = 13;    //buggy. we haven't allocated memory for pointer y.

    y = x;      //pointer y points where pointer x is pointing

    *y = 13;    //replace memoryallocated with value 13
}
