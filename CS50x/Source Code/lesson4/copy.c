// goal to get a string from user (non cap) and capitalize (first letter) of a copy.

#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(void)
{
    char *s = get_string("s: "); //get string from user.

    char *t = malloc(strlen(s) + 1); //malloc permits to allocate memory for ourselves preparing the copy.

    strcpy(t,s); //function that replicates the loop that copies the string.

    //for (int i = 0, n = strlen(s); i <= n; i++) //iterate copying character by character from s string to p string.
    //{
        //t[i] = s[i];
    //}

    t[0] = toupper(t[0]); //capitalizing the first letter.

    printf("%s\n", s);
    printf("%s\n", t);
    free(t);    //free memory  //valgrind ./name  and  help50 valgrind ./name debugging tool for memory leaks.
}