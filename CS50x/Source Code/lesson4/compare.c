#include <cs50.h>
#include <stdio.h>

int main(void)
{
    //get two integers
    string s = get_string("s: ");
    string t = get_string("t: ");
    
    //compare integers
    if (s == t)
    {
        printf("Same\n");
    }
    else
    {
        printf("Different\n");
    }
//it makes sense because each "string" variable is pointing to a different location in memory.
}