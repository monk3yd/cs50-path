// goal to get a string from user (non cap) and capitalize (first letter) of a copy.

#include <cs50.h>
#include <ctype.h>
#include <stdio.h>

int main(void)
{
    char *s = get_string("s: ");    //string s = get_string("s: ");
    char *t = s;    //string t = s;

    t[0] = toupper(t[0]);

    printf("%s\n", s);
    printf("%s\n", t);
}