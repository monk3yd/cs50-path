//very similar to argv.c except instead of saying hello world by default, it yells at the user with this missing command line argumente, and then return one to signal the computer this program do not succed. And i'm going to return zero, if and only if, it did succeed. 

#include <cs50.h>
#include <stdio.h>

int main(int argc, string argv[])
{
    if (argc!= 2) // I literally typed two words at the prompt, even though only one of them is technically an argument i care about.
    {
        printf("missing command-line argument\n");
        return 1; //return 1 if something went wrong.
    }
    printf("hello, %s\n", argv[1]); //in argv the first word you type, the program's name, is stored at argv[0]. The second word you typed, the first argument you care about is argv[1]
    return 0; //exit
}