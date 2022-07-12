#include <stdio.h>

int main(void)
{
    char s[5];  // char *s = NULL;             // give me a variable called s that will store the address of a char
    printf("s: ");              //prompt for the human.
    scanf("%s", s);             //takes format code string %s, and the address of a place to put it. doesn't use * because unlike an int, char * is already, by definition, a pointer or address.
    printf("s: %s\n", s);       // print whatever the human typed in.
}