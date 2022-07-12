#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    string names[4] = {"EMMA", "RODRIGO", "BRIAN", "DAVID"};

    for (int i = 0; i < 4; i++)
    {
//if (names[i] == "EMMA") //not going to work. you can't use == for strings. they aren't a simple data type. but an array of  many characters instead.
        if (strcmp(names[i], "EMMA") == 0)
        {
            printf("Found\n");
            return 0;
        }
    }
    printf("Not Found\n");
    return 1;
}