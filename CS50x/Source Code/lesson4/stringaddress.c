//#include <cs50.h>
#include <stdio.h>

int main(void)
{
//a string is quite simply a variable that contains the address of a character.
//a string is just the address of the first byte in the sequence of characters (array).
//terminated by null \0 by human convention
    char *s = "EMMA";       //string s = "EMMA";
    printf("%s\n", s);      //printf("%s\n", s);
    printf("%p\n", s);      //address where emma's name is stored at. exactly the same a infra.
    printf("%p\n", &s[0]);    //address where first letter of emma's name is stored at
    printf("%p\n", &s[1]);
    printf("%p\n", &s[2]);
    printf("%p\n", &s[3]);
    printf("%p\n", &s[4]);
    printf("%c\n", *s);     // s[0]//go to address contained in s, which has the first character in the string.
    printf("%c\n", *(s+1));// s[1]  syntactic sugar but this is actually what happens in clang. arithmetic underneath the hood. no magic.
    printf("%c\n", *(s+2));  //s[2]
    printf("%c\n", *(s+3)); //s[3]
    printf("%s\n", s);
//when you tell printf to use %s it has special meaning and it knows to print not just the first char s[0] but everyone after until \0 null.
}