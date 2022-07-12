//help50
//By "undeclared identifier," clang means you've used a name string on line 5 of buggy1.c which hasn't been defined. Did you forget to #include <cs50.h> (in which string is defined) atop your file?

#include <stdio.h>

int main(void)
{
    string name = get_string("What's your name?\n");
    printf("hello, %s", name);
}